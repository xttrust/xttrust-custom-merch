from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm

def product_reviews(request, product_id):
    """ 
    View to display all reviews for a product.
    
    Retrieves all reviews associated with a specific product and checks if the logged-in 
    user has already submitted a review for that product. Adds SEO metadata dynamically.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    star_range = range(1, 6)

    # Check if the logged-in user has a review for this product
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    # SEO metadata for the reviews page
    seo_description = f'Read customer reviews for {product.name} on xttrust Merch. See what others think about this product.'
    seo_keywords = f'{product.name}, reviews, customer feedback, product reviews, xttrust Merch'

    context = {
        'product': product,
        'reviews': reviews,
        'user_review': user_review,
        'star_range': star_range,
        'page_title': f'Reviews for {product.name} | xttrust Merch',
        'seo_description': seo_description,
        'seo_keywords': seo_keywords,
    }

    return render(request, 'reviews/reviews.html', context)


@login_required
def add_review(request, product_id):
    """ 
    View to add a new review for a product.
    
    Allows a user to submit a review for a product if they haven't already done so. 
    Validates the review form and saves it if valid, then redirects the user to the reviews page.
    """
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

    # SEO metadata for the add review page
    seo_description = f'Add your review for {product.name} on xttrust Merch. Share your experience and feedback with other customers.'
    seo_keywords = f'{product.name}, add review, customer feedback, xttrust Merch, product review'

    context = {
        'form': form,
        'product': product,
        'page_title': f'Add Review for {product.name} | xttrust Merch',
        'seo_description': seo_description,
        'seo_keywords': seo_keywords,
    }

    return render(request, 'reviews/add_review.html', context)


@login_required
def delete_review(request, review_id):
    """ 
    View to allow a user to delete their review.
    
    The function ensures that only the owner of the review can delete it. 
    If the user is authorized, they can confirm the deletion.
    """
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

    # SEO metadata for the delete review confirmation page
    seo_description = f'Delete your review for {review.product.name} on xttrust Merch. Confirm if you want to remove your feedback.'
    seo_keywords = f'delete review, {review.product.name}, xttrust Merch, product feedback, manage review'

    context = {
        'review': review,
        'page_title': f'Delete Review for {review.product.name} | xttrust Merch',
        'seo_description': seo_description,
        'seo_keywords': seo_keywords,
    }

    # If GET request, show confirmation page
    return render(request, 'reviews/confirm_delete.html', context)
