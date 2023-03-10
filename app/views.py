"""
Definition of views.
"""

from . import models
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import PersonInfo, RelationshipInfo, JopCategoryInfo, TargetCategoryInfo,DraftPersonInfo, KannaiInfo, RegisterReasonInfo, RegisterPersonInfo,PaymentInfo, DecisionInfo

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def second(request):
    pid = request.GET.get('personId',None)
    personInfos = PersonInfo.objects.get(personId = pid)
    relationforPerson = RelationshipInfo.objects.filter(relationshipID = personInfos.relationshipId)
    relations = list(RelationshipInfo.objects.filter(id__gt=0))
    jobId = list(JopCategoryInfo.objects.filter(id__gt=0))
    targetID = list(TargetCategoryInfo.objects.filter(id__gt=2))
    draftID = list(DraftPersonInfo.objects.filter(id__gt=0))
    kannaiID = list(KannaiInfo.objects.filter(id__gt=0))
    reReasonId = list(RegisterReasonInfo.objects.filter(id__gt=0))
    registerPersonId = list(RegisterPersonInfo.objects.filter(id__gt=0))
    paymentId = list(PaymentInfo.objects.filter(paymentID__gt=0))
    decisionId = list(DecisionInfo.objects.filter(id__gt=0))

    #print(gurdians, "for relations")
  
    results = {'personInfos': personInfos, 'relationforPerson': relationforPerson, 'relations' : relations, 'jobID' : jobId, 'targetId': targetID, 'draftId': draftID, 'kannaiId': kannaiID, 'reReasonId': reReasonId, 'registerPersonId': registerPersonId, 'paymentId': paymentId, 'decisionId': decisionId}
    return render(request, 'app/second.html',results)


