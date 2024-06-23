from django.db import models

class Product(models.Model):
    condition = models.CharField(max_length=255, default='new')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    brand = models.ForeignKey('store.Brand', on_delete=models.CASCADE, default=None, null=True)
    image = models.ImageField(upload_to='products/images/', default=None, null=True)
    category = models.ForeignKey('store.SubCategory', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=255)
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    description = models.TextField(default='')
    rating = models.FloatField(default=0.0)
    color_of = models.CharField(max_length=255, default='')
    color = models.TextField(default='')
    characteristics_principal = models.TextField(default='')
    characteristics_other = models.TextField(default='')
    deliverFree = models.BooleanField(default=False)
    deliverPrice = models.FloatField(default=0.0)
    deliverAtAll = models.BooleanField(default=False)
    kg = models.FloatField(default=0.0)
    dimentions = models.TextField(default='')
    discount = models.IntegerField(default=0)
    sku = models.CharField(max_length=255, default='')
    paused = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Doubt(models.Model):
    customer = models.ForeignKey('store.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    doubt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
    
class Answer(models.Model):
    question = models.ForeignKey('store.Doubt', on_delete=models.CASCADE)
    answer = models.TextField()
    customer = models.ForeignKey('store.Customer', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
    


class ProductMedia(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')
    video = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.product
    
class Opinion(models.Model):
    customer = models.ForeignKey('store.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    opinion = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='opinions/images/', default=None, null=True)

    def __str__(self):
        return self.product


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brands/images/')

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255)
    sales_Success = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to='store/logo/')
    description = models.TextField(default='')
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        if self.store is None:
            return f"{self.name} - {self.email}"
        else: 
            return f"{self.name} - {self.email} - {self.store}"
        

class Favorite(models.Model):
    customer = models.ForeignKey('store.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} - {self.product}"
        

class Order(models.Model):
    customer = models.ForeignKey('store.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} - {self.product} - {self.quantity}"
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name