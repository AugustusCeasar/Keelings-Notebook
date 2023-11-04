import re

bot_state_json_path = "bot_state.json"


team_names_list = ["aksu", "AugustusCaesar", "J0N4LD", "xdg", "HaverOfFun", "Baa Ram Wu",
                   "Gathzen", "Jai", "profwacko", "reubenpieters"]

owner_user_id = 393788845021200385
brewing_channel_id = 1133092635993718794
find_the_truth_role_id = 1167845775875788851

# decoding_re must contain a timestring group, where XX/XX/XXXX and XX:XX:XX are located
# and a timezone group containing the timezone (that can only be an integer relative to GMT with current impl)
# GMT is advised against in times of daylight savings
time_decoding_re = re.compile(r"%(?P<timestring>.*)([Uu][Tt][Cc](?P<timezone>[+-]\d\d?))?%")  # (?P<tzmode>UTC|GMT)

help_message = "Welcome to the usage of the most useful tool of the net. Its abilities are:\n" \
               "-**Find the Truth**: Automatic addition of people with a role to all threads created in certain " \
               "channels. (currently only for hardcoded channels cause im lazy, if you want more of them let me know " \
               "and ill stop procrastinating)\n" \
               "-**Conversion of Timezone messages**. If you surround any time/date you want to coordinate with with " \
               "two `%` and include a timezone in the form of `UCT+-XY` (or just UTC equivalently to UCT+0), " \
               "this bot will respond with a discord timestamp that will show each user the conversion of " \
               "that time to their local time. Acceptable formats for dates/times are:\n" \
               "\t*`%15/5/23 UTC%`\n" \
               "\t*`%2.11 UTC+2%`\n" \
               "\t*`%23-02-2024 UTC-1%` (always Day Month Year, sorry americans)\n" \
               "\t*`%10th UTC-5%`\n" \
               "\t*`%20:30 UTC+0%`\n" \
               "\t*`%20: UTC%`\n" \
               "\t*`%on the 2nd of this month at 15:15 UTC%` (or any text that includes 2nd/3rd/4th...)\n"  \
               "\t*`%02/11 @ 23:55 UTC%`\n" \
               "-**Inter Server Communication**: WIP\n" \
               "-**Disable Function**: WIP\n"
