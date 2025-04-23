import reflex as rx

from .. import constants, styles


def abstract() -> rx.Component:
    """Abstract component."""

    return rx.container(
        rx.vstack(
            rx.accordion.root(
                rx.accordion.item(
                    header=rx.text("Abstract"),
                    content=styles.markdown(constants.ABSTRACT_MD),
                ),
                rx.accordion.item(
                    header="What's Search Engine Ads?",
                    content=styles.image(
                        src="/search-engine-ad.png",
                        caption="An example of a search engine ad.",
                        width="50%",
                    ),
                    align="center",
                    justify="center",
                ),
                rx.accordion.item(
                    header="AdOps and its Workflow",
                    content=styles.image(
                        src="/adops-workflow.png",
                        caption="The workflow of AdOps.",
                    ),
                ),
                width="100%",
                radius="small",
                collapsible=True,
                type="multiple",
                variant="outline",
                color_scheme="gray",
            ),
        ),
        width="100%",
        height="100%",
        align="center",
    )
