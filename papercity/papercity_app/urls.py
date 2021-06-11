from django.urls import path, include
from . import views
from django.views.generic import ListView
from .models import Books

urlpatterns = [
    path('', ListView.as_view(queryset=Books.objects.all().order_by('-id')[:5], template_name='papercity_app/home.html')),
    path('home', ListView.as_view(queryset=Books.objects.all().order_by('-id')[:5], template_name='papercity_app/home.html')),
    path('books', views.BookView.as_view()),
    path('<slug:slug>', views.BookDetailView.as_view(), name="book_detail"),
    path('review/<int:pk>', views.AddReview.as_view(), name="add_review"),

    path('cat1', views.cat1, name='cat1'),
    path('cat2', views.cat2, name='cat2'),
    path('cat3', views.cat3, name='cat3'),
    path('cat4', views.cat4, name='cat4'),
    path('cat5', views.cat5, name='cat5'),
    path('cat6', views.cat6, name='cat6'),
    path('cat7', views.cat7, name='cat7'),
    path('cat8', views.cat8, name='cat8'),
    path('cat9', views.cat9, name='cat9'),
    path('minicat1', views.minicat1, name='minicat1'),
    path('minicat2', views.minicat2, name='minicat2'),
    path('minicat3', views.minicat3, name='minicat3'),
    path('minicat4', views.minicat4, name='minicat4'),
    path('minicat5', views.minicat5, name='minicat5'),
    path('minicat6', views.minicat6, name='minicat6'),
    path('minicat7', views.minicat7, name='minicat7'),
    path('minicat8', views.minicat8, name='minicat8'),
    path('minicat9', views.minicat9, name='minicat9'),
    path('minicat10', views.minicat10, name='minicat10'),
    path('minicat11', views.minicat11, name='minicat11'),
    path('minicat12', views.minicat12, name='minicat12'),
    path('minicat13', views.minicat13, name='minicat13'),
    path('minicat14', views.minicat14, name='minicat14'),
    path('minicat15', views.minicat15, name='minicat15'),
    path('minicat16', views.minicat16, name='minicat16'),
    path('minicat17', views.minicat17, name='minicat17'),
    path('minicat18', views.minicat18, name='minicat18'),
    path('minicat19', views.minicat19, name='minicat19'),
    path('minicat20', views.minicat20, name='minicat20'),
    path('minicat21', views.minicat21, name='minicat21'),
    path('minicat22', views.minicat22, name='minicat22'),
    path('minicat23', views.minicat23, name='minicat23'),
    path('minicat24', views.minicat24, name='minicat24'),
    path('minicat25', views.minicat25, name='minicat25'),
    path('minicat26', views.minicat26, name='minicat26'),
    path('minicat27', views.minicat27, name='minicat27'),
    path('minicat28', views.minicat28, name='minicat28'),
    path('minicat29', views.minicat29, name='minicat29'),
    path('minicat30', views.minicat30, name='minicat30'),
    path('minicat31', views.minicat31, name='minicat31'),
    path('minicat32', views.minicat32, name='minicat32'),
    path('minicat33', views.minicat33, name='minicat33'),
    path('minicat34', views.minicat34, name='minicat34'),
    path('minicat35', views.minicat35, name='minicat35'),
    path('minicat36', views.minicat36, name='minicat36'),
    path('minicat37', views.minicat37, name='minicat37'),
    path('minicat38', views.minicat38, name='minicat38'),
    path('minicat39', views.minicat39, name='minicat39'),
    path('minicat40', views.minicat40, name='minicat40'),
    path('minicat41', views.minicat41, name='minicat41'),
    path('minicat42', views.minicat42, name='minicat42'),
    path('minicat43', views.minicat43, name='minicat43'),
    path('minicat44', views.minicat44, name='minicat44'),
    path('minicat45', views.minicat45, name='minicat45'),
]