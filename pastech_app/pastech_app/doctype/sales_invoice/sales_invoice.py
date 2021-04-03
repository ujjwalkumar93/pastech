# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ujjwal kumar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SalesInvoice(Document):
	def get_mobile(self):
		if self.scan_barcode:
			mobile = frappe.db.get_value("Mobile Details", {'imei': self.scan_barcode}, ['model','selling_price', 'parent','imei'], as_dict= True)
			if mobile:
				brand = frappe.db.get_value("Mobile", {"name": mobile.get('parent')}, 'brand_name')
				mobile['brand_name'] = brand
				return mobile
			else:
				return 'not found'