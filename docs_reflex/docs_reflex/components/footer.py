import reflex as rx

from .. import constants


def footer() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text(
                f"Copyright © 2025 {constants.AUTHORS[0]['name']}. All rights reserved.",
                align="center",
            ),
            rx.text(
                "Commons Attribution-ShareAlike 4.0 International License.",
                align="center",
            ),
            height="200px",
            justify="center",
            align="center",
            margin_top="auto",
            margin_bottom="auto",
            spacing="0",
        ),
    )
