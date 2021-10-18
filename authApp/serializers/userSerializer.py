from rest_framework import serializers
from authApp.models.user import User
from authApp.models.profile import Profile
from authApp.serializers.profileSerializer import ProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
        model = User
        # fields = ['id', 'username', 'password', 'name', 'last_name', 'email', 'address', 'cellphone', 'profile']
        fields = ['id', 'username', 'password', 'name', 'last_name', 'email', 'address', 'cellphone']

    def create(self, validated_data):
        # profileData = validated_data.pop('profile')
        userInstance = User.objects.create(**validated_data)
        # Profile.objects.create(user=userInstance, **profileData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        # profile = Profile.objects.get(user=obj.id)
        return {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "last_name": user.last_name,
            "email": user.email,
            "address": user.address,
            "cellphone": user.cellphone
            # "profile": {
            #     "birth_date": profile.birth_date, 
            #     "gender": profile.gender, 
            #     "country": profile.country, 
            #     # "payment_method": profile.payment_method, 
            #     "notification_status": profile.notification_status, 
            #     "plan_type": profile.plan_type
            # }
        }

