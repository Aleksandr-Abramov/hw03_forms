from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .forms import PostForm
from .models import Post, Group


def index(request):
    """Главная страницы"""
    post_list = Post.objects.select_related("group").order_by("-pub_date")
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    context = {
        "page": page
    }
    return render(request, "index.html", context)


def group_posts(request, slug):
    """Страница автора"""
    group = get_object_or_404(Group, slug=slug)
    # post_list = Post.objects.select_related("group").order_by("-pub_date")
    author = Group.objects.get(slug=slug)
    post_list = author.posts.all().order_by("-pub_date")
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    context = {
        "group": group,
        "page": page
    }
    return render(request, "group.html", context)


def new_post(request):
    """Страница добовления поста"""
    if request.method != "POST":
        form = PostForm()
        context = {"form": form}
        return render(request, "new.html", context)

    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("index")
    context = {"form": form}
    return render(request, 'index.html', context)


def profile(request, username):
    # тут тело функции
    return render(request, 'profile.html', {})


# def post_view(request, username, post_id):
#     # тут тело функции
#     return render(request, 'post.html', {})
#
#
# def post_edit(request, username, post_id):
#     # тут тело функции. Не забудьте проверить,
#     # что текущий пользователь — это автор записи.
#     # В качестве шаблона страницы редактирования укажите шаблон создания новой записи
#     # который вы создали раньше (вы могли назвать шаблон иначе)
#     return render(request, 'post_new.html', {})
