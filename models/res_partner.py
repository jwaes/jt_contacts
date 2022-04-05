import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = "res.partner"

    type = fields.Selection(selection_add=[('order', 'Order Address')])
    order_address = fields.Many2one('res.partner', string='Order Address', compute='_compute_order_address', store=False)

    @api.depends('order_address', 'type')
    def _compute_order_address(self):
        for partner in self:
            addr_id = self.address_get(['order'])['order']
            self.order_address = self.env['res.partner'].search([('id', '=', addr_id)])
            _logger.debug("order address is  %s", self.order_address)

            # {{ object.partner_id.order_address.id }}
            # user this for the To(Partners) field in the mail template