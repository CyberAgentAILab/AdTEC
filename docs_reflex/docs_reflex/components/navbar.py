import reflex as rx

from .. import constants, styles


class ScrollState(rx.State):
    navbar_shadow: bool = False

    @rx.event
    def show_navbar_shadow(self):
        self.navbar_shadow = True


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    styles.navbar_link(
                        rx.heading(
                            constants.TITLE,
                            size="4",
                            weight="bold",
                        ),
                        href="/",
                        on_click=rx.scroll_to("top"),
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    styles.navbar_link(
                        rx.text("About", size="4", weight="medium"),
                        href="#abstract",
                        on_click=rx.scroll_to("abstract"),
                    ),
                    styles.navbar_link(
                        rx.text("Cite", size="4", weight="medium"),
                        href="#cite",
                        on_click=rx.scroll_to("cite"),
                    ),
                    rx.color_mode.button(),
                    justify="end",
                    align_items="center",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(constants.TITLE, size="4", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item(
                            rx.link(
                                rx.text("About", size="4", weight="medium"),
                                href="/#",
                                on_click=rx.scroll_to("top"),
                            ),
                        ),
                        rx.menu.item(
                            rx.link(
                                rx.text("Cite", size="4", weight="medium"),
                                href="#cite",
                                on_click=rx.scroll_to("cite"),
                            ),
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        padding="1em",
        position="sticky",
        top="0px",
        z_index="5",
        width="100%",
        bg=rx.color_mode_cond(
            light="rgba(255, 255, 255, 0.8)",
            dark="rgba(0, 0, 0, 0.8)",
        ),
        backdrop_filter="blur(10px)",
        box_shadow=rx.cond(
            ScrollState.navbar_shadow,
            rx.color_mode_cond(
                light="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                dark="0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2)",
            ),
            "",
        ),
        on_scroll=ScrollState.show_navbar_shadow,
    )
