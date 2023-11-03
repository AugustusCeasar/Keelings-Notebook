import datetime
import re
import time

import pytz
from pytz import timezone

from config import time_decoding_re


def parse_time_message(s):
    possible_match = time_decoding_re.search(s)
    if not possible_match:
        return None

    time_string = possible_match.group("timestring") or "0"
    timezone_offset_parsed = datetime.timedelta(hours=int(possible_match.group("timezone")))
    # tzmode = possible_match.group("tzmode")  # either UTC or GMT as reference

    parsed_date = re.search(
        r"(?P<day>\d\d?)(([/\-\.](?P<month>\d\d?)([/\-\.](?P<year>\d\d\d?\d?))?)|(th)|(st)|(nd)|(rd))",
        time_string)
    parsed_time = re.search(r"(?P<hours>\d\d?):(?P<minutes>\d\d?)?(:(?P<seconds>\d\d?))?", time_string)

    # default dates can cause some funny behaviour around edges of timespans for some timezones
    # but when dates are left unspecified these shouldnt change anything of importance
    today = datetime.date.today()
    day = (parsed_date.group("day") if parsed_date else None) or today.day
    month = (parsed_date.group("month") if parsed_date else None) or today.month
    year = (parsed_date.group("year") if parsed_date else None) or today.year
    hours = (parsed_time.group("hours") if parsed_time else None) or 12
    minutes = (parsed_time.group("minutes") if parsed_time else None) or 0
    seconds = (parsed_time.group("seconds") if parsed_time else None) or 0
    parsed_dt_before_tz = datetime.datetime(int(year), int(month), int(day), int(hours), int(minutes), int(seconds))

    # if tzmode == "GMT": #fuck GMT offsets
    #    gmt_utc_offset = pytz.timezone("GMT").utcoffset() # localize(parsed_dt_before_tz) - parsed_dt_before_tz
    #    timezone_offset_parsed = timezone_offset_parsed+gmt_utc_offset

    dt_after_tz_ofset = parsed_dt_before_tz - timezone_offset_parsed

    style = "F"
    if parsed_time is None or parsed_time.group("hours") is None:
        style = "D"
    if parsed_date is None or parsed_date.group("day") is None:
        if parsed_time.group("seconds") is None:
            style = "t"
        else:
            style = "T"
    return f"Your Quality Time message has been decoded to be " \
           f"<t:{int(time.mktime(dt_after_tz_ofset.timetuple()))}:{style}>"


def test_parse():
    print(parse_time_message("some random stuff %10th at 20:15 UTC+1%"))


if __name__ == "__main__":
    test_parse()
