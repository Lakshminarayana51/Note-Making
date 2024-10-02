from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])

def create_todo(request,formate=None):
   title_input = request.data["title"]
   description_input = request.data["description"]

   status_input = "in progress"
   obj = create_todo(
                     title = title_input,
                     description = description_input,
                     status = status_input
                     )
   obj.save()

   return Response({"message":"completed"})