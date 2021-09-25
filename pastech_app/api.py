import frappe

@frappe.whitelist(allow_guest=True)
def create_customer_enquiry(name,phone,email,data):
    doc = frappe.new_doc("Customer Enquiry")
    doc.name = name
    doc.mobile = phone
    doc.email = email
    doc.enquiry = data
    doc.insert()
    if doc.get("name"):
        return True
    else:
        return False

@frappe.whitelist(allow_guest=True)
def get_all_brands():
    return frappe.db.get_all("Mobile",{},['*'])

@frappe.whitelist(allow_guest=True)
def get_all_mobiles():
    all_models = frappe.db.get_all("Model",{},['name','parent','model_name'])
    data = []
    for model in all_models:
        d = {}
        phone = "{0}-{1}".format(model.get("parent"),model.get("model_name"))
        d["name"] = phone
        d["key"] = model.get("name")
        data.append(d)
    return data 
