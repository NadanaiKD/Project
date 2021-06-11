from re import T, sub
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import serializers
from core.models import Profile, Email
from core.forms import SubscriberForm
from core.images import Me
from core.serializers import SubscriberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
def index(request):
    image = "https://scontent.fbkk12-2.fna.fbcdn.net/v/t31.18172-8/17039375_1413314708718737_7612081425750414986_o.jpg?_\nc_cat=104&ccb=1-3&_nc_\
            sid=09cbfe&_nc_eui2=AeHNVHSGiLFBGLNaF11ssc50C-P8RooO4hAL4_xGig7iEKWkZ2nO9crW69UZW1MWYXl6JW8QNTXnI-3RPH1EhYNM&_nc_ohc=6rN0_NpqWoQAX-R-\
            ns0&_nc_ht=scontent.fbkk12-2.fna&oh=dc7330ef7f530fd499254dafb81ef218&oe=60E0EA04"
    http = (
            """
            <html>
            <h1>LM is Me</h1> \
            <h2>Lukmoo</h2> \
            <p>I am newbie for coding </p> \
            <img src=%s width='500' height='500' ></p> \
            <p>I know it's hard, but I will do it.</p> \
            </html>
           """
            % (Me)
    )
    return HttpResponse(http)


class IndexView(View):
    def get(self, request):
        # 1 before use render
        # http = (
        #     """
        #     <html>
        #     <h1>LM is Me</h1> \
        #     <h2>Lukmoo</h2> \
        #     <p>I am newbie for coding </p> \
        #     <img src=%s width='500' height='500' ></p> \
        #     <p>I know it's hard, but I will do it.</p> \
        #     </html>
        #    """
        # )
        # return HttpResponse(http)

        # 2 render index.html
        profile = Profile.objects.get(id=1)

        title = "HELLO WORLD"
        # query name from db
        name = profile.name
        about_me = "I am newbie for coding"
        github_url = "https://github.com/NadanaiKD/Project.git"

        form = SubscriberForm()

        return render(
            request,
            "index.html",
            {
                "title": title,
                "name": name,
                "about_me": about_me,
                "github_url": github_url,
                "form": form,
                "profile": profile.name
            }
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get("email"))

        profile = Profile.objects.get(id=1)
        title = "HELLO WORLD"
        name = profile.name
        about_me = "I am newbie for coding"
        github_url = "https://github.com/NadanaiKD/Project.git"

        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_email = form.cleaned_data.get("email")
            # save into database
            Email.objects.create(email=user_email)

        return render(
            request,
            "index.html",
            {
                "title": title,
                "name": name,
                "about_me": about_me,
                "github_url": github_url,
                "form": form,
                "profile": profile.name
            }
        )


class SubscriberAPIView(APIView):
    def get(self, request):
        # data = {
        #     "text": "Hello world"
        # }
        # return JsonResponse(data)

        # request-->serializers-->serializers
        # subscriber = Email.objects.first()
        # serializers = SubscriberSerializer(subscriber)

        # many data
        subscriber = Email.objects.all()
        serializers = SubscriberSerializer(subscriber, many=True)

        return Response(serializers.data)

    def post(self, request):
        serializers = SubscriberSerializer(data=request.data)
        if serializers.is_valid():
            # print(serializers.data)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
