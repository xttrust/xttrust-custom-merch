from django.db import models

class Category(models.Model):
    """
    The Category model represents product categories for the e-commerce store.
    Each category has a `name` (used for internal reference) and a `friendly_name`
    (a more human-readable name for display purposes).
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the category if it exists.
        """
        return self.friendly_name


class Product(models.Model):
    """
    The Product model represents individual products available in the e-commerce store.
    Each product is related to a category and includes fields such as SKU, name, description,
    price, rating, and image (both URL and file).
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="ForeignKey to Category, allowing each product to belong to one category."
    )
    sku = models.CharField(
        max_length=254, null=True, blank=True,
        help_text="Stock Keeping Unit (SKU) used to uniquely identify the product."
    )
    name = models.CharField(
        max_length=254, help_text="Name of the product."
    )
    description = models.TextField(
        help_text="Detailed description of the product."
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="Price of the product."
    )
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True,
        help_text="Customer rating for the product, if available."
    )
    image_url = models.URLField(
        max_length=1024, null=True, blank=True,
        help_text="URL for the product image if hosted externally."
    )
    image = models.ImageField(
        null=True, blank=True, help_text="Upload an image for the product."
    )

    def __str__(self):
        return self.name
        