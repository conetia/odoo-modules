# Copyright 2026 Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice To Review",
    "summary": "Add a to_review flag on invoices to highlight those requiring manual review",
    "version": "18.0.1.0.0",
    "development_status": "Beta",
    "maintainers": [],
    "category": "Accounting",
    "author": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-invoicing",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        "views/account_move_views.xml",
    ],
    "application": False,
    "installable": True,
}