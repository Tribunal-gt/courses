from api.models import CourseResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name="v1")
api.register(CourseResource())
api.register(CategoryResource())

# api/v1/courses/1
# api/v1/categories/1

urlpatterns = [path("", include(api.urls), name="index")]
