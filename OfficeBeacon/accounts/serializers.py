from rest_framework import serializers
from accounts.models import Profile
from django.contrib.auth.models import User




class ProfileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = Profile(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Profile
        fields = ['pk', 'username', 'password', 'email', 'nick', 'phone', 'is_flextime', 'flextime', 'created_at', 'updated_at']
        extra_kwargs = {'password':{'write_only':True}}



class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['username', 'password', ]







# Token Serializer
"""
class ProfileTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['token', ]
"""

#1 Use PrimaryKeyRelatedField
"""
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(User.objects.filter())
    class Meta:
        model = Profile
        fields = ['nick','phone', 'username', ]
"""

#2 Use SerializerMethodField - for GET method only
"""
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['nick', 'phone', 'username', ]

    def get_username(self, profile):

        user_obj = User.objects.get(pk=profile.pk)
        return user_obj.username

        #return profile.user.username
"""


#3 Use nested Serializer
"""
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['nick','phone','user', ]
"""

#4 Define serializer field explicitly with 'source = '
"""
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ['nick', 'phone', 'username', ]

    #def create(self, validated_data):
"""