from reactpy import component, html


@component
def Navbar():
    navbar_style = {
        "backgroundColor": "white",
    }

    return html.ul(
        {
            "className": "navbar-nav sidebar sidebar-dark accordion",
            "id": "accordionSidebar",
            "style": navbar_style,
        },
        html.a(
            {
                "href": "#",
                "className": "d-flex align-items-center justify-content-center",
            },
            html.div(
                {"className": "navbar-brand"},
                html.a(
                    {
                        "class": "btn mx-3",
                        "style": {
                            "color": "black",
                            "display": "flex",
                            "alignItems": "center",
                        },
                    },
                    html.i(
                        {
                            "class": "bi bi-motherboard",
                            "style": {
                                "fontSize": "30px",
                                "marginRight": "8px",
                                "fill": "currentColor",
                            },
                        }
                    ),
                    html.b({"style": {"lineHeight": "1"}}, "B I G   D A T A"),
                ),
            ),
        ),
        html.hr(
            {
                "className": "sidebar-divider my-0",
                "style": {"backgroundColor": "black", "marginTop": "11%"},
            }
        ),
        html.div(
            {
                "className": "sidebar-heading",
                "style": {
                    "textAlign": "center",
                    "marginTop": "15%",
                    "fontSize": "15px",
                },
            },
            html.p({"style": {"color": "black"}}, html.b("A G E N D A")),
        ),
        html.hr(
            {
                "className": "sidebar-divider my-0",
                "style": {"backgroundColor": "black", "marginTop": "11%"},
            }
        ),
        html.li(
            {
                "class": "nav-item active",
                "style": {
                    "marginLeft": "10%",
                    "marginTop": "8%",
                    "color": "#000000",
                    "textAlign": "left",
                },
            },
            html.i(
                {
                    "class": "bi bi-person-plus",
                    "style": {"fontSize": "20px", "marginRight": "8px"},
                }
            ),
            html.b(
                html.a({"href": "/Añadir_Contacto", "style": {"color": "black"}}, "Añadir Contacto")
            ),
        ),
        html.li(
            {
                "class": "nav-item active",
                "style": {
                    "marginLeft": "10%",
                    "marginTop": "8%",
                    "color": "#000000",
                    "textAlign": "left",
                },
            },
            html.i(
                {
                    "class": "bi bi-person-vcard",
                    "style": {"fontSize": "20px", "marginRight": "8px"},
                }
            ),
            html.b(
                html.a({"href": "/Ver_Contactos", "style": {"color": "black"}}, "Ver Contactos")
            ),
        ),
          html.li(
            {
                "class": "nav-item active",
                "style": {
                    "marginLeft": "10%",
                    "marginTop": "8%",
                    "color": "#000000",
                    "textAlign": "left",
                },
            },
            html.i(
                {
                    "class": "bi bi-newspaper",
                    "style": {"fontSize": "20px", "marginRight": "8px"},
                }
            ),
            html.b(
                html.a({"href": "/Ver_Contactos_Combinados", "style": {"color": "black"}}, "Ver Contactos Combinados")
            ),
        ),
        html.li(
            {
                "className": "nav-item active",
                "style": {
                    "marginLeft": "10%",
                    "marginTop": "8%",
                    "color": "#000000",
                    "textAlign": "left",
                },
            },
            html.i(
                {
                    "className": "bi bi-people",
                    "style": {"fontSize": "20px", "marginRight": "8px"},
                }
            ),
            html.b(
                html.a(
                    {"href": "/Ver_Usuarios", "style": {"color": "black"}},
                    "Ver Usuarios",
                )
            ),
        ),
        html.li(
            {
                "className": "nav-item active",
                "style": {
                    "marginLeft": "10%",
                    "marginTop": "8%",
                    "color": "#000000",
                    "textAlign": "left",
                },
            },
            html.i(
                {
                    "className": "bi bi-envelope",
                    "style": {"fontSize": "20px", "marginRight": "8px"},
                }
            ),
            html.b(
                html.a(
                    {"href": "/Solicitudes", "style": {"color": "black"}},
                    "Solicitudes",
                )
            ),
        ),
        html.hr(
            {
                "className": "sidebar-divider my-0",
                "style": {"backgroundColor": "black", "marginTop": "11%"},
            }
        ),
    )
