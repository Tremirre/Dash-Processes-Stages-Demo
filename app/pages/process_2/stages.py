from dash import html

stage_a = html.Div(
    [
        html.H2("Stage A"),
        html.P("Stage A"),
    ]
)

stage_b = html.Div(
    [
        html.H2("Stage B"),
        html.P("Stage B"),
    ]
)

STAGES = [stage_a, stage_b]
