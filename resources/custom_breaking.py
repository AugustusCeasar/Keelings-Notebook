import dataclasses
import random


@dataclasses.dataclass
class BaseBreakerStats:
    name: str
    cost: int
    memory: int
    strength: int
    subtypes: str


base_stats = [BaseBreakerStats("Audrey", 3, 2, 0, "Icebreaker - AI - Virus "),
              BaseBreakerStats("Banner", 4, 1, 5, "Icebreaker - Fracter - Weapon"),
              BaseBreakerStats("Curupira", 3, 1, 1, "Icebreaker - Fracter"),
              BaseBreakerStats("Shibboleth", 1, 1, 3, "Icebreaker - Decoder"),
              BaseBreakerStats("Living Mural", 3, 1, 1, "Icebreaker - Killer - Trojan"),
              BaseBreakerStats("Slap Vandal", 1, 1, 6, "Icebreaker - AI - Trojan"),
              BaseBreakerStats("Umbrella", 3, 1, 5, "Icebreaker - Decoder - Weapon")]
str_boosts = ["**Trash 1 card from your grip:** +3 strength.",
              "",
              "**1c:** +1 strength.",
              "**2c:** +2 strength.",
              "**1c:** +2 strength."
              "",
              ""]
interfaces = ["**Hosted virus counter:** Break up to 2 subroutines.",
              "**2c:** Subroutines on the barrier you are encountering cannot end the run for the remainder of this encounter.",
              "**1c:** Break 1 barrier subroutine.",
              "**1c:** Break 1 code gate subroutine.",
              "**1c:** Break 1 subroutine on a sentry protecting this server.",
              "**1c:** Break 1 subroutine on host ice. Use this ability only once per encounter.",
              "** 2c:** Break up to 3 code gate subroutines. If at least 1 subroutine was broken this way, each player may draw 1 card."]
special_abilities = ["Whenever you trash a card you are accessing, place 1 virus counter on this program.",
                     "",
                     """Whenever you encounter a barrier, you may spend 3 hosted power counters to bypass it.
Whenever this program fully breaks a piece of ice, place 1 power counter on this program.""",
                     "Threat 4 → This program gets −2 strength.",
                     "Threat 4 → When you install this program, it gets +3 strength for the remainder of the turn.",
                     "Install only on a piece of ice.",
                     "This program can only interface with ice hosting a trojan program."]

secret_abilities = ["Whenever you trash a card you are accessing, place 2 virus counter on this program.",
                    "",
                    """Whenever you encounter a barrier, you may spend 3 hosted power counters to bypass it and the next ice you encounter.
Whenever this program fully breaks a piece of ice, place 1 power counter on this program.""",
                    "Threat 8 → This program gets −4 strength.",
                    "Threat 2 → When you install this program, it gets +6 strength for the remainder of the turn.",
                    "**1c:** Host this program on a piece of ice.  ",
                    "This program's abilities cost 1 less **c** when interfacing with ice hosting a trojan program."]

nameparts = [["Au", "dr", "-ey", " v2"],
             ["Ban", "", "-ner", ""],
             ["Cu", "ru", "-pi", "ra"],
             ["Shi", "bb", "-ol", "eth"],
             ["Li", "ving", " Mur", "al"],
             ["Slap", "", " Van", "dal"],
             ["Um", "", "-bre", "lla"]]


def get_random_breaker():
    base_stats_i = random.randint(0, len(base_stats)-1)
    str_boost_i = random.randint(0, len(str_boosts)-1)
    interface_i = random.randint(0, len(interfaces)-1)
    ability1_i = random.choice([0, 2, 3, 4, 5, 6])
    ability2_i = random.choice([0, 2, 3, 4, 5, 6])
    c_base_stats = base_stats[base_stats_i]
    c_str_boost = str_boosts[str_boost_i]
    c_interface = interfaces[interface_i]
    c_ability = special_abilities[ability1_i]
    c_ability2 = ""
    if not c_str_boost:
        c_ability2 = "\n" + special_abilities[ability2_i]
        if c_ability == c_ability2:
            c_ability2 = ""
            c_ability = secret_abilities[special_abilities.index(c_ability)]

    return f"""{nameparts[base_stats_i][0]}{nameparts[str_boost_i][1]}{nameparts[interface_i][2]}{nameparts[ability1_i][3]}{nameparts[ability2_i][3] if c_ability2 else ""}
**Program:** {c_base_stats.subtypes}
{c_base_stats.memory} MU \\* {c_base_stats.strength} strength
{c_ability}{c_ability2}
{c_interface}
{c_str_boost}"""
