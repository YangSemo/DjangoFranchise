from django.urls import path, include

from . import views

app_name = 'myapp'

urlpatterns = [
    path('brand/', views.BrandListView.as_view()),
    path('brand/detail/', views.BrandDetailView.as_view()),

    path('headquarter/', views.HeadquarterView.as_view()),

    path('auth/', include('rest_framework.urls')),

    path('login/', views.LoginView),
    path('logout/', views.logout_view),
    path('register/', views.RegisterView.as_view()),

    path('basetheme/', views.BaseThemeView.as_view()),
    path('customtheme/', views.CustomThemeView.as_view()),

    path('address/', views.StoreAddressView.as_view()),
    path('population/', views.PopulationListView.as_view()),
]
