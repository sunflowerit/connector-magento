# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.magentoerpconnect.backend import magento, magento2000
from openerp.addons.magentoerpconnect.product import ProductImportMapper2000
from openerp.addons.connector.unit.mapper import mapping
from openerp.addons.connector.exception import MappingError


@magento2000(replacing=ProductImportMapper2000)
class ProductImportMapper2000WithTaxSupport(ProductImportMapper2000):
    """ This class extends the main mapper with taxes support. """

    @mapping
    def fiscal_classification_id(self, record):
        mag_tax_class_id = record.get('tax_class_id', None)
        result = {}
        if mag_tax_class_id:
            binder = self.binder_for(
                'magento.account.product.fiscal.classification')
            fiscal_classification_id = binder.to_openerp(
                mag_tax_class_id, unwrap=True)
            if fiscal_classification_id is None:
                raise MappingError(
                    "The tax class with magento id %s "
                    "is not imported." % mag_tax_class_id)
            result.update({'fiscal_classification_id':
                fiscal_classification_id})
        return result
