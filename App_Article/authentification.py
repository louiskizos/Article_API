import logging
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import login, get_user_model

logger = logging.getLogger(__name__)
User = get_user_model()

def authenticate_user(username_or_email, password):
    try:
        user = User.objects.get(username=username_or_email)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            return None
    
    if user.check_password(password):
        return user
    return None

# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
    
#     def post(self, request, *args, **kwargs):
#         username_or_email = request.data.get("username_or_email")
#         password = request.data.get("password")
#         logger.debug(f"Attempting to authenticate user with identifier: {username_or_email}")
        
#         user = authenticate_user(username_or_email, password)
        
#         if user is not None:
#             login(request, user)
#             usr, created = User.objects.get_or_create(username=user.username, email=user.email)
#             logger.debug(f"User authenticated successfully: {usr.username}")
#             return Response({"Msg": "Connected !", "user": usr.username})
#         else:
#             logger.debug("Invalid credentials provided")
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
