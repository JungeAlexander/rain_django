from django.http import HttpResponse
from .models import Interaction

def index(request):
    interactions = Interaction.objects.all()
    output = '<br>'.join([str(i) for i in interactions])
    return HttpResponse(output)


def interaction_detail(request, interaction_id):
    return HttpResponse("You're looking at interaction %s." % interaction_id)


def rna_detail(request, rna_id):
    return HttpResponse("You're looking at RNA %s." % rna_id)


def rna_description(request, rna_id):
    return HttpResponse("You're looking at the description RNA %s." % rna_id)
