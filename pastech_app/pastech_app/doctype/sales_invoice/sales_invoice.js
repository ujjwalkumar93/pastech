// Copyright (c) 2021, Ujjwal kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice', {
	onload: function(frm){
		frm.doc.date = frappe.datetime.nowdate()
		frm.refresh_field('date')
	},
	scan_barcode: function(frm,cdt,cdn){
		frappe.call({
			doc: frm.doc,
			method: 'get_mobile',
			callback: function(resp){
				if(resp.message){
					if(resp.message === "not found"){
						let not_found = frm.doc.scan_barcode
						frm.set_value("scan_barcode", '')
						frappe.throw(`Mobile with IMEI <b>${not_found}</b> not found`)

					}
					var row = frm.add_child("mobile_details")
					row.brand = resp.message.brand_name
					row.model = resp.message.model
					row.imei = resp.message.imei
					row.price = resp.message.selling_price
					frm.refresh_field("mobile_details")
					show_alert(`Mobile with IMEI ${frm.doc.scan_barcode} added`, 5);
					frm.set_value("scan_barcode", '')

					// add total value
					var table = locals[cdt][cdn].mobile_details
					var total = 0
					table.map(item => {
						total += parseInt(item.price)
					})
					frm.set_value("total_amount", total)
				}
			}

		})
		
	},
	after_submit: function(frm){
		//console.log("***************** submit")
	}
});
frappe.ui.form.on("Sales Invoice Details", {
	mobile_details_remove : function(frm){
		var table = frm.doc.mobile_details
					var total = 0
					table.map(item => {
						total += parseInt(item.price)
					})
					frm.set_value("total_amount", total)
	}
})
