from reactpy import component, html
from components import navbar_top_inv, navbarMenu_inv
from reactpy_router import link
import json
import requests


@component
def Page_CreateUser():
    titulo = "Crear Usuario"

    icono = "bi bi-person-up"

    def añadir(event):
        event.preventDefault()
        # Aquí puedes realizar acciones con los datos del formulario, si es necesario
        print("Formulario enviado")

    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu_inv.Navbar(),
            html.div(
                {"id": "content-wrapper", "class": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top_inv.NavbarBusqueda(titulo, icono),
                    html.div(
                        {"class": "container-fluid"},
                        html.div(
                            {
                                "class": "card shadow mb-4 justify-content-center align-items-center",
                                "style": "background-color: white; border-radius:10px; max-width: 600px; margin: auto; max-height:400px",
                            },
                            html.div(
                                {
                                    "class": "container-fluid",
                                    "style": "margin-top: 5%; margin-bottom: 5%; color: #E8E8E8;",
                                },
                                html.div(
                                    {"class": "row"},
                                    html.div(
                                        {"class": "col-auto me-auto"},
                                        html.h6(
                                            {
                                                "class": "display-6",
                                                "style": "color: black;",
                                            },
                                            html.b("Crear Usuario"),
                                        ),
                                    ),
                                ),
                            ),
                            html.hr(
                                {
                                    "class": "sidebar-divider my-0",
                                    "style": "background-color: black; margin-top: 2%;",
                                }
                            ),
                            html.div(
                                {"class": "card-body d-flex", "style": "height: 100vh;"},
                                html.div(
                                    {"class": "container-fluid "},
                                    html.div(
                                        {"class": "row no-border-bottom"},
                                        html.div(
                                            {"class": "col-auto"},
                                            html.form(
                                            {"on_submit": añadir},
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "nombre"}, "Nombre(s): "),
                                                    html.input({"type": "text", "id": "nombre", "name": "nombre", "class": "form-control"}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "correo"}, "Correo: "),
                                                    html.input({"type": "text", "id": "correo", "name": "correo", "class": "form-control"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                
                                                 html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "contraseña"}, "Contraseña: "),
                                                    html.input({"type": "text", "id": "contraseña", "name": "contraseña", "class": "form-control"}),
                                                ),
                                                 html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "url"}, "URL BD: "),
                                                    html.input({"type": "text", "id": "url", "name": "url", "class": "form-control"}),
                                                )
                                            ),
                                            html.div(
                                                {"class": "row"},
                                                html.div(
                                                    {"class": "col text-center"},
                                                    html.button({"type": "submit", "class": "btn btn-primary"}, "Crear Usuario"),
                                                ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )