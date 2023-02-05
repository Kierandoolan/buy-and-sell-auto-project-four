from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CarAd
from .forms import CommentForm, CarForm
from django.conf import settings


def Home(request):
    """
    Render about page on request
    """
    return render(request, 'index.html')


class CarAdList(generic.ListView):
    """
    Shows maximum of 12 Car Posts
    on the carlist.html page
    """
    model = CarAd
    queryset = CarAd.objects.order_by("-created_on")
    template_name = "carlist.html"
    paginate_by = 12


def AddCar(request):
    
    form = CarForm(request.POST, request.FILES)
    context = {
            'form': form,
            }
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.author = request.user
        new_form.save()
        
        return redirect('home')
    else:
        form = CarForm()
        return render(request, 'add_car.html', context)


def EditCar(request, slug):
    """
    Edit Car
    """
    item = get_object_or_404(CarAd, slug=slug)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=item)
        form.save()
        return redirect('home')
    form = CarForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'edit_car.html', context)

def DeleteCar(request, slug):
    """
    Delete Car Ciew
    """
    car = CarAd.objects.get(slug=slug)
    car.delete()
    return redirect('home')


class AdLike(View):
    
    def post(self, request, slug):
        
        car = get_object_or_404(CarAd, slug=slug)

        if car.likes.filter(id=request.user.id).exists():
            car.likes.remove(request.user)
        else:
            car.likes.add(request.user)

        return HttpResponseRedirect(reverse('Car_ad_detail', args=[slug]))


def About(request):
    """
    Render about page on request
    """
    return render(request, 'about.html')


class CarAdDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = CarAd.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "car_ad_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented":  False,
                "liked": liked,
                "comment_form": CommentForm(),
                "car_form": CarForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = CarAd.objects.filter(status=1)
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
            "car_ad_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
