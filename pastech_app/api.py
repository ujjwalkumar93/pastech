#from tkinter.messagebox import YES
import frappe
import json
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
def get_secondary_condition_check(mobile):
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

@frappe.whitelist(allow_guest=True)
def estimate_buying_price(phone):
    condition_list = frappe.get_all("Primary Condition Check",{"parent":phone},'*')
    data = []
    for cond in condition_list:
        d = {}
        d["key"] = cond.get("name")
        d["que"] = cond.get("questation")
        d["valuation"] = cond.get("valuation")
        data.append(d)
    return data

@frappe.whitelist(allow_guest = True)
def create_appointment(user,mobile,doa,slot,primary_condition,secondary_condition,address_id,estimated_price,time_stamp):
    address = frappe.get_doc("User Address",address_id)
    old_doc = frappe.get_all("Appointment",{"time_stamp":time_stamp,"user":user})
    if len(old_doc) == 0:
        doc = frappe.new_doc("Appointment")
        doc.user = user
        doc.mobile = mobile
        doc.doa = doa
        doc.appointment_slot = slot
        
        for i in json.loads(primary_condition):
            yes = False
            no = False
            if i.get("y"):
                yes = True
            if i.get("n"):
                yes = False
            doc.append("primary_condition", {
                "questation" : i.get("questation"),
                "yes" : yes,
                "no" : no,
                "depreciation" : i.get("valuation")
            })

        for i in json.loads(secondary_condition):
            yes = False
            no = False
            if i.get("y"):
                yes = True
            if i.get("n"):
                yes = False
            doc.append("secondary_condition", {
                "questation" : i.get("questation"),
                "yes" : yes,
                "no" : no,
                "depreciation" : i.get("valuation")
            })
        doc.append("user_address", {
                "full_name": address.get("full_name"),
                "mobile": address.get("mobile"),
                "city" : address.get("city"),
                "postal_code" :"123"
            })
        doc.time_stamp = time_stamp
        doc.estimated_price = estimated_price
        doc.insert(ignore_permissions = True)
        doc.submit()
        return doc.name
    else:
        return False
@frappe.whitelist(allow_guest = True)
def get_address(email):
    usr = frappe.get_doc("Web User", {"email":email})
    return usr.get("address_list")
@frappe.whitelist(allow_guest = True)
def check_postal_code(code):
    data = False
    doc = frappe.get_doc("Portal Setitngs")
    for i in doc.get("postal_code"):
        if i.get("postal_code") == code:
            data = True
    return data
@frappe.whitelist(allow_guest = True)
def get_postal_code():
    data = []
    doc = frappe.get_doc("Portal Setitngs")
    for i in doc.get("postal_code"):
        data.append(i.get("postal_code"))
    return data

@frappe.whitelist(allow_guest = True)
def get_slot():
    data = []
    doc = frappe.get_doc("Portal Setitngs")
    for i in doc.get("slot"):
        data.append({
            "time": i.get("slot"),
            "color": "#ffffff"
        })
    return data

@frappe.whitelist(allow_guest = True)
def get_order_history(user):
    return frappe.get_all("Appointment",{"user":user},['mobile',"doa","estimated_price"])

        

        
    
