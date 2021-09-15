# -*- coding: utf-8 -*-


from logging import exception
from re import match
# from typing_extensions import Required
from odoo import models, fields ,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
import re
from odoo.exceptions import ValidationError


class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Real Estate'
    _sql_constraints=[
        ('check_expected_price','CHECK(expected_price > 0)','please give true expected value'),
        ('check_selling_price','CHECK(selling_price > 0)','please enter actual selling value' )
    ]
    

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    expected_price = fields.Float(string='Expected Price', required=True)
    bedrooms = fields.Integer(string='Bedrooms', default=lambda self: (2))
    facades = fields.Integer(string='Facades', default=lambda self: (0))
    garden = fields.Boolean(string='Garden')
    garden_orientation = fields.Selection([
        ('orientation_1','Orientation 1'),
        ('orientation_2', 'Orientation 2')
        # ('orientation_3','Orientation 3'),
        # ('orientation_4', 'Orientation 4')
    ])
    # client_id = fields.Many2one('res.users', string='Client')
    active = fields.Boolean(string='Active')
    available_from = fields.Date(string='Available From', default=lambda self: fields.Datetime.now()+relativedelta(months=3))
    selling_price = fields.Float(string='Selling Price')
    living_area = fields.Integer(string='Living Area (sqm)')
    garage = fields.Boolean(string='Garage')
    garage_area = fields.Integer(string='Garage Area (meter)')
    status = fields.Selection([
        ('new','New'),
        ('old', 'Old')
    ], required=True, default='new')
    property=fields.Selection([
        ('house','House'),
        ('apartment', 'Apartment')], required=True, default='house')
    # buyer_id=fields.Many2many('res.partner',string='Buyer')
    # tin_id = fields.Many2many('res.partner',string='Tin')
    area=fields.Integer()

    # @api.depends("area")
    # def _compute_area(self):
    #     for record in self:
    #         record.area=2.0*record.garage_area
    

# class Tax(models.Model):
#     _name = 'tax.file'
#     _description = 'Taxation'
#     _sql_constraints=[
#         ('taxpayer_email','UNIQUE(taxpayer_email)','E-mail already exist'),
#     ]
#     title = fields.Char(string='Title', required=True)
#     description = fields.Text(string='Description')

#     taxpayer_name= fields.Char(string='Taxpayer')
#     taxpayer_email=fields.Char(string='Email',required=True)
#     taxpayer_id= fields.Char(string='TIN Number')
#     image= fields.Binary(string='Image')
#     # tin_id = fields.Many2many('res.users',string='Tin')
    
#     tax=fields.Float(compute="_compute_tax",inverse="_inverse_tax")
#     amount=fields.Float()


    # @api.depends("amount")
    # def _compute_tax(self):
    #     for record in self:
    #         record.tax=2.0*record.amount

    
    # def _inverse_tax(self):
    #     for record in self:
    #         record.amount=record.tax/2.0    
                    
    # @api.onchange('taxpayer_email')
    # def validate_mail(self):
    #      if self.taxpayer_email:
    #          match= re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.taxpayer_email)
    #          if match==None:
    #              raise ValidationError('Not a valid E-mail, please provide valid E-mail')      


class ResUsers(models.Model):
    _inherit ='res.users'
    buyer_id=fields.Char(string='Buyers')
    description=fields.Char(string='description')