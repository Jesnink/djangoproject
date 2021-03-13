from django.urls import path
from .views import *
urlpatterns = [
    #path('',home,name="book_home"),
    
    path('',BookListView.as_view(),name="book_home"),
    path('about/',about, name="book_about"),
    #path('create/',create_book,name="new_book"),
    path('create/',BookCreateView.as_view(),name="new_book"),
    #path('update/<int:id>/',update,name="update_book"),
    path('update/<int:id>',BookUpdateView.as_view(),name="update_book"),
    path('delete/<int:id>/',delete,name="delete_book"),
    path('category/',CategoryListView.as_view(),name="category_list"),
    path('category/update/<int:id>/',CategoryUpdateView.as_view(),name="update_category"),
    path('category/delete/<int:id>/',deletecategory,name="delete_category"),
    path('category/create/',CategoryCreateView.as_view(),name="create_category"),


]
