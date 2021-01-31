from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.admin import User
from .models import (FileUpload, CreateDB, TableData, FindDatatype,
                    UserModel, UserMaster, WorkSpace)

class UserModelSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = UserModel
        fields = '__all__'

class UserMasterSerializer (ModelSerializer):
    class Meta:
        model = UserMaster
        fields = '__all__'

class UserMasterCrtSerializer (ModelSerializer):
    class Meta:
        model = UserMaster
        fields =[
            'user',
            'Company',
            'District',
            'State',
        ]



class WorkSpaceSerializer(ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = "__all__"






class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"

class CreateDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateDB
        fields = "__all__"

class TableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableData
        fields = "__all__"

class DatatypeSerializer(serializers.ModelSerializer):
    file = serializers.JSONField()
    datatype = serializers.CharField()

class FileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)

class FindDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindDatatype
        fields = "__all__"
