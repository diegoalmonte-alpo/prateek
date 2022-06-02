from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    numero_factura = fields.Char('No Factura', help='Número o Identificación de Factura del Proveedor')
