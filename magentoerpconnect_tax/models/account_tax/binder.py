# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.magentoerpconnect.backend import magento, magento2000
from openerp.addons.magentoerpconnect.unit.binder import MagentoModelBinder


@magento
class TaxBinder(MagentoModelBinder):
    _model_name = ['magento.account.product.fiscal.classification']
