from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Autor")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name="Categoria")
    content = models.TextField(verbose_name="Conteúdo")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Imagem")
    video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="Vídeo")
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True, verbose_name="Curtidas")
    is_official = models.BooleanField(default=False, verbose_name="Notícia Oficial")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Postagem")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    content = models.TextField(verbose_name="Conteúdo")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies', verbose_name="Resposta para")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return f'Comentário de {self.author} em {self.post}'

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, verbose_name="Remetente", null=True, blank=True)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, verbose_name="Destinatário", null=True, blank=True)
    subject = models.CharField(max_length=200, verbose_name="Assunto")
    body = models.TextField(verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    is_read = models.BooleanField(default=False, verbose_name="Lida")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies', verbose_name="Resposta para")

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.subject}"

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
