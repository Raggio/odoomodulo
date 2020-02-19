from openerp import models, fields, api
class DevRequest(models.Model):
    _name = 'dev.request'
    dreqid = fields.Id('Id')
    name = fields.Char('Titulo', required=True)
    description = fields.Char('Descripcion', required=True)
    active = fields.Boolean('Active?', default=True)
    date_creation= fields.Date('Solicitado')
    date_release = fields.Date('Entrega')
    client_id = fields.Many2one('res.partner','Cliente')
    task_ids = fields.One2many('dev.request.task','devreq_id')

class DevTask(models.Model):
       _name = 'dev.request.task' 
       name = fields.Char('Descripcion', required=True)
       devreq_id = fields.Many2one('dev.request','Request',ondelete='cascade')
       id_done = fields.Boolean('Done?',default=False)
       user_id = fields.Many2one('res.users','Responsible')
       date_deadline = fields.Date('Deadline')
       horas = fields.Integer('Horas')
       priority = fields.Selection([
                                    ('0','Low'),
                                    ('1','Normal'),
                                    ('2','High')],
                                    'Priority',default='1')
       kanban_state = fields.Selection([
                                        ('normal', 'In Progress'),
                                        ('blocked', 'Blocked'),
                                        ('done', 'Ready for next stage')],
                                        'Kanban State', default='normal')