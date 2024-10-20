# views.py in the reviews app

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm

def product_reviews(request, product_id):
    """ View to display all reviews for a product """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    star_range = range(1, 6)

    # Check if the logged-in user has a review for this product
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    context = {
        'product': product,
        'reviews': reviews,
        'user_review': user_review,
        'star_range': star_range,
    }

    return render(request, 'reviews/reviews.html', context)


@login_required
def add_review(request, product_id):
    """ View to add a new review for a product """
    product = get_object_or_404(Product, pk=product_id)

    # Check if the user has already reviewed this product
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    if existing_review:
        messages.error(request, 'You have already reviewed this product.')
        return redirect('product_reviews', product_id=product.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('product_reviews', product_id=product.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})


@login_required
def delete_review(request, review_id):
    """ View to allow a user to delete their review """
    review = get_object_or_404(Review, pk=review_id)

    # Ensure the logged-in user is the owner of the review
    if review.user != request.user:
        messages.error(request, 'You are not authorized to delete this review.')
        return redirect('product_reviews', product_id=review.product.id)

    # If POST request, delete the review
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        return redirect('product_reviews', product_id=review.product.id)

    # If GET request, show confirmation page
    return render(request, 'reviews/confirm_delete.html', {'review': review})
