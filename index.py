from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages import page_addcontact, page_contacts, page_requests, page_users, page_createuser, page_contacts_merge, page_contacts_user, page_requests, page_login
#from pages.pages_client import page_catalogo_user, page_requests_user, page_cuentas_user

@component
def App():
    return simple.router(
        #route("/API", EJEMPLOAPI.App()),
        
        route("/", page_login.login_user()),
        route("/Añadir_Contacto", page_addcontact.Page_AddContacts()),
        route("/Ver_Contactos", page_contacts.Page_Contacts()),
        route("/Ver_Usuarios", page_users.Page_Users()),
        route("/Crear_Usuario", page_createuser.Page_CreateUser()),
        route("/Ver_Contactos_Combinados", page_contacts_merge.Page_ContactsMerge()),
        route("/Ver_Contactos_Usuario", page_contacts_user.Page_ContactsUser()),
        route("/Solicitudes", page_requests.Page_Solicitudes()),

        
        #route("/Admin_Cuentas", page_cuentas_admin.Page_Cuentas()),
        #route("/Admin_Pronostico", page_forcast_admin.Page_Forcast()),
        #route("/Admin_Solicitudes", page_requests_admin.Page_Solicitudes()),
        #route("/Admin_Almacenes", page_store_admin.Page_Almacenes()),
        #route("/Admin_Racks", page_racks_admin.Page_Racks()),
        #route("/Admin_Catalogo", page_catalogo_admin.Page_Catalogo()),
        #route("/"),
        #route("/User_Cuentas", page_cuentas_user.Page_Cuentas()),
        #route("/User_Catalogo", page_catalogo_user.Page_Catalogo()),
        
    )


app = FastAPI()

configure(app, App)
