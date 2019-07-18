from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

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
        messages.success(request, 'Post successfully created!')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Post not created!')  # Fail warning always shows and twice

    context = {
        'form': form
    }

    return render(request, 'post_form.html', context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance
    }
    return render(request, 'post_detail.html', context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Post</a> successfully Updated!", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': instance.title,
        'instance': instance,
        'form': form
    }

    return render(request, 'post_form.html', context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Post Successfully Deleted!')
    return redirect('posts:list')
