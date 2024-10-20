from django.shortcuts import render

def index(request):
    """ The view to return the homepage """

    context = {
        'page_title': 'xttrust Merch - Premium Apparel & Accessories for Your Unique Style', 
        'seo_description': 'Discover the latest collection of premium apparel and accessories at xttrust Merch. Custom t-shirts and hoodies to hats and streetwear.',
        'seo_keywords': 'xttrust, merch, fashion, accessories, streetwear, custom clothing, t-shirts, hoodies, hats, urban style, trendy outfits, online shopping',
    }

    return render(request, 'home/index.html', context)