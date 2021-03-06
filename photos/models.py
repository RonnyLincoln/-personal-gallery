from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt


class Location(models.Model):
   
    name = models.CharField(max_length = 30)

    def save_location(self):

        self.save()

    def delete(self):
       
        self.delete()

    def update(self,field,val):
        
        Location.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name


class Category(models.Model):
    
    name = models.CharField(max_length = 30)
    def save_category(self):
      
        self.save()

    def delete(self):
       
        Category.objects.get(id = self.id).delete()

    def update(self,field,val):
       
        Category.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')    
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
       
        self.save()

    def delete_image(self):
       
        Image.objects.get(id = self.id).delete()


    def update_image(self,val):
       
        Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_image_by_id(cls,image_id):
       
        return cls.objects.get(id = image_id)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

    @classmethod
    def search_image(cls,title):
       
        try:   
            searched_title = Title.objects.filter(name__icontains  = title)[0]
            return cls.objects.filter(title_id = searched_title.id)
        except Exception:
            return "No images found"    

    def __str__(self):
        return self.title

    class Meta:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        verbose_name_plural='images'

   