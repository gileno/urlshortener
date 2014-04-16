from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, View
from django.contrib import messages

from .forms import LinkForm
from .models import Link


class HomeView(CreateView):

    template_name = 'home.html'
    model = Link
    form_class = LinkForm

    def form_valid(self, form):
        link = form.save()
        messages.success(self.request, 'URL shortened with success: %s' % link.get_short_url())
        return redirect('home')


class RedirectLinkView(View):

    def get(self, request, slug):
        link = get_object_or_404(Link, slug=slug)
        link.views = link.views + 1
        link.save()
        return redirect(link.url)
