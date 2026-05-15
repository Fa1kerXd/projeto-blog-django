from django.urls import path
from blog.views import PostListView,mundodev,mundootaku,PostDetailView,PageDetailView,CreatedByListView,TagListView,SearchListView,CategoryListView


app_name = "blog"


urlpatterns = [
    path('',PostListView.as_view(),name="index" ),
    path('post/<slug:slug>/',PostDetailView.as_view(),name="post" ),
    path('page/<slug:slug>/',PageDetailView.as_view(),name="page" ),
    path('created_by/<int:author_pk>/',CreatedByListView.as_view(),name="created_by" ),
    path('category/<slug:slug>/',CategoryListView.as_view(),name="category" ),
    path('tag/<slug:slug>/',TagListView.as_view(),name="tag" ),
    path('search/',SearchListView.as_view(),name="search" ),
    path("mundodev/<slug:slug>",mundodev,name="mundodev"),
    path("mundoOtaku/<slug:slug>",mundootaku,name="mundootaku")
]