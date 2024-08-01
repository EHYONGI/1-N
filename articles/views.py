from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    articles = Article.objects.get(id=id)
    form = CommentForm()

    comments = Comment.objects.filter(article_id=id)

    context = {
        'article': articles,
        'form': form,
        'comments': comments,
    }

    return render(request, 'detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    
    return render(request, 'form.html', context)

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=article.id)
    
    else:
        # article = Article.objects.get(id=id)

        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

def delete(request, id):
    pass



def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            # 1. 객체 저장하는 방법
            # article = Article.objects.get(id=article_id)
            # comment.article = article
            # comment.save()

            # 2. integer(숫자)를 저장하는 방법
            comment.article_id = article_id
            comment.save()

            return redirect('articles:detail', id=article_id)

    else:
        return redirect('articles:index')
    
def comment_delete(request, article_id, id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=id)
        comment.delete()
    
    return redirect('articles:detail', id=article_id)   