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
    return frappe.db.get_value("Mobile",{'name':mobile},['name','model_name','ram','rom','camera','phone_image','display','maximum_price'],as_dict = True)
@frappe.whitelist(allow_guest=True)
def handle_website_user(email,name,password=None):
    if not frappe.db.exists("Website User", {email:email}) and not password:
        return "password"
    else:
        try:
            usr = frappe.new_doc("User")
            usr.email = email
            usr.first_name = name
            #usr.new_password = password
            usr.insert()
        except frappe.OutgoingEmailError:
            print(frappe.get_traceback())
            pass # email server not set, don't send email

@frappe.whitelist(allow_guest=True)
def get_primary_condition_check(mobile):
    data = frappe.get_all("Primary Condition Check",{"parent":mobile},["questation","valuation","description","yes","no","name"])
    que_list = []
    for d in data:
        d["y"] = False
        d["n"] = False
        que_list.append(d)
    return que_list

@frappe.whitelist(allow_guest=True)
def get_primary_secondary_check(mobile):
    data =  frappe.get_all("Secondary Condition Check",{"parent":mobile},["questation","valuation","description","yes","no","name"])
    que_list = []
    for d in data:
        d["y"] = False
        d["n"] = False
        que_list.append(d)
    return que_list

@frappe.whitelist(allow_guest=True)
def create_website_user(email,gmail_uid,full_name):
    user = frappe.get_doc("Website User",email)
    if user:
        return "User already exist"
    else:
        usr_doc = frappe.new_doc("Website User")
        usr_doc.full_name = full_name
        usr_doc.gmail_uid = gmail_uid
        usr_doc.email = email
        usr_doc.insert()
        return "User created"
# @frappe.whitelist(allow_guest=True)
# def modify_website_user(email,full_name):


@frappe.whitelist(allow_guest=True)
def add_address(email,full_name,mobile,full_address,city,postal_code,state):
    user = frappe.get_doc("Website User",email)
    if user:
        is_this_default_add = False
        if len(user.get("address_list")) == 0:
            is_this_default_add = True
        user.append("address_list", {
            "full_name" : full_name,
            "mobile" : mobile,
            "full_address" : full_address,
            "city" : city,
            "postal_code" : postal_code,
            "state" : state,
            "enable" : is_this_default_add
        })
        user.save()

@frappe.whitelist(allow_guest=True)
def modify_address(email,full_name,mobile,full_address,city,postal_code,state,add_doc_name):
    q = "update `tabAddress List` set full_name = {0},mobile = {1}, full_address = {2}, city = {3}, postal_code = {4}, state = {5}, email = {6} where name = {7};".format(full_name,mobile,full_address,city,postal_code,state,email,add_doc_name)
    frappe.db.sql(q)
    frappe.db.commit()
    return "Address Updated"

    
