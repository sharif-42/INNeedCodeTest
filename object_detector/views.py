import cv2
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from object_detector.models import UserFile
from object_detector.object_detectors import detect_object


class ObjectDetector(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'dashboard.html'

    def post(self,request):
        try:
            file = request.FILES['image']
            print(type(file))
            file_name = file.name
            print(type(file_name))
            print(file_name)
            user_file_obj = UserFile.objects.create_user_file(user=request.user, requested_file=file)
            detect_object(file_name) # call object detection module
            return Response({"Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"Failed"}, status=status.HTTP_200_OK)

class DeleteUserFile(APIView):
    def get(self,request,pk):
        try:
            file_obj = UserFile.objects.get(pk=pk).delete()
            print("###############")
            return redirect('/dashboard/')

        except ObjectDoesNotExist:
            return redirect('/dashboard/')
