from django.shortcuts import render

# Create your views here.
from app.models import *

def equi_joins(request):
    LEDO=Emp.objects.select_related('deptno').all()
    d={'LEDO':LEDO}
    return render(request,'equi_joins.html',d)