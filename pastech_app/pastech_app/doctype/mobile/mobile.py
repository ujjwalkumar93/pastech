# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ujjwal kumar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Mobile(Document):
	def get_brand_name(self):
		return frappe.db.get_value("Brand", {'name': self.brand}, 'brand_name')