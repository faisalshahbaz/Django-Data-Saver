# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render , redirect
#from djangoDB.models import profile
from projectDB.models import Profile
from projectDB.form import NameForm
from django.http import HttpResponseRedirect


# Create your views here.
class HomePage(TemplateView):
    template_name = 'templatesviews/index.html'

    def get(self, request, *args, **kwargs):
        form = NameForm()
        posts = Profile.objects.all()
        # return redirect('index:index')
        form = NameForm()
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            phoneno = form.cleaned_data['phoneno']
            post = form.save(commit=False)
            #post.user = request.user
            post.save()
            form = NameForm()
            # return redirect ('index:index')

        args = {'form': form, 'name': name, 'city': city, 'country':country,'phoneno':phoneno}
        return render(request, self.template_name, args)
