from dash import register_page

from app.page_builders import ProcessPageBuilder
from app.pages.process_2.stages import STAGES


NAME = "Process 2"
register_page(path="/process_2", name=NAME, module=__name__)

builder = ProcessPageBuilder(name=NAME)
builder.add_stages(STAGES)

layout = builder.build()
