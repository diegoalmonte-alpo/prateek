
from odoo import models, fields, api, _

class Product(models.Model):
    _inherit = 'product.template'

    familia_id = fields.Many2one('ap.familia', 'Familia', track_visibility="onchange", help='Familia del Producto')

class FleetVehicleModelBrand(models.Model):
    _name = 'ap.familia'
    _description = 'Familia del Producto'
    _order = 'name asc'

    name = fields.Char('Familia', required=True)