# Copyright 2026 Odoo Community Association (OCA)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestAccountMoveToReview(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.move = cls.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "partner_id": cls.env["res.partner"].create({"name": "Test"}).id,
            }
        )

    def test_to_review_default_false(self):
        self.assertFalse(self.move.to_review)

    def test_to_review_toggle(self):
        self.move.to_review = True
        self.assertTrue(self.move.to_review)