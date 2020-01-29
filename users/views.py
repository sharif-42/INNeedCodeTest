from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from object_detector.models import UserFile
from users.forms import SignUpForm, LoginForm, ChangePasswordForm
from users.serializers import LoginSerializer


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)


class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        form = SignUpForm()
        queryset = "This is Home Page"
        return Response({'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
            # return Response({'form': form}, status=status.HTTP_200_OK)
        return Response({'form': form}, status=status.HTTP_200_OK)


class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return Response({'form': form})

    def post(self, request):
        form = LoginForm()
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            user = authenticate(request, username=serializer.data['username'], password=serializer.data['password'])
            if user is not None:
                login(request, user)
            print(request.data)
            return redirect('/dashboard/')
        return Response({'form': form}, status=status.HTTP_200_OK)


class Logout(APIView):
    def get(self, request):
        logout(request)
        return redirect('/home')


class ChangePassword(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'password_change.html'

    def get(self, request):
        form = ChangePasswordForm()
        return Response({'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
        return Response({'form': form}, status=status.HTTP_200_OK)


class DashBoard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'

    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        req_user = request.user
        print(req_user)
        files = UserFile.objects.filter(user=req_user)
        print(files)
        return Response({"files":files},status=status.HTTP_200_OK)
