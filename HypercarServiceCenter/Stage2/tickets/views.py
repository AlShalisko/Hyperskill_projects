from django.views import View
from django.http.response import HttpResponse


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')
class MenuView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<a href="/get_ticket/change_oil">Change Oil</a><br><a href="/get_ticket/inflate_tires">Inflate tires</a><br><a href="/get_ticket/diagnostic">Diagnostic</a>')

