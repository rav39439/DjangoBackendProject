from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra fields from the user model
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['is_superuser'] = self.user.is_superuser 

        return data


from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer