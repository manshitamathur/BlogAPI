from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.BlogDisplay.as_view()),
    path('categories/',views.CategoryDisplay.as_view()),
    path('blog/<int:pk>/',views.BlogUpdate.as_view()),
    path('categories/<int:pk>/',views.CategoryUpdate.as_view()),
    path('<str:Category__name>/<int:pk>/',views.BlogPostByCategory.as_view()),
    #path('<str:category__name>/<int:pk>/',views.BlogPostByCategory.as_view()),

]
