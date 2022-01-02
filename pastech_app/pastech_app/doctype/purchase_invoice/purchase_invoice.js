// Copyright (c) 2021, Ujjwal kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase Invoice', {
	// refresh: function(frm) {

	// }
	appointment: function(frm){
		frappe.db.get_value("Appointment",{"name":frm.doc.appointment},"full_name", resp => {
			frm.doc.supplier_name = resp.full_name
			frm.refresh_field("supplier_name")
		})
	}
});
