from flask import render_template
from flask.views import MethodView



class PricingView(MethodView):
    pricing_plans = [
        {
            'name': 'Free',
            'price': '0/mo',
            'description': 'Get started with our free plan.',
            'offer': '100',
            'duration': '5 minutes per day',
        },
        {
            'name': 'Pro',
            'price': '5/mo',
            'description': 'Perfect for occasional users.',
            'offer': '500',
            'duration': '15 minutes per day',
        },
        {
            'name': 'Premium',
            'description': 'Best value for regular users.',
            'offer': '800',
            'duration': '30 minutes per day',
            'price': '10/mo',
        },
    ]

    def get(self):
        return render_template('pricing.html', pricing_plans=self.pricing_plans)