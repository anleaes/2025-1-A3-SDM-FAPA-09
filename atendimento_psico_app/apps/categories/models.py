from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'
        ordering =['id']

    def str(self):
        return self.name