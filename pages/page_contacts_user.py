from reactpy import component, html, hooks
from components import navbar_top, navbarMenu, tabla
from reactpy_router import link
import json
import requests

def generate_arr_data(data):
    list_data=[]
    for list_contacts in data:
        contacts =[]
        contacts.append(list_contacts["id"])
        contacts.append(list_contacts["nombre"])
        contacts.append(list_contacts["telefono"])
        contacts.append(list_contacts["correo"])
        contacts.append(list_contacts["direccion"]["calle"])
        contacts.append(list_contacts["direccion"]["cuidad"])
        contacts.append(list_contacts["direccion"]["codigo_postal"])
        contacts.append(list_contacts["direccion"]["num_exterior"])
        contacts.append(list_contacts["direccion"]["numero_interior"])
        contacts.append(list_contacts["direccion"]["colonia"])
        list_data.append(contacts)
    return list_data



@component
def Page_ContactsUser():
    titulo = "Contactos"

    tabla_contactos, set_tabla_contactos = hooks.use_state([])

    icono = "bi bi-person-square"

    url = "https://api-agenda-8dij.onrender.com/"

    token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JyZW8iOiJwZWRyb2FiZGllbDI3QGdtYWlsLmNvbSIsImNvbnRyYXNlXHUwMGYxYSI6InBhYXMyNyIsImV4cCI6MTcwMjc5Njk1MH0.fr2vd74irg2q7WAi-2feroyh2_9Mgn7k3fKvUaPodMo"

    def Datos_Contatos():
        email="ernest@gmail.com"

        headers = {"Authorization": f"Bearer {token}"}
        response =  requests.get(f"{url}contacts_user/{email}", headers=headers)
        response.raise_for_status()
        datos = response.json()
        set_tabla_contactos(datos)


    hooks.use_effect(Datos_Contatos, [])

    headers = [
        "ID",
        "Nombre(s)",
        "Correo",
        "Teléfono",
        "Calle",
        "Ciudad",
        "Código Postal",
        "No. Ext",
        "No. Int",
        "Colonia",
        ""
    ]

    arreglo_contactos = generate_arr_data(tabla_contactos)

    content=[
        "nombre",
        "correo",
        "telefono",
        "nombre",
        "direccion.calle",
        "direccion.ciudad",
        "direccion.codigo_postal",
        "direccion.num_ext",
        "direccion.numero_interior",
        "colonia"
    ]


  

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
                                "class": "card shadow mb-4",
                                "style": "background-color: white; border-radius:10px;",
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
                                            html.b("Contactos de:"),
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
                                {"class": "card-body", "style": "height: 100vh;"},
                                html.hr({"class": "sidebar-divider my-0"}),
                                html.div(
                                    {"class": "container-fluid "},
                                    html.div(
                                        {"class": "row no-border-bottom"},
                                        html.div(
                                            {"style": {"display": "inline-flex"}},
                                            html.button(
                                                {
                                                    "class": "btn btn-primary",
                                                    "type": "button",
                                                    "data-bs-toggle": "collapse",
                                                    "data-bs-target": "#collapseExample",
                                                    "aria-expanded": "false",
                                                    "aria-controls": "collapseExample",
                                                },
                                                "Hacer Merge",
                                            ),
                                            html.span(
                                                {"style": {"width": "1rem"}}
                                            ),  # Espacio adicional
                                            html.div(
                                                {
                                                    "class": "collapse",
                                                    "id": "collapseExample",
                                                },
                                                html.div(
                                                    {
                                                        "class": "card card-body",
                                                        "style": {
                                                            "display": "flex",
                                                            "flexDirection": "column",
                                                        },
                                                    },
                                                    html.button(
                                                        {
                                                            "type": "submit",
                                                            "class": "btn btn-primary",
                                                            "style": {
                                                                "marginBottom": "1rem"
                                                            },
                                                        },
                                                        "Conservar Todos Los Contactos",
                                                    ),
                                                    html.button(
                                                        {
                                                            "type": "submit",
                                                            "class": "btn btn-primary",
                                                        },
                                                        "Conservar Los Contactos Más Actuales",
                                                    ),
                                                ),
                                            ),
                                        ),
                                       html.div(
                                            {"style": {"overflow-y": "auto", "overflow-x": "auto", "max-height": "1000px"}},
                                            tabla.Tabla(headers, arreglo_contactos),
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
