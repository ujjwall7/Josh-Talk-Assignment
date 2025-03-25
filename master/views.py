from .models import *
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class TaskAPI(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        if id:
            obj = get_object_or_404(Task, id=id)
            serializer = TaskGetSerializer(obj, many=False)
            return Response(
                {
                    'data': serializer.data,
                    'success':True, 
                }
            )
        obj = Task.objects.all().order_by('-id')
        serializer = TaskGetSerializer(obj, many=True)
        return Response(
            {
                'data': serializer.data,
                'success':True, 
            }
        )

    def post(self, request):
        serializer=AddUpdateTaskSerializer(data=request.data)
        if serializer.is_valid():
            f=serializer.save()
            return Response({'msg':'Task Created Successfully','success':True}, status=status.HTTP_201_CREATED)
        return Response({"errors":serializer.errors,"success":False,"msg": "Something went wrong! Kindly recheck!"}, status=status.HTTP_400_BAD_REQUEST)


class AssignTaskAPI(APIView):
    def post(self, request):
        get_user_id = eval(request.data.get('user_id',[]))
        print(type(get_user_id))
        print(get_user_id)
        get_task_id = request.data.get('task_id')
        if not get_user_id or not get_task_id:
            return Response({'msg':'user id and task id is required','success':False})
        try:
            task = Task.objects.get(id = get_task_id)
        except Exception as e:
            return Response({'error':'Task id not exists!','success':False})
        
        user = User.objects.filter(id__in = get_user_id)

        user_set_in_task = task.assigned_users.set(user)
        return Response({'msg':'Assigned Task Successfully','success':True}, status=status.HTTP_201_CREATED)

class UserTaskAPI(APIView):
    def get(self, request):
        user_id = self.request.query_params.get('user_id')
        
        try:
            user = User.objects.get(id = user_id)
            serializer = UserGetSerializer(user, many=False)
            return Response({'data': serializer.data})
        except Exception as e:
            return Response({'error':str(e),'success':False})
        

