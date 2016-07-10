from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the portal index.")


def interaction_detail(request, interaction_id):
    return HttpResponse("You're looking at interaction %s." % interaction_id)


def rna_detail(request, rna_id):
    return HttpResponse("You're looking at RNA %s." % rna_id)


def rna_description(request, rna_id):
    return HttpResponse("You're looking at the description RNA %s." % rna_id)
