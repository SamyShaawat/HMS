{
    "name": "Hospital Managment System",
    "version": "17.0.1.0.0",
    "category": "Custom Apps",
    'summary': '',
    'description': 'Hospital Information System',
    "author": "Samy Mostafa Shaawat",
    "depends": [
        "base",
        "account",
        "website",
        "mail",
        "sale_management",
        "stock",
        "contacts",
        "web_enterprise",
        "account_accountant",
        "crm",
        "purchase",
        "web_studio",
        "web_enterprise"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/patient_views.xml",
        "views/patient_readonly_views.xml",
        "views/appointment_views.xml",
        "views/menus.xml"
    ],
    "installable": True,
    "application": True,
    'license': 'OEEL-1',
}
