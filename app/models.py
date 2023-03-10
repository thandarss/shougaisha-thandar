"""
Definition of models.
"""

from pyexpat import model
from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    personId = models.CharField(max_length=10)
    personNameKana = models.CharField(max_length=100)
    personNameKanji = models.CharField(max_length=100)
    personAddress = models.CharField(max_length=50)
    personBD = models.CharField(max_length=50)
    relationshipId = models.CharField(max_length=7)
    phoneNo = models.CharField(max_length=9)
    mailAddressNo = models.CharField(max_length=10)
    familyId = models.CharField(max_length=10)
    noOfHistory = models.CharField(max_length=50)
    ticketNumber = models.CharField(max_length=10)
    issueDate = models.CharField(max_length=10)
    caseNumber = models.CharField(max_length=10)
    diseaseInfo = models.CharField(max_length=50)
    class Meta:
        db_table = "app_personinfo"

class RelationshipInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    relationshipID = models.CharField(max_length=7)
    relationshipType = models.CharField(max_length=100)

    class Meta:
        db_table ="app_relationshipinfo"

class JopCategoryInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    jobID = models.CharField(max_length=7)
    jobType = models.CharField(max_length=100)

    class Meta:
        db_table = "app_jobcategoryinfo"

class GurdianInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    gurdianID = models.CharField(max_length=10)


    class Meta:
        db_table = "app_gurdianinfo"

class TargetCategoryInfo(models.Model):
    id = models.IntegerField(primary_key = True)
    targetID = models.CharField(max_length=7)
    targetName = models.CharField(max_length=100)

    class Meta:
        db_table = "app_targetcatgoryinfo"

class DraftPersonInfo(models.Model):
    id = models.IntegerField(primary_key = True)
    draftPersonID = models.CharField(max_length=7)
    draftPersonName = models.CharField(max_length=100)

    class Meta:
        db_table = "app_draftpersoninfo"

class KannaiInfo(models.Model):
    id = models.IntegerField(primary_key = True)
    kannaiID = models.CharField(max_length=7)
    kannaiType = models.CharField(max_length=100)

    class Meta:
        db_table = "app_kannaiinfo"

class RegisterReasonInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    reReasonID = models.CharField(max_length=7)
    reReasonName = models.CharField(max_length=100)

    class Meta:
        db_table = 'app_registerreasoninfo'
                
class RegisterPersonInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    registerPersonID = models.CharField(max_length=7)
    registerPersonName = models.CharField(max_length=100)

    class Meta:
        db_table = 'app_registerpersoninfo'

class PaymentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    paymentID = models.CharField(max_length=7)
    paymentType = models.CharField(max_length=100)

    class Meta:
        db_table = 'app_paymentinfo'

class DecisionInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    decisionID = models.CharField(max_length=7)
    decisionType = models.CharField(max_length=100)

    class Meta:
        db_table = 'app_decisioninfo'