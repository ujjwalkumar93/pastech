// Copyright (c) 2021, Ujjwal kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Mobile', {
	brand: function(frm){
		frappe.call({
			method: 'get_brand_name',
			doc: frm.doc,
			callback: function(resp){
				if(resp.message){
					frm.doc.brand_name = resp.message
					frm.refresh_field("brand_name")
				}
			}
		})
		
	}
});
