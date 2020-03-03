from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# ..views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from django.views import generic


# Create your views here.
from . import models
from . import forms


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     busqueda = request.POST.get("producto")
    #     context['post'] = models.Post.objects.filter(title__contains = keyword)
    #     context['pages'] = models.Entries.objects.filter(section='home').filter(active=1).order_by('ordered')


class PostListView(generic.ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(active=1).order_by('publish_on')[:5]  # obtenemos 5 noticias


# def posts(request):
#     keyword = request.GET.get("keyword")
#     if keyword:
#         posts = models.Post.objects.filter(title__contains = keyword)
#         return render(request, "posts.html" , {"posts": posts})
#     posts = models.Post.objects.all()

#     return render(request, "posts.html", {"posts": posts})

    
# def index(request):
#     return render(request,"index.html")
    
# def about(request):
#     return render(request,"about.html")
# @login_required(login_url = "user:login")
# def dashboard(request):
#     articles = Article.objects.filter(author = request.user)
#     context = {
#         "articles":articles
#     }
#     return render(request,"dashboard.html",context)
# @login_required(login_url = "user:login")
# def addArticle(request):
#     form = ArticleForm(request.POST or None,request.FILES or None)

#     if form.is_valid():
#         article = form.save(commit=False)
        
#         article.author = request.user
#         article.save()

#         messages.success(request,"Makale başarıyla oluşturuldu")
#         return redirect("article:dashboard")
#     return render(request,"addarticle.html",{"form":form})
# def detail(request,id):
#     #article = Article.objects.filter(id = id).first()   
#     article = get_object_or_404(Article,id = id)

#     comments = article.comments.all()
#     return render(request,"detail.html",{"article":article,"comments":comments})
# @login_required(login_url = "user:login")
# def updateArticle(request,id):

#     article = get_object_or_404(Article,id = id)
#     form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
#     if form.is_valid():
#         article = form.save(commit=False)
        
#         article.author = request.user
#         article.save()

#         messages.success(request,"Makale başarıyla güncellendi")
#         return redirect("article:dashboard")


#     return render(request,"update.html",{"form":form})
# @login_required(login_url = "user:login")
# def deleteArticle(request,id):
#     article = get_object_or_404(Article,id = id)

#     article.delete()

#     messages.success(request,"Makale Başarıyla Silindi")

#     return redirect("article:dashboard")
# def addComment(request,id):
#     article = get_object_or_404(Article,id = id)

#     if request.method == "POST":
#         comment_author = request.POST.get("comment_author")
#         comment_content = request.POST.get("comment_content")

#         newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

#         newComment.article = article

#         newComment.save()
#     return redirect(reverse("article:detail",kwargs={"id":id}))
    