from django.views import View
from django.http.response import HttpResponse
from collections import deque
from django.middleware.csrf import get_token
from django.shortcuts import redirect

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')
class MenuView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<a href="/get_ticket/change_oil">Change Oil</a><br><a href="/get_ticket/inflate_tires">Inflate tires</a><br><a href="/get_ticket/diagnostic">Diagnostic</a>')

class OperatorView(View):
    def get(self, request, *args, **kwargs):
        csrf_token = get_token(request)

        return HttpResponse(f'''<div>Change oil queue: {len(oil_tickets)}</div>
<div>Inflate tires queue: {len(tires_tickets)}</div>
<div>Get diagnostic queue: {len(diagnostic_tickets)}</div>

<form method="post">  
<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
  <button type="submit">Process next</button>
</form>''')

    def post(self, request, *args, **kwargs):
        global oil_tickets, tires_tickets, diagnostic_tickets, current_ticket

        if oil_tickets:
            current_ticket = oil_tickets.pop(0)
        elif tires_tickets:
            current_ticket = tires_tickets.pop(0)
        elif diagnostic_tickets:
            current_ticket = diagnostic_tickets.pop(0)

        return redirect('/processing')



ticket_number = 0
current_ticket = None
oil_tickets = []
tires_tickets = []
diagnostic_tickets = []

class NextView(View):
    def get(self, request, *args, **kwargs):
        global oil_tickets, tires_tickets, diagnostic_tickets, current_ticket
        if current_ticket is None:
            return HttpResponse('<div>Waiting for the next client</div>')
        else:
            return HttpResponse(f'<div>Ticket #{current_ticket}</div>')
class OilView(View):
    def get(self, request, *args, **kwargs):
        global ticket_number, oil_tickets

        ticket_number += 1

        minutes_to_wait = (
            len(oil_tickets) * 2
        )

        oil_tickets.append(ticket_number)

        return HttpResponse(
            f'<div>Your number is {ticket_number}</div>'
            f'<div>Please wait around {minutes_to_wait} minutes</div>'
        )

class TiresView(View):
    def get(self, request, *args, **kwargs):
        global ticket_number, oil_tickets, tires_tickets

        ticket_number += 1

        minutes_to_wait = (
            len(oil_tickets) * 2
            + len(tires_tickets) * 5
        )

        tires_tickets.append(ticket_number)

        return HttpResponse(
            f'<div>Your number is {ticket_number}</div>'
            f'<div>Please wait around {minutes_to_wait} minutes</div>'
        )
class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        global ticket_number, oil_tickets, tires_tickets, diagnostic_tickets

        ticket_number += 1

        minutes_to_wait = (
            len(oil_tickets) * 2
            + (len(tires_tickets)) * 5
            + len(diagnostic_tickets) * 30
        )

        diagnostic_tickets.append(ticket_number)

        return HttpResponse(
            f'<div>Your number is {ticket_number}</div>'
            f'<div>Please wait around {minutes_to_wait} minutes</div>'
        )