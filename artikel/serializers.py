from rest_framework import serializers
from .models import Kategori, Artikel, Comment

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class ArtikelSerializer(serializers.ModelSerializer):
    kategori = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Artikel
        fields = '__all__'

# Serializer baru untuk Komentar
class CommentSerializer(serializers.ModelSerializer):
    
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        
        fields = ['id', 'artikel', 'user', 'user_username', 'content', 'created_at', 'is_approved']
        
        # 'user' dan 'created_at' bersifat read-only.
        read_only_fields = ['created_at', 'user']