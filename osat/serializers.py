from rest_framework import serializers
from osat.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = alumni
        fields = ('fname', 'lname', 'email')


#class GroupSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
  #     fields = ('url', 'name')