# -*- coding: utf-8 -*-
# © 2015 AvanzOSC
# © 2015 Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MrpProduction(models.Model):

    _inherit = 'mrp.production'

    no_confirm = fields.Boolean('No Confirm')
