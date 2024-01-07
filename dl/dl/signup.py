from flask import Flask, render_template
from flask.views import View

app = Flask(__name__)

class SignupView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('signup.html', active_page='signup')


