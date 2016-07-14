from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Interaction, RNA, RNAalias

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
    rna = get_object_or_404(RNA, pk=rna_id)
    return render(request, 'portal/rna_detail.html', {'rna': rna})


def rna_description(request, rna_id):
    return HttpResponse("You're looking at the description RNA %s." % rna_id)


def vote(request, rna_id):
    rna = get_object_or_404(RNAalias, pk=rna_id)
    try:
        selected_choice = rna.rnaalias_set.get(pk=request.POST['choice'])
    except (KeyError, RNAalias.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'portal/rna_detail.html', {
            'rna': rna,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('portal:results', args=(rna.id,)))


def results(request, rna_id):
    rna = get_object_or_404(RNA, pk=rna_id)
    return render(request, 'polls/results.html', {'rna': rna})