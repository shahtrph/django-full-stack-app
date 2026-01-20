from rest_framework import serializers
from .models import *


class CountrySerilizer(serializers.ModelSerializer):
  class Meta:
    model=Country
    field= ('id','name')

class LeagueSerilizer(serializers.ModelSerializer):
  class Meta:
    model=League
    field= ('id','name')


class CharacteristicsSerilizer(serializers.ModelSerializer):
  class Meta:
    model=Characteristics
    field= ('id','name')


class FootballClubsSerilizer(serializers.ModelSerializer):
  class Meta:
    model=FootballClubs
    field= "__all__"