import reflex as rx

from .. import constants, styles


def abstract() -> rx.Component:
    """Abstract component."""

    return rx.container(
        rx.vstack(
            rx.accordion.root(
                rx.accordion.item(
                    header="What's Search Engine Ads?",
                    value="search_engine_ads",
                    content=styles.image(
                        src="/search-engine-ad.png",
                        caption="An example of a search engine ad.",
                        zoom=True,
                    ),
                ),
                rx.accordion.item(
                    header="What's AdOps?",
                    value="adops_workflow",
                    content=styles.image(
                        src="/adops-workflow.png",
                        caption="We define AdOps (Advertising Operations) as the process of managing and optimizing advertising campaigns to maximize their effectiveness and efficiency. We also generalized the workflow of AdOps into the image above based on the experts' interview: (1) The advertiser creates an LP to promote a product. (2) Based on the product information in the LP and target customers, text and graphics are designed by creators. (3) The creatives are evaluated based on fluency, attractiveness, regulations, legality, and other factors. (4) Once the creatives pass the quality evaluation, they are submitted to a delivery platform. (5) Customers respond to the displayed ads, such as page views, clicks, and purchases. (6) Based on the customer engagement, ad performance is reported back to the advertiser, and Steps 1-5 are repeated to improve the quality of the LP and ads.",
                        zoom=True,
                    ),
                ),
                rx.accordion.item(
                    header="Abstract",
                    value="abstract",
                    content=styles.markdown(
                        constants.ABSTRACT_MD,
                        text_align="justify",
                    ),
                ),
                width="100%",
                radius="small",
                collapsible=True,
                type="multiple",
                variant="outline",
                color_scheme="gray",
            ),
        ),
        width="100%",
        height="100%",
        align="center",
    )
