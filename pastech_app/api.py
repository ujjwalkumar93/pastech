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
def get_all_branbds():
    return frappe.db.get_all("Brand",{},['*'])