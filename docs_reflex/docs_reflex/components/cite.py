import reflex as rx

from .. import constants, styles


def cite() -> rx.Component:
    return rx.container(
        styles.h2("BibTeX"),
        styles.code_block(
            constants.BIBTEX,
            language="latex",
        ),
        id="cite",
    )
