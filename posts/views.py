# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
from django.views import generic
from .models import Post, Comment 
from .forms import PostForm

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    # return HttpResponse('<h1>welcome to django</h1>')
    return Response({'name':'Fatemeh dehghan'})


def home(request):
    return HttpResponse('<h3>welcome to my blog..</h3>')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'posts/post_list.html',context=context)


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    
    def get_context_data(self,**kwargs): 
        context = super(PostDetail,self).get_context_data()
        context['comments'] = Comment.objects.filter(post=kwargs['object'].pk)
        return context



def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)

    except Post.DoesNotExist:
        return HttpResponseNotFound('post is not exist!')

    comments = Comment.objects.filter(post=post)
    context = {'post':post, 'comments': comments}
    return render(request,'posts/post_detail.html',context=context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # print(type(form.cleaned_data))
            # print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form=PostForm()

    return render(request,'posts/post_create.html',{'form':form})

