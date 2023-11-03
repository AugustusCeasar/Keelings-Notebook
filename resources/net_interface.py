import asyncio
from typing import Union

from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession, AsyncHTMLSession
from dataclasses import dataclass

from config import team_names_list

@dataclass
class HtmlElement:
    name: str
    class_attr: Union[str, None] = None  # None has the meaning that this element has no attributes, e.g. <div>..</div>
    all_attrs: dict[str, str] = None

    @staticmethod
    def find_in_html(html, element):
        return html.find(element.name, attrs=element.all_attrs or {"class": element.class_attr})

    @staticmethod
    def find_all_in_html(html, element):
        return html.find_all(element.name, attrs=element.all_attrs or {"class": element.class_attr})


@dataclass
class StraightHtmlHierarchy:
    elements: tuple[HtmlElement, ...]

    def parse_to_end(self, bs_html_body):
        c_state = bs_html_body
        for e in self.elements:
            c_state = HtmlElement.find_in_html(c_state,
                                               e)  # c_state.find(e.name, attrs=e.all_attrs or {"class": e.class_attr})
        return c_state


HTML_STRUCTURE_TO_GAME_LIST = StraightHtmlHierarchy((
    HtmlElement("div", all_attrs={"id": "main-content"}),
    HtmlElement("div", all_attrs={"id": "main"}),
    HtmlElement("div", class_attr="game-list"),
))
PLAYER_LINE_ELEMENT = HtmlElement("div", class_attr="gameline")
HTML_STRUCTURE_TO_PLAYERS = StraightHtmlHierarchy((
    HtmlElement("div", class_attr=None),
))
INDIVIDUAL_PLAYER_ELEMENT = HtmlElement("span", class_attr="player")
HTML_STRUCTURE_TO_NAME_TEXT = StraightHtmlHierarchy((
    HtmlElement("span", class_attr="user-status"),
))


async def get_current_jnet_play_page(load_wait=1.0):
    session = AsyncHTMLSession()
    r = await session.get("https://www.jinteki.net/play")
    await r.html.arender(sleep=load_wait)

    return bs(r.html.html, features="lxml")


async def get_all_active_players():
    current_jnet_play = await get_current_jnet_play_page()
    player_list = HTML_STRUCTURE_TO_GAME_LIST.parse_to_end(current_jnet_play.body)
    player_pairs = []
    for player_line in HtmlElement.find_all_in_html(player_list, PLAYER_LINE_ELEMENT):
        players_html = HTML_STRUCTURE_TO_PLAYERS.parse_to_end(player_line)
        players_text = []
        for p in HtmlElement.find_all_in_html(players_html, INDIVIDUAL_PLAYER_ELEMENT):
            players_text.append(HTML_STRUCTURE_TO_NAME_TEXT.parse_to_end(p).find(string=True, recursive=False))
        player_pairs.append(players_text)
    return player_pairs


async def get_online_team_members():
    all_players = await get_all_active_players()
    test_games = []  # of one teammate vs another
    free_players = []  # team members playing against a rando

    for players in all_players:
        filtered_players = [p for p in players if p in team_names_list]
        if len(filtered_players) == 1:
            free_players.append(filtered_players[0])
        elif len(filtered_players) >= 2:
            test_games.append(filtered_players)

    return free_players, test_games


if __name__ == "__main__":
    members = asyncio.run(get_online_team_members())
    print(members)
    # print(get_all_active_players())

"""
from timeloop import Timeloop
from datetime import timedelta
tl = Timeloop()


@tl.job(interval=timedelta(seconds=10))
def send_or_update_jnet_message():
    print(asyncio.run(get_online_team_members()))
# tl.start()
# tl.stop()"""