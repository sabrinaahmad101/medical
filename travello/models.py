from django.db import models


# Create your models here.
class Destination(models.Model): 

    name = models.CharField(max_length=100)
    img = models.ImageField( upload_to='pics' )
    
    price = models.IntegerField
    offer = models.BooleanField(default=False)


class studentDetails(models.Model):

    idno = models.IntegerField()
    s_name = models.CharField(max_length=100)
    marks =  models.IntegerField()

    def _str_(self):
        return self.s_name

    class Meta:
        db_table= "studentDetails"


class s_info(models.Model):

    
    name = models.ForeignKey(studentDetails, on_delete= models.CASCADE)
    roll =  models.IntegerField()

    def _str_(self):
        return self.name

    class Meta:
        db_table= "student_info"


        
    
