# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime, timedelta

from openerp import models, fields, api
from openerp.addons.connector.session import ConnectorSession
from openerp.addons.magentoerpconnect.connector import get_environment

from ..account_tax.importer import tax_import_batch

IMPORT_DELTA_BUFFER = 30


class MagentoBackend(models.Model):
    _name = 'magento.backend'
    _inherit = 'magento.backend'

    @api.multi
    def import_tax_classes(self):
        session = ConnectorSession(self.env.cr, self.env.uid,
                                   context=self.env.context)
        for backend in self:
            tax_import_batch.delay(
                session,
                'magento.account.product.fiscal.classification',
                backend.id)
        return True
