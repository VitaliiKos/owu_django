from rest_framework.views import APIView
from rest_framework.response import Response
import json


class UsersListCreateView(APIView):

    def get(self, *args, **kwargs):
        try:
            with open('users.json', encoding='UTF-8') as users_file:
                data = json.load(users_file)
                return Response(data)
        except Exception:
            return Response("List is empty")

    def post(self, *args, **kwargs):
        params = self.request.data

        try:
            with open('users.json', encoding='UTF-8', mode='r') as users_file:
                data = json.load(users_file)
        except Exception:
            data = []
        try:
            with open('users.json', encoding='UTF-8', mode='w') as users_file:
                data.append(params)
                json.dump(data, users_file, indent=4)
                return Response("Created")
        except Exception as error:
            return Response(error)
