import dash
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc

def create_default() -> dbc.Card:
    return dbc.Card(dbc.CardBody([
        html.H2(children='Player not selected.'),
    ]))
    