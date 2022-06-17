# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################
from odoo import api, fields, models, _
import datetime
import calendar
     

class vendor_statement(models.TransientModel):
    _name = "vendor.statement"
    
    month = fields.Selection([('1','JAN'),('2','FEB'),('3','MAR'),('4','APR'),('5','MAY'),('6','JUN'),('7','JUL'),('8','AUG'),('9','SEP'),('10','OCT'),('11','NOV'),('12','DEC')])
    aging_by = fields.Selection([('inv_date','Invoice Date'),('due_date','Due Date')],string='Ageing By', default='due_date', required="1")
    
    date_upto = fields.Date('Upto Date',required="1", default=datetime.date.today())
    is_privious_year = fields.Boolean('Print Previous Year')

    currency_id = fields.Many2one('res.currency', string='Currency')

    @api.onchange('month','is_privious_year')
    def onchange_month(self):
        if self.month:
            a= self.month
            a = int(a)
            date=datetime.datetime.now()
            if self.is_privious_year:
                month_end_date=datetime.datetime(date.year-1,a,1) + datetime.timedelta(days=calendar.monthrange(date.year-1,a)[1] - 1)
                self.date_upto = month_end_date.date()
            else:
                month_end_date=datetime.datetime(date.year,a,1) + datetime.timedelta(days=calendar.monthrange(date.year,a)[1] - 1)
                self.date_upto = month_end_date.date()

    
    def send_statement(self):
        partner = self.env['res.partner']
        part_ids=self._context.get('active_ids')
        partner_ids = partner.browse(part_ids)
        if partner_ids:
            partner_ids.write({'overdue_date':self.date_upto,'aging_by':self.aging_by})
        
        ir_model_data = self.env['ir.model.data']
        template_id = ir_model_data.get_object_reference('dev_vendor_account_statement','dev_vendor_send_statement')
        mtp = self.env['mail.template']
        template_id = mtp.browse(template_id[1])
        for partner in partner_ids:
            template_id.send_mail(partner.id, True)
            
            
    def print_statement(self):
        partner = self.env['res.partner']
        part_ids=self._context.get('active_ids')
        partner_ids = partner.browse(part_ids)
        if partner_ids:
            partner_ids.write({'overdue_date':self.date_upto,'aging_by':self.aging_by,'report_currency_id':self.currency_id})
        datas = {
		        'form': partner_ids.ids
		    }
        return self.env.ref('dev_vendor_account_statement.report_vendor_statement').report_action(self, data=datas)
    



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
