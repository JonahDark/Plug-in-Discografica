from odoo import models, fields, api


class discograficamulti_boton_model(models.Model):
    _name = 'discografica.entrada_model'
    _inherit = 'discografica.entrada_model'
    _description = 'discograficamulti'



    def eliminaHistorial(self):
        historialEntradasVendidas = self.search([("active", "=", "False")])
        for rec in historialEntradasVendidas:
            rec.unlink()
