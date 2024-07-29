from django.shortcuts import render

# Create your views here.
from app.models import *

def equi_joins(request):
    LEDO=Emp.objects.select_related('deptno').all()
    LEDO=Emp.objects.select_related('deptno').filter(ename='SCOTT')
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    LEDO=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    LEDO=Emp.objects.select_related('deptno').filter(mgr=1111)
    d={'LEDO':LEDO}
    return render(request,'equi_joins.html',d)


def em_dp_mr(request):
    LEDMO=Emp.objects.select_related('deptno','mgr').all()
    
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(ename='CLARK')
    d={'LEDMO':LEDMO}
    return render(request,'em_dp_mr.html',d)










