# -*- coding: utf-8 -*-

from openerp import models, fields, api

class news_app(models.Model):
    _name = 'news.app'
    _inherit = 'mail.thread'

    # _defaults = {'name': lambda obj, cr, uid, context: obj.pool.get(
    #     'ir.sequence').get(cr, uid, 'code_news'), }

    name = fields.Char( required=True, select=True, copy=False, default=lambda
        self: self.env['ir.sequence'].next_by_code('code_news'), help="Unique number")


    title = fields.Char(string="Title", required=True)
    sub_title = fields.Char(string="Sub Title", required=True)
    message = fields.Text(string="Message", required=True)
