from django.urls import path 
from . import views 

urlpatterns = [
    path ('', views.books),
    path ('add_book', views.add_book),
    path ('add_favorite', views.add_favorite),
    path ('delete_favorite/<int:id>', views.delete_favorite),
    path ('<int:id>', views.book_detail),
    path ('book_update', views.book_update),
    path ('delete/<int:id>', views.book_delete),
    path ('my_view', views.my_view),
    path ('logout', views.logout),
]