# Copyright 2026 Conetia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice custom proforma view",
    "summary": "Shows bank account in proforma documents (invoices with draft state)",
    "version": "18.0.1.0.0",
    "development_status": "Beta",
    "maintainers": ["javiermatos"],
    "category": "Accounting/Localizations",
    "author": "Conetia",
    "website": "https://conetia.com",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        "views/report_invoice_document_proforma_bank.xml",
    ],
    "application": False,
    "installable": True,
}
