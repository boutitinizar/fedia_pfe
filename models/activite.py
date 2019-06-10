from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

class fedia_pfe_activite(models.Model):
    _name = 'fedia_pfe.activite'
    _description = "Adhérents Activité"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'




    name = fields.Char('Activité',index=True, required=True, translate=True)

    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True)

    parent_id = fields.Many2one('fedia_pfe.activite', 'Marché', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('fedia_pfe.activite', 'parent_id', 'Child Categories')

    cotation = fields.Integer(compute='_clacul_cotation', store=True, string='Cotation')
    risque = fields.Selection([
        ('1', 'Faible'),
        ('2','Moyen'),
        ('3','Elevé')
    ],string='Risque',)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s   /  %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name


    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
        return True

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]

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