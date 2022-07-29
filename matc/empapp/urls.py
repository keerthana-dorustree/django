from empapp import views
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Profile services",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [

    path('apidocs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/', views.Login.as_view()),
    path('createemp', views.CreateEmployee.as_view()),
    path('createaddress', views.CreateAddress.as_view()),
    path('createperson',views.CreatePerson.as_view()),
    path('getallemp',views.GetAllemployee.as_view()),
    path('deleteemp/<str:pk>', views.DeleteEmployee.as_view()),
    path('deleteaddress/<str:pk>', views.DeleteAddress.as_view()),

]




