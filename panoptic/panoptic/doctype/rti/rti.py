# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

from frappe.model.naming import make_autoname
from frappe.website.website_generator import WebsiteGenerator

class RTI(WebsiteGenerator):
	def autoname(self):
		if not self.name:
				self.name = make_autoname("RTI-.#####")

	def make_route(self):
		return 'right-to-information/' + self.name