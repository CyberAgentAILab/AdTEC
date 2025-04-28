import reflex as rx

from .. import styles


def discussion() -> rx.Component:
    return rx.container(
        styles.h2("Discussion"),
        rx.accordion.root(
            rx.accordion.item(
                header="Fine-tuning encoder PLMs still perform well in AdTEC",
                value="discussion_1",
                content=styles.markdown(
                    "Achieved the highest score in three out of five tasks"
                ),
            ),
            rx.accordion.item(
                header="Humans surpassed PLMs in Ad Acceptability and Consistency tasks",
                value="discussion_2",
                content=styles.markdown(
                    "In the Ad Acceptability task, models miss semantic issues such as redundancy or contradiction. In the Ad Consistency task, models struggled when LPs omit meta expressions like “official”"
                ),
            ),
            rx.accordion.item(
                header="GPT-4 and fine-tuned models beat human performance in Ad Similarity",
                value="discussion_3",
                content=styles.markdown(
                    "PLMs can better understand nuanced relationships between ad content"
                ),
            ),
            width="100%",
            radius="small",
            collapsible=True,
            type="multiple",
            variant="outline",
            color_scheme="gray",
        ),
        width="100%",
        height="100%",
        align="center",
    )
