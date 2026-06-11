# Copyright 2026 Conetia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice Tag",
    "summary": "Add custom tags to customer and vendor invoices",
    "version": "18.0.1.0.0",
    "development_status": "Beta",
    "maintainers": [],
    "category": "Accounting",
    "author": "Conetia",
    "website": "https://conetia.com",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/account_invoice_tag_views.xml",
        "views/account_move_views.xml",
    ],
    "application": False,
    "installable": True,
}
