from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print('kkkkkkkkkkk----1')
        content = {'message': 'Hello, World!'}
        print('kkkkkkkkkkk')
        return Response(content)