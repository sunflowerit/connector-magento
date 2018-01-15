# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.magentoerpconnect.backend import magento, magento2000
from openerp.addons.magentoerpconnect.product import ProductImporter2000
from openerp.addons.connector.unit.mapper import mapping
from openerp.addons.connector.exception import MappingError


@magento2000(replacing=ProductImporter2000)
class ProductImporter2000WithTaxSupport(ProductImporter2000):
    """ This extends the main product import with tax support. """

    def _import_dependencies(self):
        ret = super(ProductImporter2000WithTaxSupport,
                    self)._import_dependencies()
        # import related tax classes
        record = self.magento_record
        mag_tax_class_id = record.get('tax_class_id', None)
        if mag_tax_class_id:
            self._import_dependency(mag_tax_class_id,
                'magento.account.product.fiscal.classification')
        return ret

