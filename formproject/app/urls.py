from django.urls import path
from .views import *


urlpatterns = [
    # path('book/', books),
    path('addbook/', addbook),
    path('showbook/', showbook),
    path('update/<int:id>/', update),
    path('delete/<int:id>/', delete),

]