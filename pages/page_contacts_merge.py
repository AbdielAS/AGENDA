from reactpy import component, html
from components import navbar_top, navbarMenu, tabla
from reactpy_router import link
import json
import requests


@component
def Page_ContactsMerge():
    token,setToken = reactpy.hooks.use_state("Ignore")
    titulo = "Contactos Combinados"

    icono = "bi bi-newspaper"

    headers = [
        "Nombre(s)",
        "Correo",
        "Teléfono",
        "Calle",
        "Ciudad",
        "Código Postal",
        "No. Ext",
        "No. Int",
        "Colonia",
    ]

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
        html.div(
            {"id": "wrapper"},
            html.input({"style":"display:none","id": "divToken","onkeypress":lambda event:setToken(str(event['currentTarget']['value']))}),
            getToken(),
            validarSesion(token),
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
                                            html.b("Contactos Combinados"),
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
                                            tabla.Tabla(headers, content),
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
