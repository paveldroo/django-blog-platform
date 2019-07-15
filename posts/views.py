from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_list(request):
    context = {
        'title': 'Post List'
    }
    return render(request, 'index.html', context)


def post_create(request):
    return HttpResponse('<h1>Create</h1>')


def post_detail(request):
    return HttpResponse('<h1>Detail</h1>')


def post_update(request):
    return HttpResponse('<h1>Update</h1>')


def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')
