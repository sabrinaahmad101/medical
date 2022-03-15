from django.db import models

# Create your models here.




class booking1(models.Model):

    hospitsl_name = models.CharField(max_length=100)
    booking_type = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=100)
    card_no = models.IntegerField()
    bkash_no = models.IntegerField()
    address = models.CharField(max_length=100)


class hospital(models.Model):

    hospitsl_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    Bkash_no = models.CharField(max_length=10)
    contact_no= models.IntegerField()

    



class information(models.Model):

    hospitsl_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    ICU = models.IntegerField()
    ward = models.IntegerField()
    oxygen_supply = models.CharField(max_length=10)
    contact_no= models.IntegerField

    def __str__(self):
        return self.hospitsl_name
    




class dept(models.Model):
    dept_name = models.TextField()
    def __str__(self):
        return self.dept_name
class Meta:
    verbose_name_plural = "departments"



class doctor1(models.Model):
    img = models.ImageField(null=True, blank= True )
    name = models.CharField(max_length=100)
    #dept= models.CharField(max_length=100)
    #dept = models.ForeignKey(dept, verbose_name=dept, default=1, on_delete= models.SET_DEFAULT)
    dept = models.ForeignKey(dept, on_delete= models.CASCADE)
    #hospital = models.CharField(max_length=100)
    hospital = models.ForeignKey(information, on_delete= models.CASCADE)
    status = models.BooleanField(default=False)
    qualification = models.TextField()
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_doctors():
        return doctor1.objects.all()
    @staticmethod
    def get_all_doctors_by_id(dept_id):
      if dept_id:
        return doctor1.objects.filter(dept = id)
      else:
        return doctor1.get_all_doctors()






class news(models.Model):
    top_news = models.BooleanField(default=False)
    img_link = models.TextField()
    news_title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.TextField()
    def __str__(self):
        return self.news_title


