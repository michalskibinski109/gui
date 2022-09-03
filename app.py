from zlib import adler32
from dash import Dash, html, dcc, Input, Output
import dash
import ids
import dash_bootstrap_components as dbc
from layout import create_layout
from pages.analytics import create_analytics
from pages.home import create_home

app = Dash(__name__,  external_stylesheets=[dbc.themes.DARKLY])
app.title = 'chess dashboard'
app.layout = create_layout(app)
app.config.suppress_callback_exceptions=True

@app.callback(
    dash.dependencies.Output(ids.MAIN_CONTAINTER, 'children'),
    [dash.dependencies.Input(ids.PATH, 'pathname')])
def update_output(value:str):
    if value == '/':
        return create_home(app)
    adress = value.split('/')
    if 'analytics' in adress:
        PLAYER = adress[-1]
        return create_analytics(app, PLAYER)
if __name__ == '__main__':
    app.run_server(debug=True)
