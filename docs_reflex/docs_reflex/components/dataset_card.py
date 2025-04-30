import reflex as rx

from .. import styles


class DatasetTableState(rx.State):
    dataset: list[dict] = [
        {
            "name": "Ad Acceptability",
            "task_setup": "Classification",
            "input": "Ad text",
            "labels": "Acceptable/Unacceptable",
            "metrics": "Accuracy/F1 Score",
            "train_size": 13265,
            "dev_size": 970,
            "test_size": 980,
        },
        {
            "name": "Ad Consistency",
            "task_setup": "Classification",
            "input": "Ad text, LP text",
            "labels": "Consistent/Inconsistent",
            "metrics": "Accuracy/F1 Score",
            "train_size": 10639,
            "dev_size": 945,
            "test_size": 970,
        },
        {
            "name": "Ad Performance Estimation",
            "task_setup": "Regression",
            "input": "Ad texts, Keywords, Industry",
            "labels": "Quality Score ([0, 100])",
            "metrics": "Pearson/Spearman Correlation",
            "train_size": 125087,
            "dev_size": 965,
            "test_size": 965,
        },
        {
            "name": "Ad Aspect Recognition",
            "task_setup": "Multi-label Classification",
            "input": "Ad text",
            "labels": "Aspects (e.g., Brand, Price, Quality)",
            "metrics": "F1-micro/-macro Score",
            "train_size": 1856,
            "dev_size": 465,
            "test_size": 410,
        },
        {
            "name": "Ad Similarity",
            "task_setup": "Regression",
            "input": "Ad text pair",
            "labels": "Similarity Score ([0, 1])",
            "metrics": "Pearson/Spearman Correlation",
            "train_size": 4980,
            "dev_size": 623,
            "test_size": 629,
        },
    ]


def dataset_card() -> rx.Component:
    return rx.vstack(
        styles.h2("Dataset Card"),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Task Name", justify="center"),
                    rx.table.column_header_cell("Task Setup", justify="center"),
                    rx.table.column_header_cell("Input", justify="center"),
                    rx.table.column_header_cell("Labels", justify="center"),
                    rx.table.column_header_cell("Metrics", justify="center"),
                    rx.table.column_header_cell("#Train", justify="center"),
                    rx.table.column_header_cell("#Dev", justify="center"),
                    rx.table.column_header_cell("#Test", justify="center"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    DatasetTableState.dataset,
                    lambda dataset: rx.table.row(
                        rx.table.cell(rx.text.strong(dataset["name"])),
                        rx.table.cell(dataset["task_setup"]),
                        rx.table.cell(dataset["input"]),
                        rx.table.cell(dataset["labels"]),
                        rx.table.cell(dataset["metrics"]),
                        rx.table.cell(dataset["train_size"], justify="center"),
                        rx.table.cell(dataset["dev_size"], justify="center"),
                        rx.table.cell(dataset["test_size"], justify="center"),
                        align="center",
                    ),
                ),
            ),
            variant="surface",
        ),
        id="dataset-card",
        justify="center",
        align="center",
        width="90%",
    )
