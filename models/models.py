# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Provincia(models.Model):
    _name = 'movimientos_aragon.provincia'
    name = fields.Char(string="NombrePro", required=True)
    habitantes = fields.Integer(string="Number de habitantes",compute='_compute_habitantes')
    poblacion_id = fields.One2many('movimientos_aragon.poblacion','provincia_id', string="Poblacion")
    @api.multi
    def _compute_habitantes(self):
        for record in self:
            record.habitantes = 25.000



class Poblacion(models.Model):
    _name = 'movimientos_aragon.poblacion'
    name = fields.Char(string="NombrePob", required=True)
    provincia_id = fields.Many2one('movimientos_aragon.provincia', string="Provincia")
    penas_id = fields.One2many('movimientos_aragon.penas','poblacion_id', string="Peñas")

class Petos(models.Model):
    _name = 'movimientos_aragon.petos'
    numeroDePetos = fields.Integer(string="Number de petos a comprar(la unidad a 10,50)")
    precioUnidad = fields.Integer(string="Precio por unidad")
    colorPeto = fields.Char(string="Color del peto", required=True)
    peña_id = fields.Many2one('movimientos_aragon.penas', string="Peña")
    precioTotalPetos = fields.Integer(string="Number de petos a comprar")
    @api.onchange('numeroDePetos')
    def _onchange_price(self):
            self.precioTotalPetos =10.5*self.numeroDePetos

    

class Penas(models.Model):
    _name = 'movimientos_aragon.penas'
    name = fields.Char(string="NombrePeña", required=True)
    poblacion_id = fields.Many2one('movimientos_aragon.poblacion', string="Poblacion")
    peñista_id = fields.One2many('res.partner','peña_id', string="Peñas")
    petos_id = fields.One2many('movimientos_aragon.petos','peña_id', string="Petos")
    presidentes_id = fields.One2many('base.entidad','peña_id', string="Presidentes")
    colorPeña = fields.Char(string="Color de la peña", required=True)
    integrantes = fields.Integer(string="Number de integrantes")
    local = fields.Boolean('Tiene local ?', compute='_compute_local')
    @api.multi
    def _compute_local(self):
        for record in self:
            record.local = True



class Penista(models.Model):
    _inherit = 'res.partner'
    poblacion_id = fields.Many2one('movimientos_aragon.poblacion', string="Poblacion")
    peña_id = fields.Many2one('movimientos_aragon.penas', string="Peña")
    edad = fields.Integer(string="Edad")


class Presidentes(models.Model):
    _inherit = 'base.entidad'
    peña_id = fields.Many2one('movimientos_aragon.penas', string="Peña")
    añosPresidente = fields.Integer(string="Numero de años como presidente")
   


# class movimientos_aragon(models.Model):
#     _name = 'movimientos_aragon.movimientos_aragon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100