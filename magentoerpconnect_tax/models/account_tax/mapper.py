# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.magentoerpconnect.backend import magento, magento2000
from openerp.addons.connector.unit.mapper import \
    mapping, ImportMapper


@magento
class TaxImportMapper(ImportMapper):
    _model_name = 'magento.account.product.fiscal.classification'

    # direct = [
    #     ('class_name', 'name'),
    # ]

    @mapping
    def name(self, record):
        return {'name': record['class_name']}

    @mapping
    def magento_id(self, record):
        return {'magento_id': record['class_id']}

    @mapping
    def backend_id(self, record):
        return {'backend_id': self.backend_record.id}

    @mapping
    def active(self, record):
        return {'active': True}
