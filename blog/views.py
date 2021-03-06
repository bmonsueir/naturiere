from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.all()


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    title = post.title
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('forum')
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'title': title})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
    
@login_required
def forum(request):
   
    all_posts = Post.objects.all()
    all_comments = Comment.objects.all()
    comment_form = CommentForm(request.POST or None, request.FILES or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.save()
    form = CommentForm()

    context = {'form':form,
       
        'all_posts': all_posts,
        'all_comment': all_comments
    }
    return render(request, 'blog/forum.html', context)
    
@login_required
def new_comment(request):
    comment_form = CommentForm(request.POST or None, request.FILES or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.save()
    form = CommentForm()
    return render(request, 'blog/new_comment.html', {'form':form})