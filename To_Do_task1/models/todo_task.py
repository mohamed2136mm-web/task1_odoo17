from odoo import models,fields,api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
     _name='todo.task'
     _inherit = ['mail.thread','mail.activity.mixin']
     _description = 'Todo Management'

     name = fields.Char(string='Task Name',required=True)
     assign_to_ids = fields.Many2one('res.partner',string='Assign To',required=True,tracking=True)
     description = fields.Char(string='Description',required=True)
     due_date = fields.Date(string='Due Date',required=True,tracking=True)
     status = fields.Selection([
         ('new','New'),
         ('in_progress','In Progress'),
         ('completed','Completed'),
     ],string='status',required=True)

     state = fields.Selection([
         ('draft', 'Draft'),
         ('pending', 'Pending'),
         ('sold', 'Sold'),
     ],default='draft')

     def action_draft(self):
         for rec in self:
             rec.state = 'draft'
     def action_pending(self):
         for rec in self:
             rec.state = 'pending'
     def action_sold(self):
         for rec in self:
             rec.state = 'sold'


     _sql_constraints = [
         ('unique_name','unique("name")','please enter a unique name'),
     ]

     @api.constrains('name')
     def _check_name_greater_zero(self):
         for rec in self:
             if rec.name == 0:
                 raise ValidationError('Please enter a valid name')

     @api.model_create_multi
     def create(self,vals):
         res = super(TodoTask,self).create(vals)
         print('create good')
         return res

     @api.model
     def _search(self,domain, offset=0, limit=None, order=None, access_rights_uid=None):
         res = super(TodoTask,self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
         print('search good')
         return res

     def write(self,vals):
         res = super(TodoTask,self).write(vals)
         print('write good')
         return res

     def unlink(self):
         res = super(TodoTask,self).unlink()
         print('unlink good')
         return res