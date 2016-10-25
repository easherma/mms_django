from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Prompt, Response

class IndexView(generic.ListView):
    template_name = 'stories/index.html'
    context_object_name = 'output'

    def get_queryset(self):
        """Return a list of stories."""
        return Response.objects

class DetailView(generic.DetailView):
    model = Response
    template_name = 'stories/detail.html'

class ResultsView(generic.DetailView):
    model = Response
    template_name = 'stories/results.html'


# def index(request):
#     return HttpResponse("check out this siick index")
#
# def prompts(request, prompt_id):
#     prompt_list = Prompt.objects.all()
#     output = ', '.join([p.prompt_text for p in prompt_list])
#     return HttpResponse("Available Prompts: %s" % output)
#
# def prompt_detail(request, prompt_id):
#     prompt = get_object_or_404(Prompt, pk=prompt_id)
#     return render(request, 'stories/detail.html', {'prompt': prompt})
#
# def results(request, prompt_id):
#     results_list = Response.objects.all()
#     #output = ', '.join([p.response_text for p in results_list])
#     output = Response.objects.all()
#     context = {'output': output}
#     return render(request, 'stories/index.html', context)
#
# def result_detail(request, prompt_id):
#     result = get_object_or_404(Response, pk=response_id)
#     return render(request, 'stories/detail.html', {'prompt': result})
#
def count(request, prompt_id):
    count = Response.objects.all()
    output = ', '.join([str(p.count) for p in count])
    return HttpResponse("Number of entries: %s" % output)
