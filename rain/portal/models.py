from django.db import models


# TODO allow to add proteins - introduce super-class Entity an then RNA and Protein inherit from Entity?
class RNA(models.Model):
    identifier = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    views = models.IntegerField(default=0)

    def is_mirna(self):
        return self.identifier.startswith('miRNA')

    is_mirna.admin_order_field = 'identifier'
    is_mirna.boolean = True
    is_mirna.short_description = 'Is a microRNA?'

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return self.identifier


class RNAalias(models.Model):
    rna = models.ForeignKey(RNA, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=128, unique=True)
    source = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return self.identifier


class Interaction(models.Model):
    entity1 = models.ForeignKey(RNA, on_delete=models.CASCADE, related_name='entity1')
    entity2 = models.ForeignKey(RNA, on_delete=models.CASCADE, related_name='entity2')
    views = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return str(self.entity1) + '-' + str(self.entity2)
