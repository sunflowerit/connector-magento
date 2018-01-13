# -*- coding: utf-8 -*-
{
    'name': 'Magento Connector - Taxes',
    'version': '2.0.0',
    'category': 'Connector',
    'depends': [
        'magentoerpconnect',
        'account_product_fiscal_classification',
    ],
    'author': "Sunflower IT",
    'license': 'AGPL-3',
    'website': 'http://www.odoo-magento-connector.com',
    'summary': """Magento Connector - Product Tax Classes""",
    'images': [],
    'demo': [],
    'data': [
        'views/magento_backend.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
 }
