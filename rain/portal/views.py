from django.http import HttpResponse
from django.template import loader
from .models import Interaction, RNA

# def index(request):
#     interactions = Interaction.objects.all()
#     output = '<br>'.join([str(i) for i in interactions])
#     return HttpResponse(output)

def index(request):
    entities = RNA.objects.order_by('identifier')[:2]
    template = loader.get_template('portal/index.html')
    context = {
        'entity_list': entities,
    }
    return HttpResponse(template.render(context, request))


def interaction_detail(request, interaction_id):
    return HttpResponse("You're looking at interaction %s." % interaction_id)


def rna_detail(request, rna_id):
    return HttpResponse("You're looking at RNA %s." % rna_id)


def rna_description(request, rna_id):
    return HttpResponse("You're looking at the description RNA %s." % rna_id)
