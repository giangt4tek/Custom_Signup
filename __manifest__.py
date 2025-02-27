{
    'name': 'Custom Signup Form',
    'version': '18.0',
    'category': 'Tutorial',
    'summary': 'Add custom fields to the website signup form',
    'description': 'This module adds a custom field to the website signup form.',
    'author': 'GinGa GX',
    'category': 'Website',
    'depends': ['auth_signup'],
    'data': [
              'views/auth_signup_template.xml'
            # 'models/res_partner.py',
            ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "license": "LGPL-3",
  
}