# -*- coding: utf-8 -*-
{
    'name': "repostary_card",

    'summary': """
        welcome in the repostary_card apps this app maked to help the people
        to enhance their live by give them some money
        """,

    'description': """
      in this app the admin add some beneficiary with their information 
      and can edit and delete the information of any beneficiary also
      the beneficiary can see other beneficiaries and can edit and delete 
      his information
    """,

    'author': "Mohammed almaqdy",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/securityrules.xml',
        'security/ir.model.access.csv',
        'data/gen_seq.xml',
        'data/expireddate.xml',
        
        # 'data/new_req.xml',
        # 'data/update_req.xml',
        'views/card.xml',
        'views/newrequest.xml',
        'views/updaterequest.xml', 
        'views/emails.xml',        
    ],
    'demo': [
        'demo/demo.xml',
    ],
}