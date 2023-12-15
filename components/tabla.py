from reactpy import component, html


@component
def list_headers(headers):
    list_th = [html.th(head) for head in headers]
    return html.tr(list_th)


@component
def list_data(content):
    list_td = []
    list_tr = []
    for data in content:
        td_data = []
        for td in data:
            if td == 1:
                td_data.append(
                    html.td(
                        html.span(
                            {
                                "class_name": "rounded-3 p-1 ",
                                "style": {"background-color": "#f5e679"},
                            },
                            "Ver Agenda",
                        )
                    )
                )
            else:
                td_data.append(html.td({"class_name": "text-dark"}, td))
        list_td.append(td_data)

    for tr in list_td:
        list_tr.append(html.tr(tr))
    return html.tbody(list_tr)


@component
def Tabla(headers, content):
    return html.table(
        {"class_name": "table  table-hover"},
        html.thead(list_headers(headers)),
        list_data(content),
    )


