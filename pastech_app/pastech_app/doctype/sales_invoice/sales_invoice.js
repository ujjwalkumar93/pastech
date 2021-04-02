// Copyright (c) 2021, Ujjwal kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice', {
	onload: function(frm){
		frm.doc.date = frappe.datetime.nowdate()
		frm.refresh_field('date')
	}
});
