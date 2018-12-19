# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    request_id = fields.Many2one('crm.lead')


class Request(models.Model):
	_inherit = 'crm.lead'
	request_method = fields.Selection(
		selection=[('phone','Phone'),('email','E-mail'),('other','Other')]
		)

class RequestCheck(models.Model):
	_name = 'request.check'
	name = fields.Char(compute="_get_name")
	request_id = fields.Many2one('crm.lead')
	item_name = fields.Char(related='request_id.name')
	website = fields.Char()
	cost = fields.Float(string='Item Cost')
	available = fields.Boolean()
	delivery_cost = fields.Float(string='Delivery Cost')
	service_percent = fields.Float()
	total_cost = fields.Float(compute="get_total_cost")
	delivery_time = fields.Integer(string="can be delivered in: ")

	@api.one
	def _get_name(self):
		self.name = "CHRQ00" + str(self.id)
	
	@api.one
	def get_total_cost(self):
		added_cost = self.cost * self.service_percent/100 
		self.total_cost = self.cost + self.delivery_cost + added_cost