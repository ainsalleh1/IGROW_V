from rest_framework import serializers
from .models import Person
from .models import Users
from rest_framework.exceptions import NotAuthenticated

class UsersSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(required=False)
    #password = serializers.CharField(required=False)
    #name = serializers.CharField(required=False)
    #ranking = serializers.FloatField(required=False)
    
    Email = serializers.CharField(required=False)
    # Pwd = models.CharField(max_length=150)
    Password = serializers.CharField(required=False)
    Username = serializers.CharField(required=False)
    Name =serializers.CharField(required=False)
    DateOfBirth = serializers.CharField(required=False)
    Age = serializers.IntegerField (required=False)
    District = serializers.CharField(required=False)
    State = serializers.CharField(required=False)
    Occupation = serializers.CharField(required=False)
    About = serializers.CharField(required=False)
    Gender = serializers.CharField(required=False)
    MaritalStatus = serializers.CharField(required=False)

    class Meta:
        model = Person
        fields = ['name', 'password',]
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    #def validate(self, data):
        #username = data.get("username", None)
        #password = data.get("password", None)
        #if Users.objects.filter(username=username).filter(password=password).first():
        #    return True

        #raise NotAuthenticated
