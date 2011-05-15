from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
from place.photo.models import Photo
import json

def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = PhotoForm()
    return render_to_response('upload.html', {'form': form})

def get(request):
#    if request.GET:
#        params = request.GET.copy();
#        place_id = params['place_id']
    photos = Photo.objects.all()
    return __get_json_response(Photo, photos)

def __get_json_response(cls, obj):
    return HttpResponse(__to_json(cls, obj), content_type='application/json')

def __to_json(cls, obj):
    return json.dumps(obj, default=cls.json_default)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo


if __name__ == '__main__':
    pass