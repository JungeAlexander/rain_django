from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Interaction, RNA

# def index(request):
#     interactions = Interaction.objects.all()
#     output = '<br>'.join([str(i) for i in interactions])
#     return HttpResponse(output)

def index(request):
    entities = RNA.objects.order_by('-identifier')[:2]
    context = {
        'entity_list': entities,
    }
    return render(request, 'portal/index.html', context)


def interaction_detail(request, interaction_id):
    return HttpResponse("You're looking at interaction %s." % interaction_id)


def rna_detail(request, rna_id):
    try:
        rna = RNA.objects.get(pk=rna_id)
    except RNA.DoesNotExist:
        raise Http404("RNA does not exist")
    return render(request, 'portal/rna_detail.html', {'rna': rna})


def rna_description(request, rna_id):
    return HttpResponse("You're looking at the description RNA %s." % rna_id)
