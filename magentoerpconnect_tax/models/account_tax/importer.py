# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp.addons.connector.queue.job import job
from openerp.addons.magentoerpconnect.connector import get_environment
from openerp.addons.magentoerpconnect.backend import magento, magento2000
from openerp.addons.magentoerpconnect.unit.import_synchronizer \
    import DelayedBatchImporter, MagentoImporter

from .mapper import TaxImportMapper

_logger = logging.getLogger(__name__)


@magento
class TaxBatchImporter(DelayedBatchImporter):
    """ Import the Magento Tax Classes.
        For every tax class in the list, a delayed job is created."""
    _model_name = ['magento.account.product.fiscal.classification']

    def run(self):
        """ Run the synchronization """
        record_ids = self.backend_adapter.search()
        _logger.info('search for magento tax classes returned %s', record_ids)
        for record_id in record_ids:
            self._import_record(record_id)


@magento
class TaxImporter(MagentoImporter):
    _model_name = ['magento.account.product.fiscal.classification']

    _base_mapper = TaxImportMapper


@job(default_channel='root.magento')
def tax_import_batch(session, model_name, backend_id):
    """ Import tax classes from Magento """
    env = get_environment(session, model_name, backend_id)
    importer = env.get_connector_unit(TaxBatchImporter)
    importer.run()



# @magento2000
# class ProductCategoryBatchImporter2000(DirectBatchImporter):
#     """ Only a full tree of categories can be retrieved. """
#     _model_name = ['magento.product.category']
#
#     def run(self, filters=None):
#         """ Run the synchronization """
#
#         env = get_environment(
#             self.session, self.model._name, self.backend_record.id)
#         importer = env.get_connector_unit(MagentoImporter)
#
#         tree = self.backend_adapter.search_read()
#
#         def import_branch(branch):
#             children = branch.pop('children_data', [])
#             importer.run(branch['id'], data=branch)
#             for child in children:
#                 import_branch(child)
#
#         import_branch(tree)
#
#
# @magento
# class ProductCategoryImporter(MagentoImporter):
#     _model_name = ['magento.product.category']
#
#     def _import_dependencies(self):
#         """ Import the dependencies for the record"""
#         record = self.magento_record
#         # import parent category
#         # the root category has a 0 parent_id
#         if record.get('parent_id'):
#             parent_id = record['parent_id']
#             if self.binder.to_openerp(parent_id) is None:
#                 importer = self.unit_for(MagentoImporter)
#                 importer.run(parent_id)
#
#     def _create(self, data):
#         openerp_binding = super(ProductCategoryImporter, self)._create(data)
#         checkpoint = self.unit_for(AddCheckpoint)
#         checkpoint.run(openerp_binding.id)
#         return openerp_binding
#
#     def _after_import(self, binding):
#         """ Hook called at the end of the import """
#         translation_importer = self.unit_for(TranslationImporter)
#         translation_importer.run(self.magento_id, binding.id)
#
#
