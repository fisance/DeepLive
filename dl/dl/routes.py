from dl import app
from dl.models import HomeView
from dl.signup import SignupView
from dl.login import SignInView
from dl.pricing import PricingView
from dl.checkout import CheckoutInView


app.add_url_rule('/home', view_func=HomeView.as_view('home'))
app.add_url_rule('/signup', view_func=SignupView.as_view('signup'))
app.add_url_rule('/login', view_func=SignInView.as_view('login'))
app.add_url_rule('/pricing', view_func=PricingView.as_view('pricing'))
app.add_url_rule('/checkout', view_func=CheckoutInView.as_view('checkout'))