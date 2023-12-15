from reactpy import component, html
from reactpy_router import link


@component
def NavbarBusqueda(titulo, icono):
    return html.div(
        html.nav(
            {
                "class": "navbar navbar-expand navbar-light bg-white topbar d-flex mb-3 static-top shadow"
            },
            html.a(
                {
                    "href": "#",
                    "class": "btn",
                    "role": "button",
                    "type": "button",
                    "data-bs-toggle": "button",
                    "style": {"color": "black", "marginRight": "50%"},
                },
                html.i({"className": icono, "style": {"fontSize": "20px", "marginRight": "8px"}}),
                html.b(titulo),
            ),
        )
    )
