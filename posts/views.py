from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from posts.forms import PostForm
from posts.models import Post


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'objects_list': queryset,
        'title': 'Post List'
    }
    return render(request, 'index.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        'form': form
    }

    return render(request, 'post_create.html', context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance
    }
    return render(request, 'post_detail.html', context)


def post_update(request):
    return HttpResponse('<h1>Update</h1>')


def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')
