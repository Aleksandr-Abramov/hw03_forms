from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, Group


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def new_post(request):
    #Максим, я просто не представляю, как можно написать иначе функцию в концепции "Guard Block".
    #Статью прочел, буду следовать. Но, в этом случае...
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
        return render(request, 'index.html', {'form': form})

    form = PostForm()
    return render(request, "new.html", {"form": form})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})

#Максим, здравствуйте. Сохранил старый вариант создания формы в комментариях. Как напоминание. Прошу, не осуждать.)

# def new_post(request):
#     if request.method == "POST":
#
#         form = PostForm(request.POST)
#         if form.is_valid():
#             group = form.cleaned_data["group"]
#             text = form.cleaned_data["text"]
#             author = request.user
#             Post.objects.create(group=group,
#                                 text=text,
#                                 author=author
#                                 )
#             return redirect("index")
#
#         return render(request, 'index.html', {'form': form})
#
#     form = PostForm()
#     return render(request, "new.html", {"form": form})