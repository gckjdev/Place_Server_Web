from django.contrib import admin
from django.db import models
from django.db.models.fields import Field
from django.db.models.query import QuerySet

class Photo(models.Model):
    post_id = models.CharField(max_length=100)
    caption = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='photos')

    @classmethod
    def json_default(cls, obj):
        if isinstance(obj, QuerySet):
            entities = []
            for entity in obj:
                entities.append(entity)
            return entities
        if isinstance(obj, models.Model):
            return obj.to_dict()
        raise TypeError(repr(obj) + ' is not JSON serializable')

    def to_dict(self):
        dict = {}
        cls = self.__class__
        for name, column in self.__class__.__dict__.iteritems():
            if isinstance(column, Field):
                dict[name] = self.__getattribute__(name)
        return dict

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'image', 'caption')

admin.site.register(Photo, PhotoAdmin)