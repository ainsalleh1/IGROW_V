from rest_framework import serializers
from .models import Person
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsersSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(required=False)
    #password = serializers.CharField(required=False)
    #name = serializers.CharField(required=False)
    #ranking = serializers.FloatField(required=False)
    
    Email = serializers.CharField(required=False)
    # Pwd = models.CharField(max_length=150)
    Password = serializers.CharField(required=False)
    #Username = serializers.CharField(required=False)
    #Name =serializers.CharField(required=False)
    #DateOfBirth = serializers.CharField(required=False)
    #Age = serializers.IntegerField (required=False)
    ##District = serializers.CharField(required=False)
    #State = serializers.CharField(required=False)
    #Occupation = serializers.CharField(required=False)
    #About = serializers.CharField(required=False)
    #Gender = serializers.CharField(required=False)
    #MaritalStatus = serializers.CharField(required=False)

    class Meta:
        model = Person
        fields = ['Email', 'Password']
        #fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    #def validate(self, data):
        #username = data.get("username", None)
        #password = data.get("password", None)
        #if Users.objects.filter(username=username).filter(password=password).first():
        #    return True

        #raise NotAuthenticated

        #def create(self, validated_data):
        #    return Person.objects.create(validated_data)
        
        #def update(self, instance, validated_data):
        #    instance.Email = validated_data.get('Email', instance.Email)
        #    instance.Passwrod = validated_data.get('Password', instance.Password)
        #    instance.save()
        #    return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

        @classmethod

        def get_token(cls, user):
            token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
            token['username'] = user.username
            return token

