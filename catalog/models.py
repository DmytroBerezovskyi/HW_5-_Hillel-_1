from django.db import models


class City(models.Model):  # noqa DJ10, DJ11
    name = models.CharField(max_length=200, help_text="Enter a city")
    state = models.CharField(max_length=200, help_text="Enter a state")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return "%s, %s" % (self.name, self.state)


class Product(models.Model):  # noqa DJ10, DJ11
    """
    Model representing a Product.
    """

    title = models.CharField(max_length=100)
    exp_date = models.DateField(null=True, blank=True)
    vendor_code = models.CharField(max_length=50)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f"({self.title}, {self.vendor_code})"


class Client(models.Model):  # noqa DJ10, DJ11
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True)
    # Foreign Key used because client can only have one city, but cities can have multiple clients
    product = models.ManyToManyField(Product, help_text="Select a product")
    # ManyToManyField used because client can contain many cities. Cities can cover many clients.
    # Product class has already been defined so we can specify the object above.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def display_product(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ", ".join([product.title for product in self.product.all()[:3]])

    display_product.short_description = "Product"


class Supplier(models.Model):  # noqa DJ10, DJ11
    city = models.OneToOneField("City", on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object
        """
        return "%s (%s)" % (self.city, self.title)
