from flask import render_template
from flask.views import View

class CheckoutInView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('checkout.html', active_page='checkout')