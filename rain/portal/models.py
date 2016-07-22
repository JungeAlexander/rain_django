from django.db import models


class Interaction(models.Model):
    views = models.IntegerField(default=0)
    INTERACTION_TYPES = (
        ('Co', 'Combined'),
        ('Cu', 'Curated'),
        ('Ex', 'Experiments'),
        ('Pr', 'Predictions'),
        ('Te', 'Textmining'),
    )
    type = models.CharField(max_length=2, choices=INTERACTION_TYPES, null=True)
    score = models.DecimalField(max_digits=6, decimal_places=5, null=True)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        interaction_str = ' - '.join(sorted([str(e) for e in self.entities.all()]))
        return 'Interaction {}: type {}, score {}'.format(interaction_str, str(self.type), str(self.score))

class Entity(models.Model):
    interactions = models.ManyToManyField(Interaction)
    identifier = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return self.identifier

    class Meta:
        abstract = True


class Protein(Entity):
    pass


class RNA(Entity):
    description = models.TextField()

    def is_mirna(self):
        return self.identifier.startswith('miRNA')

    is_mirna.admin_order_field = 'identifier'
    is_mirna.boolean = True
    is_mirna.short_description = 'Is a microRNA?'


class RNAalias(models.Model):
    rna = models.ForeignKey(RNA, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=128, unique=True)
    source = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return self.identifier

