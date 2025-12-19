from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    LandpageView, CustomLoginView, SignUpView,
    MessageListView, MessageDetailView, MessageCreateView, 
    MessageUpdateView, MessageDeleteView, ConversationDetailView,
    PostCreateView, PostDetailView,
    PostListAPIView, PostDetailAPIView, PostLikeAPIView, CommentCreateAPIView,
    MessageListCreateAPIView, MessageDetailAPIView, CategoryListAPIView, UserSearchAPIView,
    ConversationDetailAPIView
)

urlpatterns = [
    # Pages
    path('', LandpageView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(template_name='auth/logout_confirm.html'), name='logout'),
    
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/new/', MessageCreateView.as_view(), name='message_create'),
    path('messages/u/<str:username>/', ConversationDetailView.as_view(), name='conversation_detail'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_edit'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    # API Endpoints
    path('api/users/search/', UserSearchAPIView.as_view(), name='api_user_search'),
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list_create'),
    path('api/categories/', CategoryListAPIView.as_view(), name='api_category_list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api_post_detail'),
    path('api/posts/<int:pk>/like/', PostLikeAPIView.as_view(), name='api_post_like'),
    path('api/posts/<int:pk>/comment/', CommentCreateAPIView.as_view(), name='api_post_comment'),
    
    path('api/messages/', MessageListCreateAPIView.as_view(), name='api_message_list_create'),
    path('api/messages/conversation/<str:username>/', ConversationDetailAPIView.as_view(), name='api_conversation_detail'),
    path('api/messages/<int:pk>/', MessageDetailAPIView.as_view(), name='api_message_detail'),
]
