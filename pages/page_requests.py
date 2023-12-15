from reactpy import component, html, hooks
from components import navbar_top, navbarMenu, tabla
from reactpy_router import link
import json
import requests


def generate_arr_data(data):
    list_data=[]
    for list_requests in data:
        requests =[]
        requests.append(list_requests["id"])
        requests.append(list_requests["user_solicita"])
        requests.append(list_requests["lectura/escritura"])
        requests.append(list_requests["merge"])
        #requests.append(html.button({"class": "btn btn-primary"}, "Editar" ))
        #requests.append(html.button({"class": "btn btn-danger"}, "Eliminar" ))
        list_data.append(requests)
    return list_data

@component
def Page_Solicitudes():
    token,setToken = reactpy.hooks.use_state("Ignore")
    titulo = "Solicitudes"

    tabla_solicitudes, set_tabla_solicitudes = hooks.use_state([])

    icono = "bi bi-envelope"

    url = "https://api-agenda-8dij.onrender.com/"

    token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JyZW8iOiJwZWRyb2FiZGllbDI3QGdtYWlsLmNvbSIsImNvbnRyYXNlXHUwMGYxYSI6InBhYXMyNyIsImV4cCI6MTcwMjc5Njk1MH0.fr2vd74irg2q7WAi-2feroyh2_9Mgn7k3fKvUaPodMo"

    def Datos_Solicitudes():
        headers = {"Authorization": f"Bearer {token}"}
        response =  requests.get(url + "all_merge", headers=headers)
        response.raise_for_status()
        datos = response.json()
        set_tabla_solicitudes(datos)


    hooks.use_effect(Datos_Solicitudes, [])

    headers = [
        "ID",
        "Usuario",
        "Lectura/Escritura",
        "Merge"
        "Estatus",
    ]

    arreglo_solicitudes = generate_arr_data(tabla_solicitudes)

    data =[
        "Pedro Abdiel",
        "Alcántara Soto"
        "pedroabdiel27@gmail.com"
        "7221779302"
    ]
    def getToken():
        #return html.script("var elemento = document.getElementById('divToken');elemento.value = 'asdasdasd';console.log('token recibido en home:    '+localStorage.getItem('token'));")
        return html.script("var elemento = document.getElementById('divToken'); var item = localStorage.getItem('token'); if (item == null) { item = \"None\"; } elemento.value = item; elemento.dispatchEvent(new Event('keypress'));")

    def validarSesion(tkn):
        script =  ("localStorage.clear();window.location.href = \"/\";" if (tkn == "None") else "localStorage.clear();localStorage.setItem(\"token\", \""+tkn+"\");") if tkn != "Ignore" else ""  
        return html.script(script)
    
    return html.div(
        {"id": "app"},
        html.input({"style":"display:none","id": "divToken","onkeypress":lambda event:setToken(str(event['currentTarget']['value']))}),
        getToken(),
        validarSesion(token),
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
                                            html.b("Solicitudes"),
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
                                            tabla.Tabla(headers, arreglo_solicitudes),
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
