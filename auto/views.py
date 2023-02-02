from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CarAd
from .forms import CommentForm


def Home(request):
    """
    Render about page on request
    """
    return render(request, 'index.html')


class CarAdList(generic.ListView):
    """
    Shows maximum of 12 Car Posts
    on the browse.html page
    """
    model = CarAd
    queryset = CarAd.objects.order_by("-created_on")
    template_name = "browse.html"
    paginate_by = 12


class AdDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = CarAd.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "ad_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented":  False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = CarAd.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "ad_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class AdLike(View):

    def post(self, request, slug):
        queryset = CarAd.objects
        post = get_object_or_404(queryset, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('ad_detail', args=[slug]))


def About(request):
    """
    Render about page on request
    """
    return render(request, 'about.html')