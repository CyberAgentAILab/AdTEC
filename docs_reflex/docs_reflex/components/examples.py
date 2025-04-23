import pandas as pd
import reflex as rx

from .. import styles

df_ad_acceptability = pd.read_csv(
    "https://raw.githubusercontent.com/CyberAgentAILab/AdTEC/refs/heads/main/data/sample/ad-acceptability.train.tsv",
    sep="\t",
)

df_ad_consistency = pd.read_csv(
    "https://raw.githubusercontent.com/CyberAgentAILab/AdTEC/refs/heads/main/data/sample/ad-consistency.train.tsv",
    sep="\t",
)

df_ad_performance_estimation = pd.read_csv(
    "https://raw.githubusercontent.com/CyberAgentAILab/AdTEC/refs/heads/main/data/sample/ad-performance-estimation.train.tsv",
    sep="\t",
)

df_a3_recognition = pd.read_csv(
    "https://raw.githubusercontent.com/CyberAgentAILab/AdTEC/refs/heads/main/data/sample/a3-recognition.train.tsv",
    sep="\t",
)

df_similarity = pd.read_csv(
    "https://raw.githubusercontent.com/CyberAgentAILab/AdTEC/refs/heads/main/data/sample/ad-similarity.train.tsv",
    sep="\t",
)


def examples() -> rx.Component:
    return rx.container(
        styles.h2("Examples"),
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
            rx.tabs.content(
                rx.data_table(
                    data=df_ad_acceptability,
                    pagination=True,
                    search=False,
                    sort=True,
                ),
                value="ad-acceptability",
            ),
            rx.tabs.content(
                rx.data_table(
                    data=df_ad_consistency,
                    pagination=True,
                    search=False,
                    sort=True,
                ),
                value="ad-consistency",
            ),
            rx.tabs.content(
                rx.data_table(
                    data=df_ad_performance_estimation,
                    pagination=True,
                    search=False,
                    sort=True,
                ),
                value="ad-performance-estimation",
            ),
            rx.tabs.content(
                rx.data_table(
                    data=df_a3_recognition,
                    pagination=True,
                    search=False,
                    sort=True,
                ),
                value="a3-recognition",
            ),
            rx.tabs.content(
                rx.data_table(
                    data=df_similarity,
                    pagination=True,
                    search=False,
                    sort=True,
                ),
                value="ad-similarity",
            ),
            default_value="ad-acceptability",
        ),
        id="examples",
    )
