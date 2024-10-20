# reviews/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_reviews, name='product_reviews'),
    path('add/<int:product_id>/', views.add_review, name='add_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
