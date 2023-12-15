from reactpy import component, html
from components import navbar_top_inv, navbarMenu_inv
from reactpy_router import link
import json
import requests


@component
def Page_CreateUser():
    token,setToken = reactpy.hooks.use_state("Ignore")
    titulo = "Crear Usuario"

    icono = "bi bi-person-up"

    def añadir(event):
        event.preventDefault()
        # Aquí puedes realizar acciones con los datos del formulario, si es necesario
        print("Formulario enviado")
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