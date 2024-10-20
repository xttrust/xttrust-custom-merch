from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

@login_required
def profile(request):
    """
    Display the user's profile and handle profile updates.
    
    Allows logged-in users to view and update their profile details. 
    Also displays the user's past orders.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, "Update failed. Please make sure the form is valid.")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'page_title': 'My Profile | xttrust Merch',
        'seo_description': 'View and update your profile details, and track your past orders at xttrust Merch.',
        'seo_keywords': 'user profile, order history, account settings, xttrust Merch',
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display a past order confirmation.
    
    Allows users to view their past order details by order number.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'page_title': f'Order {order_number} History | xttrust Merch',
        'seo_description': f'View past order details for order number {order_number} at xttrust Merch.',
        'seo_keywords': f'order {order_number}, order history, purchase details, xttrust Merch',
    }

    return render(request, template, context)
