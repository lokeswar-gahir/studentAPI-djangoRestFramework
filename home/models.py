from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Name*",max_length=100, blank=False)
    age = models.IntegerField("Age*",default=0)
    phone_no = models.CharField("Phone Number*",max_length=14, blank=False)
    alternate_phone_no = models.CharField("Alternative Phone Number",max_length=14, blank=True)
    email = models.EmailField("Email", blank=True)
    address = models.TextField(blank=True)
    image = models.ImageField('Image', upload_to='student_images/', blank=True)

    def delete(self,*args, **kwargs):
        self.image.delete()
        return super().delete()
    
    @property
    def image_url(self):
        if self.image == "":
            return '#'
        return self.image.url
    
    def save(self, *args, **kwargs):
        if self.id:
            existing = Student.objects.get(id = self.id)
            if self.image != existing.image:
                existing.image.delete(save=False)
            
        return super().save(*args, **kwargs)
        