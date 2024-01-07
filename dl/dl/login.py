from flask import Flask, render_template
from flask.views import View

app = Flask(__name__)

class SignInView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('login.html', active_page='login')

