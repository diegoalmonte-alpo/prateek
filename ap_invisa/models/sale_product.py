# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    print_image = fields.Boolean(
        "Print Image",
        help="""If ticked, you can see the product image in
        report of sale order/quotation""",
    )
    image_sizes = fields.Selection(
        [
            ("image", "Big sized Image"),
            ("image_medium", "Medium Sized Image"),
            ("image_small", "Small Sized Image"),
        ],
        "Image Sizes",
        default="image_small",
        help="Image size to be displayed in report",
    )


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    image_small = fields.Binary("Product Image", related="product_id.image_1920")

    @api.depends('product_id')
    def _compute_is_service(self):
        for so_line in self:
            if (so_line.product_id.type == 'service' or so_line.product_id.service_tracking != 'no'):
                so_line.is_service = True
            else:
                so_line.is_service = False

