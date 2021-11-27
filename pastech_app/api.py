import frappe

@frappe.whitelist(allow_guest=True)
def create_customer_enquiry(name,phone,email,data):
    doc = frappe.new_doc("Customer Enquiry")
    doc.name1 = name
    doc.mobile = phone
    doc.email = email
    doc.enquiry = data
    doc.insert()
    frappe.db.commit()
    if doc.get("name"):
        return True
    else:
        return False


@frappe.whitelist(allow_guest=True)
def get_all_brands():
    return frappe.db.get_all("Brand",{},['brand_name','brand_logo'])

@frappe.whitelist(allow_guest=True)
def get_all_mobiles():
    return frappe.db.get_all("Mobile",{},['name','model_name'])
@frappe.whitelist(allow_guest=True)
def get_mobile_info(mobile):
    return frappe.db.get_all("Mobile",{'name':mobile},['name','model_name','ram','rom','camera'])

@frappe.whitelist(allow_guest=True)
def get_primary_condition_check(mobile):
    return frappe.get_all("Primary Condition Check",{"parent":mobile},["questation","valuation"])

@frappe.whitelist(allow_guest=True)
def get_primary_secondary_check(mobile):
    return frappe.get_all("Secondary Condition Check",{"parent":mobile},["questation","valuation"])
