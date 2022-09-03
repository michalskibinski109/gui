from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc


def create_layout(app: Dash) -> html.Div:
    return dbc.Container(
        className='main',
        children=[
            dcc.Location(id='path'),
            html.H1(app.title),
            html.Hr(),
            html.Div(id='main_container')
        ], fluid=True)
