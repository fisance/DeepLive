from flask import render_template
from flask.views import MethodView

class HomeView(MethodView):
    def get(self):
        # Your home page logic here
        return render_template('home.html')