# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Director(models.Model):
    _inherit = 'base.entity'
    nombre = fields.Char(string="nombre", required=True)
    pelicula_id = fields.One2many('filmoteca.peliculas','director_id', string="peliculas")

class Peliculas(models.Model):
    _name = 'filmoteca.peliculas'
    titulo = fields.Char(string="titulo", required=True)
    tematica = fields.Selection([('Horror', 'horror'), ('Comedy', 'comedy'), ('action', 'Accion')], 'Genero')
    director_id = fields.Many2one('filmoteca.director', string="director")
    actores_id = fields.Many2one('filmoteca.actores', string="actor")
    salas_id = fields.Many2one('filmoteca.salas', string="sala")
    costePelicula = fields.Integer (
        compute="_get_costePelicula",
        string="CostePelicula",
        readonly=True,
    )
    def _get_costePelicula(self):
        for record in Actores:
            self.costePelicula = Actores.cache + self.costePelicula
    
class Actores(models.Model):
    _inherit = 'base.entity'
    nombre = fields.Char(string="nombre", required=True)
    cache = fields.Integer(string="numero de cache")
    rol = fields.Char(string="papel interpretado")
    peliculas_id = fields.One2many('filmoteca.peliculas','actores_id', string="peliculas")
 
class Salas(models.Model):
    _inherit = 'base.empresa'
    nombre = fields.Char(string="nombre", required=True)
    direccion = fields.Char(string="direccion", required=True)
    recaudacion = fields.Integer(string="recaudacion")
    peliculas_id = fields.One2many('filmoteca.peliculas','salas_id', string="peliculas")
    sesion_id = fields.One2many('filmoteca.sesion','sala_id', string="sesiones")
    

class Sesion(models.Model):
    _name = 'filmoteca.sesion'
    horario = fields.Char(string="horario", required=True)
    precio = fields.Integer(string="precio")
    numeroAsistentes = fields.Integer(string="numeroAsistentes")
    recaudacionSesion = fields.Integer(string="recaudacion")
    @api.onchange('recaudacionSesion')
    def _onchange_price(self):
            self.recaudacionSesion = self.numeroAsistentes * self.precio

    sala_id = fields.Many2one('filmoteca.salas', string="salas")

