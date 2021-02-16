from django.shortcuts import render
from .models import BlogPost,Category
from .serialize import BlogSerializer,CategorySerializer
from rest_framework import mixins,generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class BlogDisplay(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class BlogUpdate(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer


    lookup_field='pk'

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

class CategoryDisplay(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class CategoryUpdate(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    lookup_field='pk'

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

class BlogPostByCategory(generics.GenericAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category']
    lookup_field='pk'
    search_fields = ['title','body','author']
    
    
