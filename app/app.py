import dash
import dash.html
import dash.dcc

app = dash.Dash(__name__, suppress_callback_exceptions=True, use_pages=True)

app.layout = dash.html.Div(
    [
        dash.html.Header(
            [
                dash.dcc.Link(page["name"] + " ", href=page["path"])
                for page in dash.page_registry.values()
            ],
            id="page-header",
        ),
        dash.html.Div(id="page-content", children=[dash.page_container]),
        dash.html.Div(id="error-box", style={"color": "red"}),
        dash.dcc.Store(id="error-msg", data=""),
        dash.html.Div(id="dummy"),
    ],
    id="app-container",
)


app.clientside_callback(
    """
    function(error_msg) {
        if (error_msg.length > 0) {
            showErrorMessage(error_msg);
        }
    }
    """,
    dash.Output("dummy", "children"),
    dash.Input("error-msg", "data"),
)
