import reflex as rx


def adtec() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.vstack(
                rx.text(
                    rx.text(
                        rx.text.em("AdTEC"),
                        size="8",
                        font_weight="bold",
                        as_="span",
                    ),
                ),
                rx.text(
                    rx.text(
                        "The first public dataset",
                        as_="span",
                        _hover={
                            "transition": "all 0.2s ease-in-out",
                            "color": rx.color_mode_cond(
                                light=rx.color("accent", 8),
                                dark=rx.color("accent", 9),
                            ),
                            "font_style": "italic",
                        },
                    ),
                    " designed for ",
                    rx.text(
                        "evaluating the quality of ad texts",
                        as_="span",
                        _hover={
                            "transition": "all 0.2s ease-in-out",
                            "color": rx.color_mode_cond(
                                light=rx.color("accent", 8),
                                dark=rx.color("accent", 9),
                            ),
                            "font_style": "italic",
                        },
                    ),
                    " based on ",
                    rx.text(
                        "real-world AdOps workflows",
                        as_="span",
                        _hover={
                            "transition": "all 0.2s ease-in-out",
                            "color": rx.color_mode_cond(
                                light=rx.color("accent", 8),
                                dark=rx.color("accent", 9),
                            ),
                            "font_style": "italic",
                        },
                    ),
                    ".",
                    size="8",
                ),
                align="center",
            ),
            align="center",
        ),
        width="100%",
        height="100%",
        align="center",
    )
