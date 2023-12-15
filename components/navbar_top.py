from reactpy import component, html, hooks
from reactpy_router import link
import requests


@component
def NavbarBusqueda(titulo, icono):
    

    return html.nav(
        {
            "class": "navbar ps-4 pe-2 navbar-light bg-white topbar d-flex mb-3 static-top shadow container-fluid",
            "style": {"width": "100%"},
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
            html.i(
                {
                    "className": icono,
                    "style": {"fontSize": "20px", "marginRight": "8px"},
                }
            ),
            html.b(titulo),
        ),
    )

