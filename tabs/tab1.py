from dash import Dash, html
import dash_bootstrap_components as dbc
import ids
from dropdowns import dropdown, year_dropdown, time_class_dropdown
from components.bar_chart import create_bar_chart


def render(app, df):
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
