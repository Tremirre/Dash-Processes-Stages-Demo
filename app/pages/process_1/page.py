from dash import register_page

from app.page_builders import ProcessPageBuilder
from app.pages.process_1.stages import STAGES
from app.pages.process_1.callbacks import register_callbacks


NAME = "Process 1"
register_page(path="/process_1", name=NAME, module=__name__)

builder = ProcessPageBuilder(name=NAME)
builder.add_stages(STAGES)
layout = builder.build()

register_callbacks(builder.elements)
