
from odoo import models, fields, api, _
from odoo.tools.misc import formatLang, format_date
import math

class AccountPayment(models.Model):
    _inherit = "account.payment"

    #Para a~nadir al Stub la fecha de la factura pagada
    def _check_make_stub_line(self, invoice):
        """ Return the dict used to display an invoice/refund in the stub
        """
        # Find the account.partial.reconcile which are common to the invoice and the payment
        if invoice.type in ['in_invoice', 'out_refund']:
            invoice_sign = 1
            invoice_payment_reconcile = invoice.line_ids.mapped('matched_debit_ids').filtered(lambda r: r.debit_move_id in self.move_line_ids)
        else:
            invoice_sign = -1
            invoice_payment_reconcile = invoice.line_ids.mapped('matched_credit_ids').filtered(lambda r: r.credit_move_id in self.move_line_ids)

        if self.currency_id != self.journal_id.company_id.currency_id:
            amount_paid = abs(sum(invoice_payment_reconcile.mapped('amount_currency')))
        else:
            amount_paid = abs(sum(invoice_payment_reconcile.mapped('amount')))

        amount_residual = invoice_sign * invoice.amount_residual

        return {
            'due_date': format_date(self.env, invoice.invoice_date_due),
            'date': format_date(self.env, invoice.invoice_date),
            'number': invoice.ref and invoice.name + ' - ' + invoice.ref or invoice.name,
            'amount_total': formatLang(self.env, invoice_sign * invoice.amount_total, currency_obj=invoice.currency_id),
            'amount_residual': formatLang(self.env, amount_residual, currency_obj=invoice.currency_id) if amount_residual * 10**4 != 0 else '-',
            'amount_paid': formatLang(self.env, invoice_sign * amount_paid, currency_obj=self.currency_id),
            'currency': invoice.currency_id,
        }

    def extraeDecimales(self, nNumero, max_digits=2):
        strDecimales = str( round(nNumero%1, 2) ).replace('0.','')
        strDecimales += "0"*max_digits
        strDecimales = strDecimales[0:max_digits]
        return float(strDecimales)

    @api.depends('payment_method_id', 'amount')
    def _amount_in_words(self):

        for order in self:

            num = order.amount
            amount_words = ''
            if num:
                currency_id = order.currency_id
                amount_words = currency_id.amount_to_text(math.floor(order.amount))
                amount_words = amount_words.replace("Pesos", "")

                intCantDecimal = self.extraeDecimales(order.amount)
                if intCantDecimal <= 9:
                    strCantDecimal = "0%d" % (intCantDecimal)
                else:
                    strCantDecimal = "%d" % (intCantDecimal)
                strCantDecimal += "/100"

                amount_words += " con " + strCantDecimal

            order.update({
                'check_amount_in_words': amount_words,
            })

    check_amount_in_words = fields.Text(string='Amount in words', compute='_amount_in_words', readonly=True, translate=True)