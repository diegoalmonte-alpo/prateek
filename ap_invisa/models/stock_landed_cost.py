from odoo import models, fields, api, _

class StockLandedCostInherit(models.Model):
    _inherit = 'stock.landed.cost'

    vendor_partner_id = fields.Char(string='Proveedor', compute='_compute_fields_relacionados',store=True)
    numero_factura = fields.Char('No Factura', compute='_compute_fields_relacionados',store=True)
    picking_ids_name_field = fields.Char(related='picking_ids.name', store=True, string='M2M')

    @api.depends('vendor_bill_id')
    def _compute_fields_relacionados(self):
        for record in self:
            if record.vendor_bill_id:
                record.vendor_partner_id = record.vendor_bill_id.partner_id.name
                record.numero_factura = record.vendor_bill_id.numero_factura
            else:
                record.vendor_partner_id = ''
                record.numero_factura = ''