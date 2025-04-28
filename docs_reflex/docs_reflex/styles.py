import reflex as rx
from reflex_image_zoom import image_zoom


def h1(text: str, **kwargs) -> rx.Component:
    return rx.heading(
        text,
        as_="h1",
        size="9",
        weight="bold",
        align="center",
        padding_bottom="0.4em",
        **kwargs,
    )


def meta_info(text: str, **kwargs) -> rx.Component:
    return rx.text(text, size="5", **kwargs)


def h2(text: str, **kwargs) -> rx.Component:
    return rx.heading(
        text,
        as_="h2",
        size="7",
        weight="bold",
        align="center",
        padding_top="1em",
        padding_bottom="0.4em",
        **kwargs,
    )


def h3(text: str, **kwargs) -> rx.Component:
    return rx.heading(text, size="5", weight="bold", **kwargs)


def badge(text: str, icon: str, href: str, **kwargs) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon, size=15),
            text,
            variant="solid",
            radius="full",
        ),
        href=href,
        _hover={
            "text_decoration": "none",
            "transition": "all 0.15s ease-in-out",
            "cursor": "pointer",
        },
        **kwargs,
    )


def body(text: str, **kwargs) -> rx.Component:
    return rx.text(text, size="4", **kwargs)


def image(src: str, caption: str = None, zoom: bool = False, **kwargs) -> rx.Component:
    image_component = (
        image_zoom(rx.image(src, align="center", **kwargs))
        if zoom
        else rx.image(src, align="center", **kwargs)
    )
    return rx.vstack(
        image_component,
        rx.text(caption, size="4", align="center", text_align="justify", **kwargs),
        width="100%",
        height="100%",
        align="center",
        justify="center",
    )


def code(text: str, **kwargs) -> rx.Component:
    return rx.code(text, **kwargs)


def code_block(text: str, language: str = "python", **kwargs) -> rx.Component:
    return rx.code_block(
        text,
        language=language,
        wrap_long_lines=True,
        can_copy=True,
        copy_button=rx.button(
            rx.icon("copy", size=15),
            variant="solid",
            color=rx.color_mode_cond(
                light=rx.color("black"),
                dark=rx.color("white"),
            ),
            style={
                "position": "absolute",
                "top": "0.5em",
                "right": "0.5em",
                "padding": "0.5em",
                "background": "transparent",
            },
            on_click=rx.set_clipboard(text),
            transition="opacity 0.3s ease-in-out",
        ),
        custom_style={"font_size": "0.8em", "max_width": "90vw", "overflow_x": "auto"},
        margin_top="0",
        margin_bottom="0",
        **kwargs,
    )


def link(component: rx.Component, **kwargs) -> rx.Component:
    return rx.link(
        component,
        color=rx.color_mode_cond(
            light=rx.color("accent", 8),
        ),
        _hover={
            "text_decoration": "underline",
            "cursor": "pointer",
            "transition": "all 0.15s ease-in-out",
        },
        **kwargs,
    )


def navbar_link(component: rx.Component, href: str, **kwargs) -> rx.Component:
    return rx.link(
        component,
        href=href,
        color=rx.color_mode_cond(
            light=rx.color("black"),
            dark=rx.color("white"),
        ),
        _hover={
            "text_decoration": "none",
        },
        **kwargs,
    )


component_map = {
    "h1": h1,
    "h2": h2,
    "h3": h3,
    "p": body,
    "code": code,
    "codeblock": code_block,
    "a": link,
}


def markdown(text: str, component_map: dict = component_map, **kwargs) -> rx.Component:
    return rx.markdown(text, component_map=component_map, **kwargs)


def accordion(items: list[rx.Component], **root_props) -> rx.Component:
    return rx.accordion.root(
        *items,
        **root_props,
    )


def accent_color(color_scheme: str = "accent", **kwargs) -> rx.Component:
    if color_scheme == "accent":
        return rx.color_mode_cond(
            light=rx.color("accent", 8),
            dark=rx.color("accent", 9),
        )
    elif color_scheme == "mono":
        return rx.color_mode_cond(
            light=rx.color("black"),
            dark=rx.color("white"),
        )
    else:
        raise ValueError(f"Invalid color scheme: {color_scheme}")
