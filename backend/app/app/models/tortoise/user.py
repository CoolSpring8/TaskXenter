from tortoise import fields
from tortoise.models import Model

class User_DB(Model):
    username = fields.CharField(20)
    hashed_password = fields.TextField()

    class Meta:
        table = "users"
