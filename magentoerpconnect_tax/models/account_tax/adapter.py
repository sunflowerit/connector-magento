# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.magentoerpconnect.backend import magento, magento2000
from openerp.addons.magentoerpconnect.unit.backend_adapter import \
    GenericAdapter


@magento
class TaxAdapter(GenericAdapter):
    _model_name = 'magento.account.product.fiscal.classification'

    _magento2_model = 'taxClasses'
    _magento2_search = 'taxClasses/search'
    _magento2_key = 'class_id'

    def search(self):
        """ Search all records and return a list of ids """

        if not self.magento.version == '2.0':
            return []
        filters = {'class_type': {'eq': 'PRODUCT'}}
        return super(TaxAdapter, self).search(filters=filters)

    def read(self, id, storeview_id=None, attributes=None):
        """ Returns the information of a record """
        if self.magento.version == '2.0':
            return super(TaxAdapter, self).read(
                id, attributes=attributes)
