from rest_framework import serializers
from .models import UserProfile, Task, CustomUser


class YourUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'phone', 'address', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class YourSignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'date_of_birth', 'profile_picture']

class TaskSerializer(serializers.ModelSerializer):
    last_updated_by = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True,
        required=False  # Ajoutez ceci pour permettre le champ d'être facultatif
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'status', 'last_updated_by', 'created_date', 'updated_date']
