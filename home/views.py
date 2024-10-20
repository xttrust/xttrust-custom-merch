from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    """ The view to return the homepage """

    context = {
        'page_title': 'xttrust Merch - Premium Apparel & Accessories for Your Unique Style', 
        'seo_description': 'Discover the latest collection of premium apparel and accessories at xttrust Merch. Custom t-shirts and hoodies to hats and streetwear.',
        'seo_keywords': 'xttrust, merch, fashion, accessories, streetwear, custom clothing, t-shirts, hoodies, hats, urban style, trendy outfits, online shopping',
    }

    return render(request, 'home/index.html', context)


def contact_view(request):
    """
    A view to handle contact form submissions.
    Saves the form data if valid, otherwise shows errors.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
    else:
        form = ContactForm()

    on_profile_page = True

    context = {
        'form': form,
        'on_profile_page': on_profile_page,
        'page_title': 'Contact Us | Your Site',
        'seo_description': 'Get in touch with us through our contact form.',
        'seo_keywords': 'contact, customer service, feedback, inquiry',
    }
    return render(request, 'home/contact.html', context)