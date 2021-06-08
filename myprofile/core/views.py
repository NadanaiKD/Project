from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from core.models import Profile, Email
from core.forms import SubscriberForm


# Create your views here.
def index(request):
    image = "https://scontent.fbkk12-2.fna.fbcdn.net/v/t31.18172-8/17039375_1413314708718737_7612081425750414986_o.jpg?_nc_cat=104&ccb=1-3&_nc_sid=09cbfe&_nc_eui2=AeHNVHSGiLFBGLNaF11ssc50C-P8RooO4hAL4_xGig7iEKWkZ2nO9crW69UZW1MWYXl6JW8QNTXnI-3RPH1EhYNM&_nc_ohc=6rN0_NpqWoQAX-R-ns0&_nc_ht=scontent.fbkk12-2.fna&oh=dc7330ef7f530fd499254dafb81ef218&oe=60E0EA04"
    http = (
        "<h1>LM is Me</h1> \
            <h2>Lukmoo</h2> \
            <p>I am newbie for coding </p> \
            <img src=%s width='500' height='500' ></p> \
            <p>I know it's hard, but I will do it.</p> \
           "
        % (image)
    )
    return HttpResponse(http)


class IndexView(View):
    def get(self, request):
        name = "Moo"

        profile = Profile.objects.get(id=1)

        form = SubscriberForm()

        return render(
            request, "index.html", {"name": name, "form": form, "profile": profile.name}
        )

    def post(self, request):
        print(request.POST)

        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_email = form.cleaned_data.get("email")
            Email.objects.create(email=user_email)

        return render(request, "index.html")
