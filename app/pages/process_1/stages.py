from dash import html, dcc


upload_stage = html.Div(
    [
        html.H2("Upload"),
        html.P("Upload your data here"),
        dcc.Upload(
            id="upload_data",
            children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
            },
            multiple=True,
        ),
        html.Div(id="upload_data_output"),
    ]
)

process_stage = html.Div(
    [
        html.H2("Process"),
        html.P("Process your data here"),
        html.Div(id="process_data"),
        dcc.Graph(id="process_graph"),
    ]
)

finish_stage = html.Div(
    [
        html.H2("Finish"),
        html.P("Finish your data here"),
        html.Div(id="finish_data"),
        html.Button(id="error-thrower", children="Throw error")
    ]
)

STAGES = [upload_stage, process_stage, finish_stage]
