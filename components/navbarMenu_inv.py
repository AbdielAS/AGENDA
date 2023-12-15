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
    )