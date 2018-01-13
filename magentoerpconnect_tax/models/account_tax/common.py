# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from openerp import models, fields

# import xmlrpclib
# from openerp.addons.connector.unit.mapper import \
#     mapping, ImportMapper
# from openerp.addons.connector.exception import \
#     IDMissingInBackend, MappingError
# from .unit.backend_adapter import \
#     GenericAdapter, MAGENTO_DATETIME_FORMAT
# from .unit.import_synchronizer import DelayedBatchImporter, \
#     DirectBatchImporter, MagentoImporter, TranslationImporter, \
#     AddCheckpoint
# from .backend import magento, magento1700, magento2000
# from .connector import get_environment

_logger = logging.getLogger(__name__)


class MagentoAccountProductFiscalClassification(models.Model):
    _name = 'magento.account.product.fiscal.classification'
    _inherit = 'magento.binding'
    _inherits = {'account.product.fiscal.classification': 'openerp_id'}
    _description = 'Magento Tax Class'

    openerp_id = fields.Many2one(
        comodel_name='account.product.fiscal.classification',
        string='Linked Odoo taxes',
        required=True,
        ondelete='restrict')


class AccountProductFiscalClassification(models.Model):
    _inherit = 'account.product.fiscal.classification'

    magento_bind_ids = fields.One2many(
        comodel_name='magento.account.product.fiscal.classification',
        inverse_name='openerp_id',
        string='Magento Bindings',
    )



# @magento1700
# class ProductCategoryBatchImporter(DelayedBatchImporter):
#     """ Import the Magento Product Categories.
#
#     For every product category in the list, a delayed job is created.
#     A priority is set on the jobs according to their level to rise the
#     chance to have the top level categories imported first.
#     """
#     _model_name = ['magento.product.category']
#
#     def _import_record(self, magento_id, priority=None):
#         """ Delay a job for the import """
#         super(ProductCategoryBatchImporter, self)._import_record(
#             magento_id, priority=priority)
#
#     def run(self, filters=None):
#         """ Run the synchronization """
#         from_date = filters.pop('from_date', None)
#         to_date = filters.pop('to_date', None)
#         if from_date or to_date:
#             updated_ids = self.backend_adapter.search(filters,
#                                                       from_date=from_date,
#                                                       to_date=to_date)
#         else:
#             updated_ids = None
#
#         base_priority = 10
#
#         def import_nodes(tree, level=0):
#             for node_id, children in tree.iteritems():
#                 # By changing the priority, the top level category has
#                 # more chance to be imported before the childrens.
#                 # However, importers have to ensure that their parent is
#                 # there and import it if it doesn't exist
#                 if updated_ids is None or node_id in updated_ids:
#                     self._import_record(node_id, priority=base_priority+level)
#                 import_nodes(children, level=level+1)
#         tree = self.backend_adapter.tree()
#         import_nodes(tree)
#
#
#
