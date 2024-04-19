from django.db import models

# Create your models here.


class DedicateServer(models.Model):
    server_zip = models.FileField(verbose_name="dedicate server", upload_to="server")

    def __str__(self):
        return "server"