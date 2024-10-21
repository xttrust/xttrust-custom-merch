from django.shortcuts import render
from .models import FAQ


def faq_list(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
        'page_title': 'FAQs | xttrust Merch',
        'seo_description': 'Find answers to the most frequently asked questions at xttrust Merch.',
        'seo_keywords': 'FAQ, frequently asked questions, support, help',
    }
    return render(request, 'faq/faq_list.html', context)