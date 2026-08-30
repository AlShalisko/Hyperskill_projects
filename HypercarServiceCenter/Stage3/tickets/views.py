from django.views import View
from django.http.response import HttpResponse
from collections import deque

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')
class MenuView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<a href="/get_ticket/change_oil">Change Oil</a><br><a href="/get_ticket/inflate_tires">Inflate tires</a><br><a href="/get_ticket/diagnostic">Diagnostic</a>')

ticket_number = 0

oil_queue = 0
tires_queue = 0
diagnostic_queue = 0

class OilView(View):
    def get(self, request, *args, **kwargs):
        global ticket_number, oil_queue

        ticket_number += 1

        minutes_to_wait = oil_queue * 2
        oil_queue += 1

        return HttpResponse(
            f'<div>Your number is {ticket_number}</div>'
            f'<div>Please wait around {minutes_to_wait} minutes</div>'
        )

class TiresView(View):
    def get(self, request, *args, **kwargs):
        global ticket_number, oil_queue, tires_queue

        ticket_number += 1

        minutes_to_wait = oil_queue * 2 + tires_queue * 5
        tires_queue += 1

        return HttpResponse(
            f'<div>Your number is {ticket_number}</div>'
            f'<div>Please wait around {minutes_to_wait} minutes</div>'
        )
class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        global ticket_number, oil_queue, tires_queue, diagnostic_queue

        ticket_number += 1

        minutes_to_wait = (
            oil_queue * 2
            + tires_queue * 5
            + diagnostic_queue * 30
        )

        diagnostic_queue += 1

        return HttpResponse(
            f'<div>Your number is {ticket_number}</div>'
            f'<div>Please wait around {minutes_to_wait} minutes</div>'
        )