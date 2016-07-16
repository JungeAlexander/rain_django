from django.db.models import F
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views import generic
from .models import Interaction, RNA, RNAalias


class IndexView(generic.ListView):
    template_name = 'portal/index.html'
    context_object_name = 'entity_list'

    def get_queryset(self):
        """Return the three RNAs appearing last in alphabetical order. However, do not show RNAs with
        an empty description."""
        return RNA.objects.exclude(description='').order_by('-identifier')[:3]


def interaction_detail(request, interaction_id):
    return HttpResponse("You're looking at interaction %s." % interaction_id)


class DetailView(generic.DetailView):
    model = RNA
    template_name = 'portal/rna_detail.html'

    def get_queryset(self):
        """
        Excludes any RNAs with no description.
        """
        return RNA.objects.exclude(description='')


def rna_description(request, rna_id):
    return HttpResponse("You're looking at the description RNA %s." % rna_id)


def vote(request, rna_id):
    rna = get_object_or_404(RNA, pk=rna_id)
    try:
        selected_choice = rna.rnaalias_set.get(pk=request.POST['choice'])
    except (KeyError, RNAalias.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'portal/rna_detail.html', {
            'rna': rna,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('portal:results', args=(rna.id,)))


class ResultsView(generic.DetailView):
    model = RNA
    template_name = 'portal/results.html'
