from .models import Image, GalleryImage
from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('image',)

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model=GalleryImage
        fields=('image',)