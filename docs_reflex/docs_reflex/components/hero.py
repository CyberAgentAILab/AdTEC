import reflex as rx

from .. import constants, styles


def join_authors(authors: list[dict]) -> rx.Component:
    return rx.hstack(
        *[
            rx.hstack(
                styles.link(
                    styles.meta_info(author["name"]),
                    href=author["url"],
                    is_external=True,
                ),
                rx.html(
                    f"<sup>{', '.join(constants.AFFILIATION_SYMBOLS_MAP[affiliation] for affiliation in author['affiliations'])}</sup>"
                ),
                styles.meta_info(
                    "," if i < len(constants.AUTHORS) - 1 else "",
                ),
                spacing="0",
            )
            for i, author in enumerate(constants.AUTHORS)
        ],
        spacing="1",
    )


def join_affiliations(affiliations: list[str]) -> rx.Component:
    return rx.hstack(
        *[
            rx.hstack(
                rx.html(f"<sup>{constants.AFFILIATION_SYMBOLS_MAP[affiliation]}</sup>"),
                styles.meta_info(affiliation),
                styles.meta_info(
                    "," if i < len(affiliations) - 1 else "",
                ),
                spacing="0",
            )
            for i, affiliation in enumerate(affiliations)
        ],
        spacing="1",
    )


def hero() -> rx.Component:
    return rx.container(
        styles.h1(
            constants.TITLE,
        ),
        rx.vstack(
            join_authors(constants.AUTHORS),
            join_affiliations(constants.UNIQUE_AFFILIATIONS),
            styles.meta_info(constants.CONFERENCE),
            spacing="0",
            align="center",
        ),
        rx.flex(
            *[
                styles.badge(
                    text=name,
                    icon=material["icon"],
                    href=material["url"],
                    is_external=material["is_external"],
                )
                for name, material in constants.MATERIALS.items()
                if name != "website"
            ],
            justify="center",
            align="center",
            spacing="2",
            padding_top="1em",
        ),
        spacing="1",
        padding_top="1em",
        id="hero",
    )
