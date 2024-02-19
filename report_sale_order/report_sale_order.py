# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class ReportSaleOrder(models.TransientModel):
    _name = "report.sale.order"
    _description = "Wizard for report.sale.order"
    _inherit = "xlsx.report"

    # Search Criteria
    #partner_id = fields.Many2one("res.partner", string="Partner")
    taller_id = fields.Selection([
        ('2','Ñuble'),
        ('3','Par Vial')],string='Sucursal')
    # Report Result, sale.order
    results = fields.Many2many(
        "taller.ot.line",
        compute="_compute_results",
        help="Use compute fields, so there is nothing stored in database",
    )

    def _compute_results(self):
        """On the wizard, result will be computed and added to results line
        before export to excel, by using xlsx.export
        """
        self.ensure_one()
        Result = self.env["taller.ot.line"]
        domain = []
        if self.taller_id:
            domain += [("branch", "=", self.taller_id)]
        self.results = Result.search(domain)
