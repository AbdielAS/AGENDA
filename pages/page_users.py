from reactpy import component, html, hooks
from components import navbar_top, navbarMenu, tabla
from reactpy_router import link
import json
import requests

def generate_arr_data(data):
    list_data=[]
    for list_users in data:
        users =[]
        users.append(list_users["id"])
        users.append(list_users["nombre"])
        users.append(list_users["correo"])
        users.append(list_users["url"])
        users.append(html.button({"class": "btn btn-primary"}, "Solicitar Lectura" ))
        users.append(html.button({"class": "btn btn-primary"}, "Solicitar Merge" ))
        users.append(html.button({"class": "btn btn-primary"}, "Solicitar todos los permisos" ))
        
        list_data.append(users)
    return list_data


@component
def Page_Users():
    titulo = "Usuarios"

    tabla_usuarios, set_tabla_usuarios = hooks.use_state([])

    icono = "bi bi-people"

    url = "https://api-agenda-8dij.onrender.com/"

    token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JyZW8iOiJwZWRyb2FiZGllbDI3QGdtYWlsLmNvbSIsImNvbnRyYXNlXHUwMGYxYSI6InBhYXMyNyIsImV4cCI6MTcwMjc5Njk1MH0.fr2vd74irg2q7WAi-2feroyh2_9Mgn7k3fKvUaPodMo"

    def Datos_Usuarios():
        headers = {"Authorization": f"Bearer {token}"}
        response =  requests.get(url + "all_users", headers=headers)
        response.raise_for_status()
        datos = response.json()
        set_tabla_usuarios(datos)


    hooks.use_effect(Datos_Usuarios, [])

    headers = [
        "ID",
        "Nombre(s)",
        "Correo",
        "URL"
        "",
        "",
        ""
    ]

    arreglo_usuarios = generate_arr_data(tabla_usuarios)

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
                                            html.b("Usuarios"),
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
                                            {"style": {"overflow-y": "auto", "overflow-x": "auto", "max-height": "1000px"}},
                                            tabla.Tabla(headers, arreglo_usuarios),
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
