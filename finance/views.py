from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request): 
        return render(request, self.template_name)