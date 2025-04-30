import reflex as rx

from .. import styles

GOOGLE_SHEET_ID = "2PACX-1vSBbtDyu-ocJ1N4N44xrl6UMxyCjGXDGsCL8jib1jbBQZtJl9SR-FCuNxgzk-SAaMj8XI1TdiqlLpkY"
GOOGLE_SHEET_EMBED_PARAMS = "?gid=0&amp;single=true&amp;widget=true&amp;headers=false&amp;printtitle=false&amp;sheetnames=false"


def examples() -> rx.Component:
    return rx.vstack(
        styles.h2("Examples"),
        rx.el.Iframe(
            src=f"https://docs.google.com/spreadsheets/d/e/{GOOGLE_SHEET_ID}/pubhtml?{GOOGLE_SHEET_EMBED_PARAMS}",
            width="100%",
            height="500px",
        ),
        id="examples",
        justify="center",
        align="center",
        width="90%",
    )
