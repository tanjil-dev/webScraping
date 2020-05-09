from django.shortcuts import render
from django.views import View

from webscraper.services.webscrapingservice import WebScrapingService


class WebScrapingView(View):
    template_name = 'home.html'
    def get(self, request):
        obj = WebScrapingService
        t1 = obj.getTallykhata()
        t2 = obj.getDate()
        print(t1)
        print(t2)
        context = {
            'date': t2,
            'web': t1,
        }
        return render(request, template_name=self.template_name, context=context)