import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from components.single_player_card import create_player_card


def get_players_cards(players):
    return [dcc.Link(create_player_card(player), href=f'/analytics/{player["name"]}', refresh=True) 
            for player in players]


def create_layout(players):
    players_cards = get_players_cards(players)
    layout = []
    for i in range(0, len(players_cards), 2):
        row = []
        for j in range(i, i + 2):
            if j >= len(players_cards):
                break
            row.append(dbc.Col(players_cards[j]))
        layout.append(dbc.Row(row))
    return html.Div(layout)


players = [{'name': 'Barabasz60', 'id': '1'},
           {'name': 'Jane Doe', 'id': '2'},
           {'name': 'pawel', 'id': '3'},
           {'name': 'ala', 'id': '4'}
           ]


def create_home(app) -> dbc.Card:
    return dbc.Container([
        create_layout(players)
    ]
    )
    