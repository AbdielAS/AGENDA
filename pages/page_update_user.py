from reactpy import component, html, hooks
from components import navbar_top, navbarMenu
from reactpy_router import link, use_params
import json
import requests


@component
def Page_UpdateContact():
    token,setToken = reactpy.hooks.use_state("Ignore")
    nombre, setNombre = hooks.use_state("")
    correo, setCorreo = hooks.use_state("")
    telefono, setTelefono = hooks.use_state("")
    calle, setCalle = hooks.use_state("")
    ciudad, setCiudad = hooks.use_state("")
    cp, setCp = hooks.use_state("")
    numExt, setNumExt = hooks.use_state("")
    numInt, setNumInt = hooks.use_state("")
    colonia, setColonia = hooks.use_state("")

    id_contact = use_params()

    id_contact = id_contact["id"]

    url = "https://api-agenda-8dij.onrender.com/"

    #token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JyZW8iOiJwZWRyb2FiZGllbDI3QGdtYWlsLmNvbSIsImNvbnRyYXNlXHUwMGYxYSI6InBhYXMyNyIsImV4cCI6MTcwMjc5MTcxOX0.ufpClNv5PcciOH7yViYlnBkCB4hamqd46mfxy_sDJcU"

    def Datos():
        headers = {"Authorization": f"Bearer {token}"}
        response =  requests.get(f"{url}contacto_id/{id_contact}", headers=headers)
        response.raise_for_status()
        datos = response.json()
        setNombre(datos["nombre"])
        setCorreo(datos["correo"])
        setTelefono(datos["telefono"])
        setCalle(datos["direccion"]["calle"])
        setCiudad(datos["direccion"]["cuidad"])
        setCp(datos["direccion"]["codigo_postal"])
        setNumExt(datos["direccion"]["num_exterior"])
        setNumInt(datos["direccion"]["numero_interior"])
        setColonia(datos["direccion"]["colonia"])

    def Update(e, nombre, correo, telefono, calle, ciudad, cp, numExt, numInt,colonia):
       
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
        response =  requests.put(url+"update_contact/"+id_contact,data=data, headers=headers)
        response.raise_for_status()
        datos = response.json()


    hooks.use_effect(Datos, [])

    titulo = "Editar Contacto"

    icono = "bi bi-person-plus"

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
                                            html.b("Editar Contacto"),
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
                                                    html.input({"type": "text", "id": "nombre", "name": "nombre", "class": "form-control", "value":nombre,"onChange":lambda event : setNombre(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "correo"}, "Correo: "),
                                                    html.input({"type": "text", "id": "correo", "name": "correo", "class": "form-control", "value":correo,"onChange":lambda event : setCorreo(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                                 html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "telefono"}, "Teléfono: "),
                                                    html.input({"type": "text", "id": "telefono", "name": "telefono", "class": "form-control", "value":telefono, "onChange":lambda event : setTelefono(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                            ),
                                            
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "calle"}, "Calle: "),
                                                    html.input({"type": "text", "id": "calle", "name": "calle", "class": "form-control", "value":calle, "onChange":lambda event : setCalle(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ciudad"}, "Ciudad: "),
                                                    html.input({"type": "text", "id": "ciudad", "name": "ciudad", "class": "form-control", "value":ciudad,"onChange":lambda event : setCiudad(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "cp"}, "Código Postal: "),
                                                    html.input({"type": "text", "id": "cp", "name": "cp", "class": "form-control", "value":cp, "onChange":lambda event : setCp(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ne"}, "Número Exterior: "),
                                                    html.input({"type": "text", "id": "ne", "name": "ne", "class": "form-control", "value":numExt,"onChange":lambda event : setNumExt(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row mb-3"},
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "ni"}, "Número Interior: "),
                                                    html.input({"type": "text", "id": "ni", "name": "ni", "class": "form-control", "value":numInt,"onChange":lambda event : setNumInt(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                                html.div(
                                                    {"class": "col"},
                                                    html.label({"for": "colonia"}, "Colonia: "),
                                                    html.input({"type": "text", "id": "colonia", "name": "colonia", "class": "form-control", "value":colonia, "onChange":lambda event : setColonia(str(event['currentTarget']['value'])),"required":"true"}),
                                                ),
                                            ),
                                            html.div(
                                                {"class": "row"},
                                                html.div(
                                                    {"class": "col text-center"},
                                                    html.button({"type": "submit", "class": "btn btn-primary", "onClick":lambda event:Update(event, nombre, correo, telefono, calle, ciudad, cp, numExt, numInt,colonia)}, "Actualizar Información"),
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
