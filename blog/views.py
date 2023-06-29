from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog-list.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': PostCreateForm()
        }
        return render(request, 'blog-create.html', context)

    def post(self, request, *args, **kwargs):
        context = {
            'form': PostCreateForm()
        }
        return render(request, 'blog-create.html', context)


# Create your views here.
