from dash import html


class PageBuilder:
    def __init__(
        self,
        name: str,
    ):
        self.page_name = name
        self.page_container_id = f"page_container_{self.page_name}"
        self.layout = html.Div(children=[], id=self.page_container_id, className="page")

    def extend_layout(self, layout: html.Div, position: int = 0) -> None:
        self.layout.children.insert(position, layout)

    def _regsiter_callbacks(self) -> None:
        return

    def build(self) -> html.Div:
        self._regsiter_callbacks()
        return self.layout

    @property
    def elements_raw(self) -> dict[str, str]:
        return {
            "PAGE_CONTAINER": self.page_container_id,
        }

    @property
    def elements(self) -> type:
        return type("Elements", (), self.elements_raw)
