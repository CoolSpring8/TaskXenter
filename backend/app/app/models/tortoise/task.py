from tortoise import fields
from tortoise.models import Model

class Task_DB(Model):
    name = fields.TextField(20)
    enabled = fields.BooleanField()
    method = fields.CharField(10)
    url = fields.TextField()
    data = fields.TextField(null=True)
    success_result = fields.TextField(null=True)
    user = fields.TextField()

    class Meta:
        table = "tasks"
