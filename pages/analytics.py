from dash import html
import pandas as pd
import dash_bootstrap_components as dbc
from pages.default import create_default
import os
from pathlib import Path
from components.bar_chart import create_bar_chart
from tabs import tab1


def find_path(PLAYER, path='./data'):
    for p in os.listdir(path):
        name = Path(os.path.abspath(p)).stem
        if PLAYER == name:
            return os.path.join(path, p)
    return None


def load_df(path):
    if not path:
        return None
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    return df


def create_analytics(app, PLAYER=None) -> dbc.Card:
    if not PLAYER:
        return create_default()
    path = find_path(PLAYER)
    df = load_df(path)
    
    
    import ids
    from dropdowns import dropdown, year_dropdown, time_class_dropdown
    from components.bar_chart import create_bar_chart
    return dbc.Card(
        dbc.CardBody([
            html.Hr(),
            html.Div(
                className='dropdown-container',
                style={'display': 'flex', 'flex-direction': 'row',
                    'flex-shrink': '0', },
                children=[
            year_dropdown.render(app, df, id = ids.YEAR_DROPDOWN_BAR),
            time_class_dropdown.render(app, df, id=ids.TIME_CLASS_DROPDOWN)]
                
            ),
            create_bar_chart(app, df)
        ]),
        style = {'width': '100%', 'height': '75vh'})
    
    return dbc.Tabs([tab1.render(app, df)])
