from django.db import models

# Create your models here.
class Dentists(models.Model):
    name=models.CharField(max_length=100, blank=False)
    cpf=models.CharField(max_length=11, blank=False, primary_key=True)
    cro=models.CharField(max_length=7, blank=False)
    email=models.EmailField(max_length=50, blank=False)
    phone=models.IntegerField(blank=False)
    password=models.CharField(max_length=50, blank=False)
    street=models.CharField(max_length=100, blank=False)
    number=models.IntegerField(blank=False)
    district=models.CharField(max_length=50, blank=False)
    city=models.CharField(max_length=50, blank=False)
    state=models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Drivers(models.Model):
    name=models.CharField(max_length=100, blank=False)
    cpf=models.CharField(max_length=11, blank=False, primary_key=True)
    cnh=models.ImageField(upload_to='src/cnh/', blank=True)
    crlv=models.ImageField(upload_to='src/crlv/', blank=True)
    email=models.EmailField(max_length=50, blank=False)
    phone=models.IntegerField(blank=False)
    password=models.CharField(max_length=50, blank=False)
    street=models.CharField(max_length=100, blank=False)
    number=models.IntegerField(blank=False)
    district=models.CharField(max_length=50, blank=False)
    city=models.CharField(max_length=50, blank=False)
    state=models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Labs (models.Model):
    name=models.CharField(max_length=100, blank=False)
    cnpj=models.CharField(max_length=11, blank=False, primary_key=True)
    insc_cfo=models.IntegerField(blank=False)
    email=models.EmailField(max_length=50, blank=False)
    phone=models.IntegerField(blank=False)
    password=models.CharField(max_length=50, blank=False)
    street=models.CharField(max_length=100, blank=False)
    number=models.IntegerField(blank=False)
    district=models.CharField(max_length=50, blank=False)
    city=models.CharField(max_length=50, blank=False)
    state=models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=100, blank=False)
    lab=models.ForeignKey('Labs', on_delete=models.CASCADE)
    description=models.TextField(max_length=1000, blank=False, null=True)
    value=models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    production=models.IntegerField(blank=False)

    def __str__(self):
        return str('%s/%s' %(self.name, self.lab.name))

class Orders(models.Model):
    

    id_product=models.ForeignKey('Products', on_delete=models.CASCADE)
    dentist=models.ForeignKey('Dentists', on_delete=models.CASCADE)
    #lab=models.ForeignKey('Products', on_delete=models.CASCADE)
    #value=models.ForeignKey('Products', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class Transports(models.Model):
    id_order=models.ForeignKey('Orders', on_delete=models.CASCADE)
    cpf_driver=models.ForeignKey('Drivers', on_delete=models.CASCADE)
    #city_lab=models.ForeignKey('Orders', on_delete=models.CASCADE)
    #city_dentist=models.ForeignKey('Orders', on_delete=models.CASCADE)
    value=models.IntegerField(blank=False)
    estimated_time=models.IntegerField(blank=False)
    
    def __str__(self):
        return str(self.id)
    
  