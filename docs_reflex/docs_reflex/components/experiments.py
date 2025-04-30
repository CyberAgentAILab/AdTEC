import reflex as rx

from .. import styles


class ExperimentState(rx.State):
    column_headers: list[tuple[str, str]] = [
        ("Ad Acceptability", "Accuracy/F1 Score"),
        ("Ad Consistency", "Accuracy/F1 Score"),
        ("Ad Perf. Est.", "Pearson/Spearman Corr."),
        ("A3 Recognition", "F1-micro/-macro"),
        ("Ad Similarity", "Pearson/Spearman Corr."),
    ]

    experiments: list[dict] = [
        {
            "evaluator": "TohokuBERT-Base",
            "ad_acceptability": "0.685/0.691",
            "ad_consistency": "0.757/0.504",
            "ad_performance_estimation": "0.437/0.454",
            "a3_recognition": "0.753/0.629",
            "ad_similarity": "0.769/0.803",
        },
        {
            "evaluator": "TohokuBERT-Large",
            "ad_acceptability": "0.711/0.688",
            "ad_consistency": "**0.767/0.552**",
            "ad_performance_estimation": "**0.480/0.497**",
            "a3_recognition": "0.774/**0.694**",
            "ad_similarity": "0.773/0.807",
        },
        {
            "evaluator": "WasedaBERT-Base",
            "ad_acceptability": "0.615/0.639",
            "ad_consistency": "0.725/0.388",
            "ad_performance_estimation": "0.444/0.454",
            "a3_recognition": "0.641/0.442",
            "ad_similarity": "0.749/0.797",
        },
        {
            "evaluator": "WasedaBERT-Large",
            "ad_acceptability": "0.598/0.637",
            "ad_consistency": "0.755/0.474",
            "ad_performance_estimation": "0.445/0.457",
            "a3_recognition": "0.663/0.517",
            "ad_similarity": "0.740/0.800",
        },
        {
            "evaluator": "XLM-RoBERTa-Base",
            "ad_acceptability": "0.694/0.677",
            "ad_consistency": "0.743/0.465",
            "ad_performance_estimation": "0.425/0.439",
            "a3_recognition": "0.730/0.542",
            "ad_similarity": "0.846/0.870",
        },
        {
            "evaluator": "XLM-RoBERTa-Large",
            "ad_acceptability": "0.705/0.690",
            "ad_consistency": "0.758/0.519",
            "ad_performance_estimation": "0.453/0.457",
            "a3_recognition": "0.778/**0.677**",
            "ad_similarity": "**0.878/0.878**",
        },
        {
            "evaluator": "CALM2-7B",
            "ad_acceptability": "0.520/0.115",
            "ad_consistency": "0.381/0.472",
            "ad_performance_estimation": "0.006/0.013",
            "a3_recognition": "0.154/0.042",
            "ad_similarity": "0.036/0.036",
        },
        {
            "evaluator": "ELYZA-7B",
            "ad_acceptability": "0.352/0.520",
            "ad_consistency": "0.628/0.771",
            "ad_performance_estimation": "0.003/0.046",
            "a3_recognition": "0.196/0.044",
            "ad_similarity": "0.015/-0.004",
        },
        {
            "evaluator": "GPT-3.5",
            "ad_acceptability": "0.369/0.489",
            "ad_consistency": "0.528/0.570",
            "ad_performance_estimation": "-0.013/-0.022",
            "a3_recognition": "0.255/0.064",
            "ad_similarity": "0.389/0.385",
        },
        {
            "evaluator": "GPT-4",
            "ad_acceptability": "0.325/0.433",
            "ad_consistency": "0.583/0.612",
            "ad_performance_estimation": "0.028/0.073",
            "a3_recognition": "0.417/0.113",
            "ad_similarity": "0.776/0.811",
        },
        {
            "evaluator": "ELYZA-7B (Fine-tuned)",
            "ad_acceptability": "0.638/0.638",
            "ad_consistency": "0.692/0.694",
            "ad_performance_estimation": "0.240/0.235",
            "a3_recognition": "0.379/0.280",
            "ad_similarity": "0.684/0.740",
        },
        {
            "evaluator": "Human",
            "ad_acceptability": "**0.732/0.790**",
            "ad_consistency": "0.703/**0.807**",
            "ad_performance_estimation": "—",
            "a3_recognition": "0.564/0.538",
            "ad_similarity": "0.699/0.765",
        },
    ]


def experiment_header(main_text: str, sub_text: str) -> rx.Component:
    return rx.vstack(
        rx.text(main_text, justify="center", align="center"),
        rx.text(
            sub_text,
            weight="light",
            font_size="0.8em",
            justify="center",
            align="center",
        ),
        justify="center",
        align="center",
        spacing="0",
    )


def experiments() -> rx.Component:
    return rx.vstack(
        styles.h2("Experiments"),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell(
                        rx.text("Evaluator", justify="center", align="center"),
                        justify="center",
                        align="center",
                    ),
                    rx.foreach(
                        ExperimentState.column_headers,
                        lambda column: rx.table.column_header_cell(
                            experiment_header(column[0], column[1]),
                            justify="center",
                        ),
                    ),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    ExperimentState.experiments,
                    lambda experiment: rx.table.row(
                        rx.table.cell(rx.text.strong(experiment["evaluator"])),
                        rx.table.cell(experiment["ad_acceptability"], justify="center"),
                        rx.table.cell(experiment["ad_consistency"], justify="center"),
                        rx.table.cell(
                            experiment["ad_performance_estimation"], justify="center"
                        ),
                        rx.table.cell(experiment["a3_recognition"], justify="center"),
                        rx.table.cell(experiment["ad_similarity"], justify="center"),
                        align="center",
                    ),
                ),
            ),
            variant="surface",
        ),
        id="experiments",
        justify="center",
        align="center",
        width="90%",
    )
