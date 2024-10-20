from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ 
    A view that renders the bag contents page with SEO metadata.
    """
    context = {
        'page_title': 'Your Shopping Bag | xttrust Merch',
        'seo_description': 'View the items in your shopping bag at xttrust Merch. Review your selected products before proceeding to checkout.',
        'seo_keywords': 'shopping bag, cart, xttrust Merch, review order, checkout',
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ 
    Add a quantity of the specified product to the shopping bag.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    # SEO Metadata for adding to the bag
    context = {
        'page_title': f'Added {product.name} to Your Bag | xttrust Merch',
        'seo_description': f'You have added {product.name} to your shopping bag. Continue shopping or proceed to checkout at xttrust Merch.',
        'seo_keywords': f'{product.name}, shopping bag, xttrust Merch, cart, add to bag',
    }

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ 
    Adjust the quantity of the specified product to the specified amount.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag

    # SEO Metadata for adjusting the bag
    context = {
        'page_title': f'Updated {product.name} Quantity | xttrust Merch',
        'seo_description': f'Update the quantity of {product.name} in your shopping bag at xttrust Merch.',
        'seo_keywords': f'update quantity, {product.name}, shopping bag, xttrust Merch, cart',
    }

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ 
    Remove the item from the shopping bag.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag

        # SEO Metadata for removing from the bag
        context = {
            'page_title': f'Removed {product.name} from Your Bag | xttrust Merch',
            'seo_description': f'{product.name} has been removed from your shopping bag at xttrust Merch. Continue browsing our products.',
            'seo_keywords': f'remove item, {product.name}, shopping bag, xttrust Merch, cart',
        }

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
