from django.contrib import admin

# Register your models here.
from .models import Koati, Video
from .models import VideoD, Uncharted, Batman, Matrix, Morbius, Moonfall, TIB, Turn, Koati
# from .models import Movie



admin.site.register(Video)
admin.site.register(VideoD)
admin.site.register(Uncharted)
admin.site.register(Batman)
admin.site.register(Matrix)
admin.site.register(Morbius)
admin.site.register(Moonfall)
admin.site.register(TIB)
admin.site.register(Turn)
admin.site.register(Koati)


