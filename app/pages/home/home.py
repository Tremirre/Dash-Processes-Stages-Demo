from dash import dcc, html, register_page
from app.page_builders import PageBuilder

NAME = "Home"
register_page(path="/", name=NAME, module=__name__)
builder = PageBuilder(name=NAME)

builder.extend_layout(
    html.Div(
        [
            html.H1(NAME),
            html.P("Welcome to the home page"),
        ]
    )
)

layout = builder.build()
