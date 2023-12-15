from reactpy import component, html
from components import navbar_top, navbarMenu
from reactpy_router import link
import json
import requests


@component
def Page_AddContacts():
    titulo = "Añadir Contacto"

    icono = "bi bi-person-plus"

    def añadir(event):
        event.preventDefault()
        # Aquí puedes realizar acciones con los datos del formulario, si es necesario
        print("Formulario enviado")

    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu.Navbar(),
            html.div(
                {"id": "content-wrapper", "class": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top.NavbarBusqueda(titulo, icono),
                    html.div(
                        {"class": "container-fluid"},
                        html.div(
                            {
                                "class": "card shadow mb-4 justify-content-center align-items-center",
                                "style": "background-color: white; border-radius:10px;max-width: 600px; margin: auto; max-height:650px",
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
                                            html.b("Añadir Contacto"),
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
                                html.hr({"class": "sidebar-divider my-0"}),
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
                                                    html.label({"for": "apellidos"}, "Apellidos: "),
                                                    html.input({"type": "text", "id": "apellidos", "name": "apellidos", "class": "form-control"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "correo"}, "Correo: "),
                                                    html.input({"type": "text", "id": "correo", "name": "correo", "class": "form-control"}),
                                                ),
                                                 html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "telefono"}, "Teléfono: "),
                                                    html.input({"type": "text", "id": "telefono", "name": "telefono", "class": "form-control"}),
                                                ),
                                            ),
                                            
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "calle"}, "Calle: "),
                                                    html.input({"type": "text", "id": "calle", "name": "calle", "class": "form-control"}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ciudad"}, "Ciudad: "),
                                                    html.input({"type": "text", "id": "ciudad", "name": "ciudad", "class": "form-control"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "cp"}, "Código Postal: "),
                                                    html.input({"type": "text", "id": "cp", "name": "cp", "class": "form-control"}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ne"}, "Número Exterior: "),
                                                    html.input({"type": "text", "id": "ne", "name": "ne", "class": "form-control"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ni"}, "Número Interior: "),
                                                    html.input({"type": "text", "id": "ni", "name": "ni", "class": "form-control"}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "colonia"}, "Colonia: "),
                                                    html.input({"type": "text", "id": "colonia", "name": "colonia", "class": "form-control"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row"},
                                                html.div(
                                                    {"class": "col text-center"},
                                                    html.button({"type": "submit", "class": "btn btn-primary"}, "Añadir Contacto"),
                                                ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                # Tabla(columnas_ad, datos_api),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
