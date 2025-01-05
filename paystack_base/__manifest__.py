{
    'name': 'Paystack Payment Gateway',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'summary': 'Paystack Payment Gateway Integration for Odoo 17',
    'description': 'Paystack Payment Gateway Integration for Odoo 17, Paystack, payment gateway,Payment Gateway Integration,Paystack payment, odoo 17, odoo payment gateway',
    'author': 'Paystack',
    'company': 'Paystack',
    'website': 'https://paystack.com',
    'depends': ['base', 'payment'],
    'data': [
        'views/payment_acquirers_views.xml',
        'views/templates.xml',
        'data/data.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': True,

}



