from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article,New
from .serializer import ArticleSerializer,AgentSerializer,LoginSerializer,NewSerializer
from rest_framework import generics,mixins
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login
import logging




class ArticleListAPIView(generics.ListAPIView):
     
     queryset = Article.objects.all() 
     serializer_class = ArticleSerializer


class ArticleMixView(generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def post(self, request, *args, **kwargs):
     
        titre = request.data.get('titre')
        resumer = request.data.get('resumer')
        date = request.data.get('date')  
        type = request.data.get('type')
        image = request.data.get('image')
        auteur = request.data.get('auteur')
        
        if Article.objects.filter(titre=titre).exists():
            return Response({"error": "User with this article already exists."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            article = Article.objects.create(
                titre=titre,
                image = image,
                resumer = resumer,
                date = date,
                type = type,
                auteur = auteur
            )
            article.save()

        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AgentMixView(generics.GenericAPIView,
                    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = AgentSerializer
    def post(self, request, *args, **kwargs):
     
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')  
                
        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this article already exists."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({"error": "User with this article already exists."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(
                username=username,
                email = email,
                password = password,
            )
            user.is_staff = True
            user.save()

        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = AgentSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class AgentListAPIView(generics.ListAPIView):
     
     queryset = User.objects.all() 
     serializer_class = AgentSerializer

logger = logging.getLogger(__name__)
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        logger.debug(f"Attempting to authenticate user with email: {username}")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            usr, created = User.objects.get_or_create(email=user.email)
            logger.debug(f"User authenticated successfully: {usr.username}")
            return Response({"Msg": "Connected !", "user": usr.username})
        else:
            logger.debug("Invalid credentials provided")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)



class NewMixView(generics.GenericAPIView,
                  mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    def post(self, request, *args, **kwargs):
     
        email = request.data.get('email')
        
        if New.objects.filter(email=email).exists():
            return Response({"error": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new = New.objects.create(
                email=email,
                
            )
            new.save()

        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = NewSerializer(new)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class NewListAPIView(generics.ListAPIView):
     
     queryset = New.objects.all() 
     serializer_class = NewSerializer
