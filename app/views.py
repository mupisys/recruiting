from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Post, Message, Category, Comment
from .serializers import PostSerializer, CommentSerializer, MessageSerializer
from .forms import SignUpForm
from .serializers import CategorySerializer

# --- Template ---

class LandpageView(TemplateView):
    template_name = 'home/landpage.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'auth/signup.html'

@method_decorator(login_required, name='dispatch')
class PostCreateView(TemplateView):
    template_name = 'posts/post_form.html'

@method_decorator(login_required, name='dispatch')
class PostDetailView(TemplateView):
    template_name = 'posts/post_detail.html'

@method_decorator(login_required, name='dispatch')
class MessageListView(TemplateView):
    template_name = 'messages/messages_list.html'

@method_decorator(login_required, name='dispatch')
class MessageCreateView(TemplateView):
    template_name = 'messages/message_edit.html'

@method_decorator(login_required, name='dispatch')
class MessageDetailView(TemplateView):
    template_name = 'messages/message_detail.html'

@method_decorator(login_required, name='dispatch')
class ConversationDetailView(TemplateView):
    template_name = 'messages/conversation_detail.html'

@method_decorator(login_required, name='dispatch')
class MessageUpdateView(TemplateView):
    template_name = 'messages/message_edit.html'

@method_decorator(login_required, name='dispatch')
class MessageDeleteView(TemplateView):
    template_name = 'messages/message_delete_confirm.html'

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

from django.contrib.auth.models import User

# --- API Views ---

class CategoryListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class PostPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination

    def get(self, request):
        is_official = request.query_params.get('is_official')
        if is_official is not None:
            is_official = is_official.lower() == 'true'
            posts = Post.objects.filter(is_official=is_official).order_by('-created_at')
        else:
            posts = Post.objects.all().order_by('-created_at')
        
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        comments = post.comments.filter(parent=None).order_by('-created_at')
        comments_serializer = CommentSerializer(comments, many=True)
        data = serializer.data
        data['comments'] = comments_serializer.data
        return Response(data)

    def put(self, request, pk):
        post = self.get_object(pk)
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return Response({"liked": liked, "total_likes": post.total_likes()})

class CommentCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSearchAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('q', '')
        if len(query) < 2:
            return Response([])
        users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)[:10]
        from .serializers import UserSerializer
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class MessageListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # Agrupamento de mensagens por conversa
        sent_to = Message.objects.filter(sender=request.user).values_list('recipient', flat=True)
        received_from = Message.objects.filter(recipient=request.user).values_list('sender', flat=True)
        
        user_ids = set(list(sent_to) + list(received_from))
        if None in user_ids:
            user_ids.remove(None)
            
        conversations = []
        for user_id in user_ids:
            other_user = User.objects.get(id=user_id)
            
            last_message = Message.objects.filter(
                (Q(sender=request.user, recipient=other_user) | 
                 Q(sender=other_user, recipient=request.user))
            ).order_by('-created_at').first()
            
            if last_message:
                conversations.append({
                    'user': {
                        'username': other_user.username,
                        'full_name': other_user.get_full_name() or other_user.username
                    },
                    'last_message': MessageSerializer(last_message).data
                })
        
        conversations.sort(key=lambda x: x['last_message']['created_at'], reverse=True)
        return Response(conversations)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConversationDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        other_user = get_object_or_404(User, username=username)
        messages = Message.objects.filter(
            (Q(sender=request.user, recipient=other_user) | 
             Q(sender=other_user, recipient=request.user))
        ).order_by('created_at')
        
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class MessageDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Message, pk=pk)

    def get(self, request, pk):
        message = self.get_object(pk)
        if request.user != message.sender and request.user != message.recipient:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def put(self, request, pk):
        message = self.get_object(pk)
        if request.user != message.sender:
            return Response({"detail": "Você não tem permissão para editar esta mensagem."}, status=status.HTTP_403_FORBIDDEN)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        message = self.get_object(pk)
        if request.user != message.sender:
            return Response({"detail": "Você não tem permissão para excluir esta mensagem."}, status=status.HTTP_403_FORBIDDEN)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
