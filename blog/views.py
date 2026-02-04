from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Post, Comment, Category, Like
from .forms import PostForm, SignupForm

def home(request):
    category = request.GET.get('category')
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    if category:
        posts = posts.filter(category__id=category)

    # Get statistics
    total_posts = Post.objects.count()
    total_authors = Post.objects.values('author').distinct().count()
    total_categories = Category.objects.count()

    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories,
        'total_posts': total_posts,
        'total_authors': total_authors,
        'total_categories': total_categories,
        'selected_category': category,
        'search_query': request.GET.get('q', '')
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    
    # Check if user has already liked this post
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = Like.objects.filter(post=post, user=request.user).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        Comment.objects.create(
            post=post,
            user=request.user,
            text=request.POST['text']
        )
        return redirect('post_detail', id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'user_has_liked': user_has_liked,
        'total_likes': post.post_likes.count()
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


@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    like = Like.objects.filter(post=post, user=request.user)
    
    if like.exists():
        like.delete()
    else:
        Like.objects.create(post=post, user=request.user)
    
    return redirect('post_detail', id=id)


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
