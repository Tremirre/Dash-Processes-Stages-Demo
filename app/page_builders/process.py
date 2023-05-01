from dash import html, dcc, callback, Output, Input, State, callback_context, ALL

from .general import PageBuilder


class ProcessPageBuilder(PageBuilder):
    def __init__(self, name: str):
        super().__init__(name)
        self.stages = []
        self.stages_container_id = f"stages_container_{name}"
        self.stages_store_id = f"stages_store_{name}"
        self.next_stage_btn_id = f"next_stage_{name}"
        self.previous_stage_btn_id = f"previous_stage_{name}"
        self.stage_blocker_id = f"stage_blocker_{self.page_name}"
        self.layout.children.extend(
            [
                html.Div(children=[], id=self.stages_container_id),
                dcc.Store(id=self.stages_store_id, data=0),
                html.Div(
                    children=[
                        html.Button("Previous", id=self.previous_stage_btn_id),
                        html.Button("Next", id=self.next_stage_btn_id),
                    ]
                ),
            ]
        )

    def make_stage_blocker(self) -> dcc.Store:
        return dcc.Store(
            id={"type": self.stage_blocker_id, "index": len(self.stages)}, data=False
        )

    def add_stage(self, stage: html.Div) -> None:
        stage.children.insert(0, self.make_stage_blocker())
        self.stages.append(stage)

    def add_stages(self, stages: list[html.Div]) -> None:
        for stage in stages:
            self.add_stage(stage)

    def _regsiter_callbacks(self):
        @callback(
            [
                Output(self.stages_container_id, "children"),
                Output(self.stages_store_id, "data"),
            ],
            [
                Input(self.next_stage_btn_id, "n_clicks"),
                Input(self.previous_stage_btn_id, "n_clicks"),
            ],
            [
                State(self.stages_store_id, "data"),
            ],
        )
        def update_stages(next_clicks, previous_clicks, current_stage):
            ctx = callback_context
            triggered = ctx.triggered[0]["prop_id"].split(".")[0]
            if triggered == self.next_stage_btn_id:
                current_stage = min(current_stage + 1, len(self.stages) - 1)
            elif triggered == self.previous_stage_btn_id:
                current_stage = max(current_stage - 1, 0)
            return self.stages[current_stage], current_stage

        @callback(
            [
                Output(self.previous_stage_btn_id, "disabled"),
                Output(self.next_stage_btn_id, "disabled"),
            ],
            [
                Input(self.stages_store_id, "data"),
                Input({"type": self.stage_blocker_id, "index": ALL}, "data"),
            ],
        )
        def update_buttons(current_stage, values):
            blocker = values[0]
            cant_go_backward = current_stage <= 0
            cant_go_forward = (current_stage >= len(self.stages) - 1) or blocker
            return cant_go_backward, cant_go_forward

    @property
    def elements_raw(self) -> dict[str, str]:
        return {
            "STAGES_CONTAINER": self.stages_container_id,
            "STAGES_STORE": self.stages_store_id,
            "NEXT_BTN": self.next_stage_btn_id,
            "PREV_BTN": self.previous_stage_btn_id,
            "BLOCKER": self.stage_blocker_id,
            **super().elements_raw,
        }

    def build(self) -> html.Div:
        return super().build()
