# -*- coding: utf-8 -*-
{
    'name': "Chic Corner Customisations",
    'description': "Chic Corner Customisations",
    'summary': "",
    'author': 'ST',
    'category': 'base',
    'version': '1.0',
    'depends': ['base', 'product', 'account', 'stock', 'sale', 'purchase', 'sale_stock', 'purchase_stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/custome_paper_format.xml',
        'views/stock_quant_view.xml',
        'views/transaction_report.xml',
        'views/transaction_session.xml',
        'views/purchase_order_view.xml',
        'report/products_with_ecart.xml',
        'report/transaction_report.xml',
        'report/bon_sortie_report.xml',
        'report/bon_sortie_template.xml',
        'report/bon_sortie_template_print.xml',
        'report/sale_report.xml',
        'views/api_key_views.xml',
        'views/product_view.xml',
        'report/report_product_label.xml',
        'report/purchase_order_inherit.xml',
        'views/pos_order_vendor.xml',
        'views/transaction_menu.xml',
        'views/stan_order.xml',
        'views/pos_payment_screen.xml',
        'views/product_viewinherit.xml',
        'views/report_template.xml',
        #'views/pos_payment_stan_view.xml',
        #'report/print_accounting.xml',
        #'views/pos_payment_methode.xml',
        #'views/account_journal.xml',
        #'views/pos_payment_stan.xml',
        #'report/print_header.xml',
        # 'views/point_of_sale_receipt.xml',
        # 'report/report_view.xml'
    ],
    #'assets': {
     #   'point_of_sale._assets_pos': [
      #      'chichcorner_customization/static/src/**/*',
       # ],
    #},
    'assets': {
        'web.assets_backend': [
            'chichcorner_customization/static/src/models/barcode_picking_model.js',
        ],
        'point_of_sale._assets_pos': [
            'chichcorner_customization/static/src/app/**/*',
        ],
        'web.report_assets_common': [
            'chichcorner_customization/static/src/css/report.css',
            'chichcorner_customization/static/src/css/bonsortie.css',
        ],
    },
    'demo': [],
}
