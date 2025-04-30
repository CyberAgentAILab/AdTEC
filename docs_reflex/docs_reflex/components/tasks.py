import reflex as rx

from .. import styles


class ExampleState(rx.State):
    tasks: list[dict] = [
        {
            "name": "ad-acceptability",
            "description": "The goal is to predict the overall quality of an ad text with binary labels: `acceptable` / `unacceptable`.",
            "background": "As most ad delivery platforms impose text length restrictions, minor grammatical errors are tolerated to enhance the readability and engage customers within limited space. However, excessive compression can mislead customers, and such poor-quality ads should be detected before delivery to avoid negative impacts on the advertiser.",
            "image_src": "/example-ad-acceptability.png",
        },
        {
            "name": "ad-consistency",
            "description": "The goal is to predict the consistency between LP content and ad text with binary labels: `consistent` / `inconsistent`.",
            "background": "Verifying consistency between the ad text and LP content is crucial. If a feature or price mentioned in the ad text is not referenced in the corresponding LP, it may violate the Law for the Prevention of Unjustified Extra or Unexpected Benefit and Misleading Representation, resulting in damages to the advertiser.",
            "image_src": "/example-ad-consistency.png",
        },
        {
            "name": "ad-performance-estimation",
            "description": "The goal is to predict the quality score (QS) from ad texts, keywords, and industry in the range of 0 to 100.",
            "background": "The most straightforward way to measure ad quality is to publish them online and let end customers evaluate them. However, delivering all ads without alterations is impractical, as low-quality ads can negatively impact advertisers. Therefore, prior studies investigated offline methods to measure ad text quality by simulating customer behavior, such as click-through rate (CTR), based on past delivery history.",
            "image_src": "/example-ad-performance-estimation.png",
        },
        {
            "name": "a3-recognition",
            "description": "The goal is to predict all labels of aspects of advertising appeals (A3) from ad texts.",
            "background": "One of the most crucial factors in advertising is the aspect of advertising appeals (A3). At its core, advertising aims to connect advertisers with readers, and A3 serves as a bridge between them. For example, an ad emphasizing low cost may resonate with price-conscious readers, while one focusing on high performance may not. Thus, recognizing appealing expressions in advertising and using appropriate A3 can enhance downstream tasks, such as CTR prediction.",
            "image_src": "/example-a3-recognition.png",
        },
        {
            "name": "ad-similarity",
            "description": "The goal is to predict the similarity between two ad texts in the range of 1 to 5.",
            "background": "Repeatedly showing same ads to readers leads to ad fatigue [15], where readers become bored and ad performance declines. Therefore, it is essential to avoid displaying the same ads for extended periods, and regularly replace them with different ones. However, the transition from old to new ads must be carefully managed because we need to maintain the product and its appeal while updating the wording or representations, or we risk disengaging customers who were attracted to the previous ads. Thus, measuring the similarity particularly focusing on this situation is crucial, which enables us to determine whether to replace the ad based on a quantified score.",
            "image_src": "/example-ad-similarity.png",
        },
    ]


def tasks() -> rx.Component:
    return rx.vstack(
        styles.h2("Task Details"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Ad Acceptability", value="ad-acceptability"),
                rx.tabs.trigger("Ad Consistency", value="ad-consistency"),
                rx.tabs.trigger(
                    "Ad Performance Estimation", value="ad-performance-estimation"
                ),
                rx.tabs.trigger("A3 Recognition", value="a3-recognition"),
                rx.tabs.trigger("Ad Similarity", value="ad-similarity"),
                size="2",
                style={
                    "font_size": "1em",
                    "justify_content": "center",
                    "margin_bottom": "1em",
                },
            ),
            rx.foreach(
                ExampleState.tasks,
                lambda task: rx.tabs.content(
                    rx.vstack(
                        rx.flex(
                            rx.vstack(
                                styles.h3("Task Description"),
                                rx.markdown(
                                    task["description"],
                                    component_map={
                                        "p": lambda text: rx.text(
                                            text,
                                            margin_top="0",
                                            margin_bottom="1em",
                                        )
                                    },
                                ),
                                styles.h3("Background"),
                                rx.markdown(
                                    task["background"],
                                    component_map={
                                        "p": lambda text: rx.text(
                                            text,
                                            margin_top="0",
                                            margin_bottom="1em",
                                        )
                                    },
                                ),
                                spacing="0",
                            ),
                            styles.image(
                                src=task["image_src"],
                                zoom=False,
                                width="300px",
                            ),
                            direction="row",
                            justify="between",
                            align="center",
                            margin_left="10%",
                            margin_right="10%",
                        )
                    ),
                    value=task["name"],
                ),
            ),
            default_value="ad-acceptability",
        ),
        id="tasks",
        justify="center",
        align="center",
        width="90%",
    )
