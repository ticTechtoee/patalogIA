from django.contrib import admin
from .models import Image,ImageType, ImagesQuestions, Specialty

admin.site.register(Image)
admin.site.register(ImageType)
admin.site.register(ImagesQuestions)
admin.site.register(Specialty)
