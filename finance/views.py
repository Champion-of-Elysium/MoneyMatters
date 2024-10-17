from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        user = request.user

        labels = list()
        data = list()

        queryset = Transaction.objects.filter(user=user, transaction_type="expense") \
            .values('category') \
            .annotate(total_outcome=Sum('amount')) \
            .order_by('-total_outcome')[:5]

        for transaction in queryset:
            labels.append(transaction['category'])
            data.append(transaction['total_outcome'])

        context = {
            'labels': labels,
            'data': data
        }

        return render(request, self.template_name, context)