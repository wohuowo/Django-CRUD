from django.urls import path#provides a link where the user would go to access the view
from .views import TodoAppCreateView, TodoAppDetailView,TodoAppListView,TodoAppDetailView, TodoAppUpdateView,TodoAppDeleteView


urlpatterns = [
    path('', TodoAppCreateView.as_view(), name="home"),#empty quote shows it is the home page and the as_view is used to link the classbased view second argument is what will show to the user
    path('list/', TodoAppListView.as_view()),
    path('detail/<pk>/', TodoAppDetailView.as_view()),
    path('update/<pk>/', TodoAppUpdateView.as_view()),
    path('delete/<pk>/', TodoAppDeleteView.as_view()),

    #pk means the primary key that is the id that is unique to each post or list
]
 