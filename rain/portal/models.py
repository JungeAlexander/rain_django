from django.db import models


# TODO allow to add proteins - introduce super-class Entity an then RNA and Protein inherit from Entity?
# TODO abstract classes should be useful: https://docs.djangoproject.com/en/1.9/topics/db/models/#model-inheritance
class Entity(models.Model):
    identifier = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)

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
    entities = models.ManyToManyField(RNA, through='InteractionInfo')
    views = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return ' - '.join(sorted([str(e) for e in self.entities.all()]))


class InteractionInfo(models.Model):
    interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    INTERACTION_TYPES = (
        ('Co', 'Combined'),
        ('Cu', 'Curated'),
        ('Ex', 'Experiments'),
        ('Pr', 'Predictions'),
        ('Te', 'Textmining'),
    )
    type = models.CharField(max_length=2, choices=INTERACTION_TYPES)
    score = models.DecimalField(max_digits=6, decimal_places=5)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return 'Interaction {}: type {}, score {}'.format(str(self.interaction), str(self.type), str(self.score))
