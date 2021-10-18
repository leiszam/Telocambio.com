from authApp.models.user import User
from authApp.models.profile import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'birth_date', 'gender', 'country', 'payment_method', 'notification_status', 'plan_type']
        

    def to_representation(self, obj):
        user = User.objects.get(id=obj.user.id)
        profile = Profile.objects.get(id=obj.id)

        return {
            "id": profile.id, 
            "birth_date": profile.birth_date, 
            "gender": profile.gender, 
            "country": profile.country, 
            "payment_method": profile.payment_method, 
            "notification_status": profile.notification_status, 
            "plan_type": profile.plan_type,
            "user": {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email,
                "address": user.address,
                "cellphone": user.cellphone
            }
        }
        


