import reflex as rx

from ..components.abstract import abstract
from ..components.adtec import adtec
from ..components.cite import cite
from ..components.dataset_card import dataset_card
from ..components.discussion import discussion
from ..components.examples import examples
from ..components.experiments import experiments
from ..components.footer import footer
from ..components.hero import hero
from ..components.navbar import navbar
from ..components.tasks import tasks


@rx.page(route="/")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        navbar(),
        hero(),
        adtec(),
        abstract(),
        tasks(),
        dataset_card(),
        examples(),
        experiments(),
        discussion(),
        cite(),
        footer(),
        spacing="2",
        justify="center",
        align="center",
        min_height="85vh",
    )
