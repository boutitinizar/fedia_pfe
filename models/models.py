# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp





class fedia_pfe(models.Model):
     _name = 'fedia_pfe.adherents'

     id_intern = fields.Integer('Num Adhérent',required=True)
     name = fields.Char('Adhérent',required=True)
     achats   = fields.Float('Achats',digits=(16,3))
     produit = fields.Many2one('fedia_pfe.produits',required=True,string='Produit')
     form_juridique = fields.Many2one('fedia_pfe.form_juridique',required=True,string='Form Juridique')
     activite = fields.Many2one('fedia_pfe.activite',required=True,string='Activité')
     zone_geo = fields.Many2one('fedia_pfe.zone_geo',required=True,string='Zone Géographique')
     note = fields.Text('Note Interne')


     produit_risque = fields.Char('Produit Risque', compute='_calcul_produit_risque', store=True)
     form_juridiquet_risqu = fields.Char('form_juridique Risque', compute='_calcul_form_juridiquet_risque', store=True)
     activite_risque = fields.Char('Activite Risque', compute='_calcul_activite_risque', store=True)
     zone_geo_risque = fields.Char('Zone_geo Risque', compute='_calcul_zone_geo_risque', store=True)


     cm = fields.Integer('Cotation Moyenne',compute='_clacul_cm',store=True )
     rm = fields.Char('Risque Moyen',compute='_clacul_rm',store=True )


     @api.depends('produit', 'form_juridique','activite','zone_geo')
     def _clacul_cm(self):
        for adherent in self:
          data = []
          if adherent.produit.cotation >  0:
              data.append(adherent.produit.cotation)

          if adherent.produit.cotation >  0 :
              data.append(adherent.form_juridique.cotation)

          if adherent.produit.cotation >  0 :
              data.append(adherent.activite.cotation)

          if adherent.produit.cotation >  0 :
              data.append(adherent.zone_geo.cotation)

          if(len(data) > 0):
              sum_adherent =  sum(data) / len(data)
              if(sum_adherent == 2.5 ):
                  adherent.cm = 3
              elif (sum_adherent == 1.5 ):
                  adherent.cm = 2
              else:
                  adherent.cm = round(sum_adherent,0)



     @api.depends('produit', 'form_juridique','activite','zone_geo')
     def _calcul_produit_risque(self):
         for pr in self:
             if pr.produit.risque == '1':
                 pr.produit_risque = 'Faible'
             if pr.produit.risque == '2':
                 pr.produit_risque = 'Moyen'
             if pr.produit.risque == '3':
                 pr.produit_risque = 'Elevé'

     @api.depends('produit', 'form_juridique','activite','zone_geo')
     def _calcul_form_juridiquet_risque(self):
         for pr in self:
             if pr.form_juridique.risque == '1':
                 pr.form_juridiquet_risqu = 'Faible'
             if pr.form_juridique.risque == '2':
                 pr.form_juridiquet_risqu = 'Moyen'
             if pr.form_juridique.risque == '3':
                 pr.form_juridiquet_risqu = 'Elevé'

     @api.depends('produit', 'form_juridique','activite','zone_geo')
     def _calcul_activite_risque(self):
         for pr in self:
             if pr.activite.risque == '1':
                 pr.activite_risque = 'Faible'
             if pr.activite.risque == '2':
                 pr.activite_risque = 'Moyen'
             if pr.activite.risque == '3':
                 pr.activite_risque = 'Elevé'


     @api.depends('produit', 'form_juridique','activite','zone_geo')
     def _calcul_zone_geo_risque(self):
         for pr in self:
             if pr.zone_geo.risque == '1':
                 pr.zone_geo_risque = 'Faible'
             if pr.zone_geo.risque == '2':
                 pr.zone_geo_risque = 'Moyen'
             if pr.zone_geo.risque == '3':
                 pr.zone_geo_risque = 'Elevé'







     @api.depends('produit', 'form_juridique','activite','zone_geo')
     def _clacul_rm(self):
        for adherent in self:
            if adherent.cm == 1:
                adherent.rm = 'Faible'
            if adherent.cm == 2:
                adherent.rm = 'Moyen'
            if adherent.cm == 3:
                adherent.rm = 'Elevé'



class fedia_pfe_prduit(models.Model):
    _name = 'fedia_pfe.produits'

    name = fields.Char('Produit',required=True)
    cotation = fields.Integer( compute='_clacul_cotation',store=True ,string='Cotation')

    risque = fields.Selection([
        ('1', 'Faible'),
        ('2','Moyen'),
        ('3','Elevé')
    ],string='Risque',)

    @api.depends('risque')
    def _clacul_cotation(self):
        for cot in self:
            risque = dict(self._fields['risque'].selection).get(cot.risque)
            if risque == 'Faible':
                cot.cotation = 1
            if risque == 'Moyen':
                cot.cotation = 2
            if risque == 'Elevé':
                cot.cotation = 3







class fedia_pfe_form_juridique(models.Model):
    _name = 'fedia_pfe.form_juridique'

    name = fields.Char('Form Juridique',required=True)
    cotation = fields.Integer( compute='_clacul_cotation',store=True ,string='Cotation')
    risque = fields.Selection([
        ('1', 'Faible'),
        ('2','Moyen'),
        ('3','Elevé')
    ],string='Risque',)

    @api.depends('risque')
    def _clacul_cotation(self):
        for cot in self:
            risque = dict(self._fields['risque'].selection).get(cot.risque)
            if risque == 'Faible':
                cot.cotation = 1
            if risque == 'Moyen':
                cot.cotation = 2
            if risque == 'Elevé':
                cot.cotation = 3


class fedia_pfe_zone_geo(models.Model):
    _name = 'fedia_pfe.zone_geo'

    name = fields.Char('Zone Géographique',required=True)
    cotation = fields.Integer( compute='_clacul_cotation',store=True ,string='Cotation')
    risque = fields.Selection([
        ('1', 'Faible'),
        ('2','Moyen'),
        ('3','Elevé')
    ],string='Risque',)

    @api.depends('risque')
    def _clacul_cotation(self):
        for cot in self:
            risque = dict(self._fields['risque'].selection).get(cot.risque)
            if risque == 'Faible':
                cot.cotation = 1
            if risque == 'Moyen':
                cot.cotation = 2
            if risque == 'Elevé':
                cot.cotation = 3



 #    value2 = fields.Float(compute="_value_pc", store=True)
  #   description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100