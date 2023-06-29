from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import api_view,APIView


from rest_framework.response import Response

from rest_framework import status

from .models import Blog
from blog.serializers import BlogSerializer





class Blogpost(APIView):
   
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        
        params = { 'blog':blogs}
        

        serializer = BlogSerializer(blogs, many=True)
        return render(request,'index.html',params)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




#function based views

# @api_view(['GET', 'POST'])
# def blog_list(request):
   
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class based views



# @login_required
# def home(request):
#     notes = UserNote.objects.filter(user=request.user)
#     return render(request, 'note.html', {'notes': notes})
#     @login_required


# @login_required
# def note(request):
#     if request.method == 'POST':
#         code = request.POST['code']
#         text_note = request.POST['text_note']
#         note = Note.objects.create(user=request.user, code=code, text_note=text_note)
#         return HttpResponse("Successfully")

#     notes = UserNote.objects.filter(user=request.user)
#     return render(request, 'note.html', {'notes': notes})


#right
# @login_required
# def user_note_view(request):

#     if request.method == 'POST':
#         code = request.POST['code']
#         text_note = request.POST['text_note']
#         note = Note.objects.create(user=request.user, code=code, text_note=text_note)
#         return HttpResponse("Successfully")

    
#     #users = User.objets.all().values_list('user','user')
#     users = User.objects.all()


#     return render(request, 'notelist.html',{'users':users})