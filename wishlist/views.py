from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Wishlist

@login_required
def wishlist_view(request):
    """
    A view to display the user's wishlist.

    Retrieves the wishlist associated with the currently logged-in user,
    creating one if it does not already exist. Then, renders the wishlist 
    template with the user's wishlist as context.
    """
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    # SEO metadata for the wishlist page
    seo_description = 'View and manage your wishlist at xttrust Merch. Save your favorite products for future purchases.'
    seo_keywords = 'wishlist, favorite products, xttrust Merch, save items, manage wishlist'

    context = {
        'wishlist': wishlist,
        'page_title': 'My Wishlist | xttrust Merch',
        'seo_description': seo_description,
        'seo_keywords': seo_keywords,
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    A view to add a product to the user's wishlist.

    The function fetches the product using the provided product_id.
    If the product is found, it adds it to the wishlist for the 
    logged-in user. If no wishlist exists for the user, it creates one.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(request, f'{product.name} has been added to your wishlist.')

    # Redirect back to the wishlist page with SEO metadata
    seo_description = f'Add {product.name} to your wishlist at xttrust Merch. \
            Save your favorite products for later.'
    seo_keywords = f'{product.name}, add to wishlist, xttrust Merch, save products'

    context = {
        'wishlist': wishlist,
        'page_title': f'{product.name} added to Wishlist | xttrust Merch',
        'seo_description': seo_description,
        'seo_keywords': seo_keywords,
    }
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    """
    A view to remove a product from the user's wishlist.

    The function fetches the product using the provided product_id. If the 
    product exists in the wishlist for the logged-in user, it is removed. 
    If the product is not in the wishlist, an info message is displayed. 
    Redirects the user back to the wishlist page after completion.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    # Check if the product is in the user's wishlist and remove it
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f'{product.name} has been removed from your wishlist.')
    else:
        messages.info(request, f'{product.name} was not in your wishlist.')

    # Redirect back to the wishlist page with SEO metadata
    seo_description = f'Remove {product.name} from your wishlist at xttrust Merch. Manage your saved products easily.'
    seo_keywords = f'{product.name}, remove from wishlist, xttrust Merch, manage wishlist'

    context = {
        'wishlist': wishlist,
        'page_title': f'{product.name} removed from Wishlist | xttrust Merch',
        'seo_description': seo_description,
        'seo_keywords': seo_keywords,
    }
    return redirect('wishlist')
