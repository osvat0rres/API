from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view     
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics
from .models import BookMenu
from .serializer import BookMenuSerializer


# Create your views here.

@api_view(['POST','GET','DELETE'])
def book(request):
    return Response('list of books', status=status.HTTP_200_OK)


def menu(request):
    return HttpResponse('Menu view')

class BookList(APIView):
    
    def get(self,requests):
        
        author = requests.GET.get("author")
        if author:
            return Response({'message':'list of books by' + author}, status.HTTP_200_OK)
        return Response({'message':'list of books'}, status.HTTP_200_OK)
    
    def post(self, request):
        return Response({'title': request.data.get('title')}, status.HTTP_201_CREATED)



class BookDetail(APIView):
    def get(self, request, pk):
        return Response({'message': 'single book with id' + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({'title': request.data.get('title')}, status.HTTP_200_OK)
    
    
class BookMenuView(generics.ListCreateAPIView):
    queryset = BookMenu.objects.all()
    serializer_class = BookMenuSerializer
    
class SingleBookMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = BookMenu.objects.all()
    serializer_class = BookMenuSerializer