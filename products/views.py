from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.utils.html import escape
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting, search queries, and pagination.
    Dynamically updates SEO meta information based on user actions.
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    seo_description = ('Browse our collection of high-quality products available at '
                       'xttrust Merch. Find the best apparel, accessories, and more!')
    seo_keywords = ['products', 'xttrust merch', 'apparel', 'accessories', 'online store']

    if request.GET:
        # Handle sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Filter by category if specified
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            category_names = ', '.join([cat.friendly_name for cat in categories])
            seo_description = f'Explore products in categories: {category_names} at xttrust Merch.'
            seo_keywords.extend([cat.name for cat in categories])

        # Handle search queries
        if 'q' in request.GET:
            query = escape(request.GET['q'])  # Escaping to prevent XSS attacks
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            seo_description = f'Search results for "{query}" at xttrust Merch.'
            seo_keywords.extend([query, 'search'])

    # Pagination logic
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    try:
        products_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        products_page = paginator.get_page(1)
    except EmptyPage:
        products_page = paginator.get_page(paginator.num_pages)

    # Current sorting for front-end display
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products_page,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'page_title': 'Products | xttrust Merch',
        'seo_description': seo_description,
        'seo_keywords': ', '.join(seo_keywords),
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'page_title': f'{product.name} - Buy Now | xttrust Merch',
        'seo_description': (f'Explore {product.name} at xttrust Merch. High-quality and trendy '
                            'products available for purchase. Shop now and elevate your style!'),
        'seo_keywords': (f'{product.name}, buy {product.name}, xttrust Merch, '
                         f'{product.category.friendly_name}, premium apparel, online store, '
                         'fashion, accessories'),
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    View to add a new product to the store. Only accessible by superusers.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Access restricted!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to add the product. Please make sure the form is valid.")
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'page_title': 'Products > Add new product | xttrust Merch',
        'seo_description': '',
        'seo_keywords': '',
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View to edit an existing product in the store. Only accessible by superusers.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Access restricted!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'page_title': f'Products > Edit product: {product.name} | xttrust Merch',
        'seo_description': '',
        'seo_keywords': '',
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    View to delete a product from the store. Only accessible by superusers.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Access restricted!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
