from django.shortcuts import render


# Create your views here.
class HomePageView(TemplateView):
template_name = 'pages/home.html'


class AboutUsView(TemplateView):
template_name = 'pages/about_us.html