from reactpy import component, html, hooks
from components import navbar_top, navbarMenu
from reactpy_router import link
import json
import requests


@component
def Page_AddContacts():
    url = "https://api-agenda-8dij.onrender.com/"

    token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JyZW8iOiJwZWRyb2FiZGllbDI3QGdtYWlsLmNvbSIsImNvbnRyYXNlXHUwMGYxYSI6InBhYXMyNyIsImV4cCI6MTcwMjc5Njk1MH0.fr2vd74irg2q7WAi-2feroyh2_9Mgn7k3fKvUaPodMo"

    def getToken():
        return html.script("var elemento = document.getElementById('token'); var item = localStorage.getItem('token'); if (item == null) { item = \"None\"; } elemento.value = item; elemento.dispatchEvent(new Event('keypress'));")
    
    nombre, setNombre = hooks.use_state("")
    correo, setCorreo = hooks.use_state("")
    telefono, setTelefono = hooks.use_state(0)
    calle, setCalle = hooks.use_state("")
    ciudad, setCiudad = hooks.use_state("")
    cp, setCp = hooks.use_state(0)
    numExt, setNumExt = hooks.use_state(0)
    numInt, setNumInt = hooks.use_state(0)
    colonia, setColonia = hooks.use_state("")


    titulo = "Añadir Contacto"
    icono = "bi bi-person-plus"
    def btn_submit(e, nombre, correo, telefono, calle, ciudad, cp, numExt, numInt,colonia):
        info = {
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
            "direccion": {
                "calle": calle,
                "cuidad": ciudad,
                "codigo_postal": cp,
                "num_exterior": numExt,
                "numero_interior": numInt,
                "colonia": colonia
            }
        }
        headers = {"Content-Type": "application/json","Authorization": f"Bearer {token}"}
        data=json.dumps(info)
        response =  requests.post(url + "nuevo-contacto",data=data, headers=headers)
        response.raise_for_status()
        datos = response.json()





    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            getToken(),
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
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "nombre"}, "Nombre(s): "),
                                                    html.input({"type": "text", "id": "nombre", "name": "nombre", "class": "form-control","required":"true", "onChange":lambda event : setNombre(str(event['currentTarget']['value']))}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "correo"}, "Correo: "),
                                                    html.input({"type": "email", "id": "correo", "name": "correo", "class": "form-control","required":"true", "onChange":lambda event : setCorreo(str(event['currentTarget']['value']))}),
                                                ),
                                                 html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "telefono"}, "Teléfono: "),
                                                    html.input({"type": "number", "id": "telefono", "name": "telefono", "class": "form-control","required":"true", "onChange":lambda event : setTelefono(str(event['currentTarget']['value']))}),
                                                ),
                                            ),
                                            
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "calle"}, "Calle: "),
                                                    html.input({"type": "text", "id": "calle", "name": "calle", "class": "form-control","required":"true", "onChange":lambda event : setCalle(str(event['currentTarget']['value']))}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ciudad"}, "Ciudad: "),
                                                    html.input({"type": "text", "id": "ciudad", "name": "ciudad", "class": "form-control","required":"true", "onChange":lambda event : setCiudad(str(event['currentTarget']['value']))}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "cp"}, "Código Postal: "),
                                                    html.input({"type": "number", "id": "cp", "name": "cp", "class": "form-control","required":"true", "onChange":lambda event : setCp(str(event['currentTarget']['value']))}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ne"}, "Número Exterior: "),
                                                    html.input({"type": "number", "id": "ne", "name": "ne", "class": "form-control","required":"true", "onChange":lambda event : setNumExt(str(event['currentTarget']['value']))}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ni"}, "Número Interior: "),
                                                    html.input({"type": "number", "id": "ni", "name": "ni", "class": "form-control","required":"true", "onChange":lambda event : setNumInt(str(event['currentTarget']['value']))}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "colonia"}, "Colonia: "),
                                                    html.input({"type": "text", "id": "colonia", "name": "colonia", "class": "form-control","required":"true", "onChange":lambda event : setColonia(str(event['currentTarget']['value']))}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row"},
                                                html.div(
                                                    {"class": "col text-center"},
                                                    html.button({"type": "submit", "class": "btn btn-primary", "onClick":lambda event:btn_submit(event, nombre, correo, telefono, calle, ciudad, cp, numExt, numInt,colonia)}, "Añadir Contacto"),
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
