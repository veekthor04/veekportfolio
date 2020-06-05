from django.shortcuts import render,redirect
from .models import Post, Comment, Category
from .forms import CommentForm

# Create your views here.
def blog_index(request):
    return redirect('blog_category', category='all')

def blog_category(request, category='all'):
    if category == 'all':
        posts = Post.objects.all().order_by('-date_created')
    else:
        posts = Post.objects.filter(
            categories__name__contains=category
        ).order_by(
            '-date_created'
        )
    categories = Category.objects.all()
    context = {
        "category": category,
        "posts": posts,
        "categories" : categories
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)
