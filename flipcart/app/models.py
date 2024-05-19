from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

STATE_CHOICE = (
    ('Andaman & Nincobar Island','Andaman & Nincobar Island' ),
    ('Andhra Pradesh','Andhra Pradesh' ),
    ('Assam','Assam' ),
    ('Bihar','Bihar' ),
    ('Chandigarh','Chandigarh' ),
    ('Chhatisgarh','Chhatisgarh' ),
    ('Dadar & Nagar Haveli','Dadar & Nagar Haveli' ),
    ('Daman & Diu','Daman & Diu' ),
    ('Delhi','Delhi' ),
    ('Goa','Goa' ),
    ('Gujarat','Gujarat' ),
    ('Haryana','Haryana' ),
    ('Himachal Pradesh','Himachal Pradesh' ),
    ('Jammu & Kashmir','Jammu & Kashmir' ),
    ('Jharkhand','Jharkhand' ),
    ('Karnataka','Karnataka' ),
    ('Kerala','kerala' ),
    ('Lakshdweep','Lakshdweep' ),
    ('Madhya Pradesh','Madhya Pradesh' ),
    ('Mahrarstra','Mahrarstra' ),
    ('Manipur','Manipur' ),
    ('Meghalya','Meghalya' ),
    ('Mizoram','Mizoram' ),
    ('Nagaland','Nagaland' ),
    ('Odisha','Odisha' ),
    ('Punduchery','Punduchery' ),
    ('Punjab','Punjab' ),
    ('Rajsathan','Rajsathan' ),
    ('Sikkim','Sikkim' ),
    ('Tamil Nadu','Tamil Nadu' ),
    ('Telengana','Telengana' ),
    ('Tripura','Tripura' ),
    ('Utter Pradesh','Utter Pradesh' ),
    ('West Bengal','West Bengal' ),

)

CATEGORY_CHOICE = (
    ('M', "Mobile"),
    ('L', "Laptop"),
    ('TW', "Top Wear"),
    ('BW', "Bottom Wear"),
)

# Customer database
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)

    def __str__(self) -> str:
        return str(self.id)
    
# Product database
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(max_length=10)
    discount_price = models.FloatField(max_length=102)
    description = models.TextField(max_length=150)
    brand = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2 ,default='TW')
    product_image = models.ImageField(upload_to='Productimg')

    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quanlity = models.PositiveBigIntegerField(default=1)

    def __str__(self) :
        return str(self.id)
    

STATUS_CHOICE = (
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("On The Way", "On The Way"),
    ("Deliverd", "Deliverd"),
    ("Cancel", "Cancel"),
)



class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATE_CHOICE, default='Pending')

    def __str__(self) :
        return str(self.id)