import reflex as rx

from ..components.abstract import abstract
from ..components.adtec import adtec
from ..components.cite import cite
from ..components.examples import examples
from ..components.footer import footer
from ..components.hero import hero
from ..components.navbar import navbar


@rx.page(route="/")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        navbar(),
        hero(),
        adtec(),
        abstract(),
        examples(),
        cite(),
        footer(),
        spacing="2",
        justify="center",
        align="center",
        min_height="85vh",
    )
