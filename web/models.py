from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = "web_category"
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["-id"]
        
    def __str__(self):
          return self.name
      

class Size(models.Model):
    name = models.IntegerField()
    
    
    class Meta:
        db_table = "web_siz"
        verbose_name = "siz"
        verbose_name_plural = "sizs"
        ordering = ["-id"]
        
    def __str__(self):
          return self.name

      
class Product(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField( max_length=255)
    image = models.ImageField( upload_to="product")
    created_on = models.DateTimeField( auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizs= models.ManyToManyField(Size, )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    class Meta:
        db_table = "web_product"
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["-id"]
        
    def __str__(self):
          return self.title
