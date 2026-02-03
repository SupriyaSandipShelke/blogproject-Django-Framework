from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Post, Comment, Category
from .forms import PostForm, SignupForm

def home(request):
    category = request.GET.get('category')
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    if category:
        posts = posts.filter(category__id=category)

    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST' and request.user.is_authenticated:
        Comment.objects.create(
            post=post,
            user=request.user,
            text=request.POST['text']
        )
        return redirect('post_detail', id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments
    })


@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home')
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', id=id)
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    post.delete()
    return redirect('home')


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
