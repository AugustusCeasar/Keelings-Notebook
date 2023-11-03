import re

team_names_list = ["aksu", "AugustusCaesar", "J0N4LD", "xdg", "HaverOfFun", "Baa Ram Wu",
                   "Gathzen", "Jai", "profwacko", "reubenpieters"]

brewing_channel_id = 1133092635993718794
find_the_truth_role_id = 1167845775875788851

# decoding_re must contain a timestring group, where XX/XX/XXXX and XX:XX:XX are located
# and a timezone group containing the timezone (that can only be an integer relative to GMT with current impl)
# GMT is advised against in times of daylight savings
time_decoding_re = re.compile(r"%(?P<timestring>.*)UTC(?P<timezone>[+-]\d\d?)?%")  # (?P<tzmode>UTC|GMT)

help_message = "Welcome to the usage of the most useful tool of the net. Its abilities are:\n" \
               "-**Find the Truth**: Automatic addition of people with a role to all threads created in certain " \
               "channels. (currently only for hardcoded channels cause im lazy, if you want more of them let me know " \
               "and ill stop procrastinating)\n" \
               "-**Conversion of Timezone messages**. If you surround any time/date you want to coordinate with with " \
               "two `%` and include a timezone in the form of `UCT+-XY` (or just UTC equivalently to UCT+0), " \
               "this bot will respond with a discord timestamp that will show each user the conversion of " \
               "that time to their local time. Acceptable formats for dates/times are:\n" \
               "\t*`%DD/MM/YYYY UTC%` (D/M/YY also recognised) (if year missing current year will be assumed)\n" \
               "\t*`%HH:MM:SS UTC%` (H:M:S recognised but discouraged)\n" \
               "\t*`%10th UTC%` (current month/year assumed) (fluff will be ignored, eg `on the 10th` read as `10th`)" \
               "\n\t*some combination of the above time and date\n" \
               "-**Inter Server Communication**: WIP\n" \
               "-**Disable Function**: WIP\n"
