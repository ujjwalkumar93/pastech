from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Document"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Mobile",
                    "doctype": "Mobile",
                },
                {
                    "type": "doctype",
                    "name": "Brand",
                    "doctype": "Brand",
                },
                {
                    "type": "doctype",
                    "name": "Make Invoice",
                    "doctype": "Sales Invoice",
                },
            ]
        },
        {
            "label": _("Data Import and Export"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Data Import",
                    "doctype": "Data Import",
                },
                {
                    "type": "doctype",
                    "name": "Data Export",
                    "doctype": "Data Export",
                }
            ]
        }
    ]