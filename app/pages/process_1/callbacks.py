from dash import html, no_update, callback, Output, Input
from plotly import express as px

from app.error import throwable, DashboardError


# ==== upload_stage callbacks ====
def validate_content(contents, filenames):
    if any(filename[-4:] == "pptx" for filename in filenames):
        raise DashboardError("PPTX files are not allowed")


@throwable(2)
def upload_data(contents, filenames, last_modified):
    if contents is None:
        return no_update, True
    validate_content(contents, filenames)
    return (
        html.Div(
            [
                html.H5(filenames),
                html.Hr(),
                html.Div(contents),
                html.Hr(),
            ]
        ),
        False,
    )


# ==== process_stage callbacks ====


def load_chart(current_stage):
    if current_stage != 1:
        return no_update
    return px.scatter(x=[1, 2, 3], y=[1, 2, 3])


# ==== finish_stage callbacks ====


@throwable(1)
def throw_error(n_clicks):
    if not n_clicks:
        return no_update
    raise DashboardError("Le-Error")


def register_callbacks(elements):
    callback(
        Output("upload_data_output", "children"),
        Output({"type": elements.BLOCKER, "index": 0}, "data"),
        Output("error-msg", "data"),
        Input("upload_data", "contents"),
        Input("upload_data", "filename"),
        Input("upload_data", "last_modified"),
        # prevent_initial_call=True,
    )(upload_data)
    callback(
        Output("process_graph", "figure"),
        Input(elements.STAGES_STORE, "data"),
    )(load_chart)
    callback(
        Output("dummy", "className"),
        Output("error-msg", "data", allow_duplicate=True),
        Input("error-thrower", "n_clicks"),
        prevent_initial_call=True,
    )(throw_error)
    callback(
        Output("finish_data", "children"),
        Input(elements.STAGES_STORE, "data"),
    )(lambda stage: f"Stage: {stage}")
