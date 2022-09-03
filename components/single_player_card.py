import dash_bootstrap_components as dbc
from dash import html

def create_player_card(data = None):  
    return dbc.Button(
        id = data['id'],
    children=[
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/static/images/placeholder.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4(data['name'], className="card-title"),
                            html.P(
                                "This is a wider card with supporting text ",
                                className="card-text",
                            ),
                            html.Small(
                                "Last updated 3 mins ago",
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px"},
)