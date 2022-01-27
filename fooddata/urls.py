from .views import RetrieveFood, SearchFoods
from django.urls import re_path


urlpatterns = [
re_path('^api/foods/(?P<searchtext>.+)/$', SearchFoods.as_view()),
re_path('^api/food/(?P<fooditem>.+)/$', RetrieveFood.as_view())
]



