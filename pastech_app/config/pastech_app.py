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
                    "label": "Master Data",
                },
                {
                    "type": "doctype",
                    "name": "Brand",
                    "doctype": "Brand",
                },
            ]
        }
    ]