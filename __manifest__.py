{
    "name": "Hospital Managment System",
    "version": "17.0.1.0.0",
    "category": "Custom Apps",
    'summary': '',
    'description': 'Hospital Information System',
    "author": "Samy Mostafa Shaawat",
    "depends": [
        "base",
        "website",
        "mail",
        "sale_management",
        "stock",
        "contacts",
        "web_enterprise",
        "account",
        "account_accountant",
        "crm",
        "purchase",
        "web_studio"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patient_view.xml"
    ],
    "installable": True,
    "application": True,
    'license': 'OEEL-1',
}
