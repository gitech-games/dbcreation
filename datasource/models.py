from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class UserModel(models.Model):
    EmpId = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=60)
    EmailId = models.EmailField(max_length=60)
    Dept = models.CharField(max_length=60)
    Desg = models.CharField(max_length=60)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-CreatedDate']

    def __unicode__(self):
        return '%s' % (self.EmpId)

class UserMaster(models.Model):
    user = models.CharField(max_length=60)
    Company = models.CharField(max_length=60)
    District = models.CharField(max_length=60)
    State = models.CharField(max_length=60)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-CreatedDate']

    def __unicode__(self):
        return '%s' % (self.user)

class WorkSpace(models.Model):
    WorkSpaceName = models.CharField(max_length=60, unique=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-CreatedDate']

    def __unicode__(self):
        return '%s' % (self.WorkSpaceName)

class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=50)
    joining_date = models.DateField()
    salary = models.IntegerField()
    # amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.employee_name

class FileUpload(models.Model):
    file = models.FileField(blank=True, null=True)
    updatedDate = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField(default=0)
    # owner = models.ForeignKey('auth_User')

    def __str__(self):
        return self.file.name

class CreateDB(models.Model):
    dbname = models.CharField(max_length=20)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(blank=True)

    def __str__(self):
        return self.dbname.name

class TableData(models.Model):
    tableName = models.JSONField(blank=True)
    tableColumn = models.JSONField(blank=True)
    tableData = models.JSONField(blank=True)
    dbName = models.JSONField(blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    updatedDate = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return '%s | %s' % (self.tableInfo, self.createdDate)

class FindDatatype(models.Model):
    ftype = [('CSV','CSV'), ('Excel','Excel'), ('JSON','JSON')]
    filetype = models.CharField(max_length=10, choices=ftype, blank=True)
    filepath = models.CharField(max_length=250, blank=True)
    filename = models.CharField(max_length=50, blank=True)
    datatype = models.JSONField(blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)

