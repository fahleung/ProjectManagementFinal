from rest_framework import serializers
from django.contrib.auth.models import User

from .models import CoursT, Cours, Ue


class CoursTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursT
        fields = ('id', 'nom_cours', 'groupe', 'quadrimestre', 'heure_debut', 'nom_prof', 'heure_fin', 'local', 'jour')


class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ('id', 'cours', 'quadrimestre', 'nombre_heure', 'nombre_credit')


class UeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ue
        fields = ('id', 'nom_ue', 'quadrimestre_ue', 'nombre_heure_ue', 'nombre_credit_ue')


# User Authentication
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



