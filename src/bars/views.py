from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import BarsCreateForm, BarsLocationCreateForm
from .models import BarsLocation
# Create your views here.

# function based view
# def home(request):
#     return HttpResponse("hello")
#     return render(request, "home.html", {})#response

# python html string, f string for python > 3.6
# def home_old(request):
#     html_var = 'f strings'
#     num = random.randint(0, 1000000)
#     html_ = f""" <!DOCTYPE html>
#     <html lang=en>
#     <head></head>
#     <body>
#     <h1>Hello World!</h1>
#     <p>This is {html_var} coming through</p>
#     <p>This is {num} coming through</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)

# render html, function-based view
# def home(request):
#     num = None
#     some_list = [random.randint(0, 10000000), random.randint(0, 10000000), random.randint(0, 10000000)]
#     conditional_bool_item = True
#     if conditional_bool_item:
#         num = random.randint(0, 1000000)
#     context = {
#         "bool_item": False,
#         "num": num,
#         "some_list": some_list
#     }
#     return render(request, "home.html", context)

# class-based view
# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)


@login_required(login_url='/login/')
# function based view
def bars_createview(request):
    form = BarsLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect("/bars/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors

    template_name = 'bars/form.html'
    context = {"form":form, "errors":errors}
    return render(request, template_name, context)

def bars_listview(request):
    template_name = 'bars/bars_list.html'
    queryset = BarsLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def bars_detailview(request, slug):
    template_name = 'bars/barslocation_detail.html'
    obj = BarsLocation.objects.get(slug=slug)
    context = {
        "object": obj
    }
    return render(request, template_name, context)




class BarListView(ListView):
    template_name = 'bars/bars_list.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = BarsLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = BarsLocation.objects.all()
        return queryset

class BarDetailView(DetailView):
    queryset = BarsLocation.objects.all()   # .filter(category__iexact='asain')
    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(BarDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
    # def get_object(self, *args, **kwargs):
    #     bar_id = self.kwargs.get('bar_id')
    #     obj = get_object_or_404(BarsLocation, id = bar_id) # pk = bar_id
    #     return obj

class BarsCreateView(LoginRequiredMixin, CreateView):
    form_class = BarsLocationCreateForm
    login_url = '/login/'
    template_name = 'bars/form.html'
    success_url = '/bars/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = request.user
        return super(BarsCreateView, self).form_valid(form)
