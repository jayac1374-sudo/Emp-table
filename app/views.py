from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length
from django.db.models import Prefetch
# Create your views here.
def insert_dept(reuest):
    dno=int(input('enter the deno: '))
    dn=input('enter the dname: ')
    dlo=input('enter the dloc:  ')
    TDO=Dept.objects.get_or_create(dno=dno,dn=dn,dlo=dlo)
    if TDO[1]:
        return HttpResponse('New DEPT object is created')
    else:
        return HttpResponse(' DEPT  is already created') 
    

def insert_emp(request):
    dno=int(input('Enter Dept No: '))
    LDO=Dept.objects.filter(deptNo=dno)
    if LDO:
        DO=LDO[0]
        eno=int(input('Enter Employee No: '))
        en=input('Name of the Employee: ')
        jb=input('Job of the Employee: ')
        hd=input('Date of Hiring: ')
        s1=int(input('Salary of Employee: '))
        com=input("Commission of Employee: ")
        if com:
            com=int(com)
        else:
            com=None
        mngr=input('Enter employee number of manager: ')
        if mngr:
            LMO=Emp.objects.filter(empNo=int(mngr))
            if LMO:
                MO=LMO[0]
            else:
                MO=None
        else:
            MO=None
        TEO=Emp.objects.get_or_create(deptNo=DO, empNo=eno, ename=en, job=jb, hireDate=hd, sal=s1, comm=com, mgr=MO)
        if TEO[1]:
            return HttpResponse(f'{eno} is created')
        else:
            return HttpResponse(f'{eno} is already present')
    else:
        return HttpResponse('deptno is not present here')
    


def display_dept(request):
    QSLDO=Dept.objects.all()
    
    D={'QSLDO':QSLDO}
    return render(request, 'display_dept.html', D)


def display_emp(request):
    QSLEO=Emp.objects.all()
    
    QSLEO=Emp.objects.filter(comm__isnull=True)
    QSLEO=Emp.objects.filter(comm__isnull=False)
    
    QSLEO=Emp.objects.all()
    D={'QSLEO':QSLEO}
    return render(request, "display_emp.html", D)


def EmpToDeptJoin(request):
    QSLEDO=Emp.objects.select_related('deptNo').all()
    
    QSLEDO=Emp.objects.select_related('deptNo').filter(sal__gt=2000)
    QSLEDO=Emp.objects.select_related('deptNo').filter(deptNo__dName='Research')
    
    QSLEDO=Emp.objects.select_related('deptNo').all()
    D={'QSLEDO':QSLEDO}
    
    return render(request, 'EmpToDeptJoin.html',D)


def EmpToMgrJoin(request):
    QSLEMO=Emp.objects.select_related('mgr').all()
    
    QSLEMO=Emp.objects.select_related('mgr').filter(sal__gt=2000)
    QSLEMO=Emp.objects.select_related('mgr').filter(mgr__sal__gt=3000)
    
    QSLEMO=Emp.objects.select_related('mgr').filter(eName__startswith='B')
    QSLEMO=Emp.objects.select_related('mgr').filter(eName__endswith='g')
    QSLEMO=Emp.objects.select_related('mgr').filter(mgr__eName='Blake')
    
    QSLEMO=Emp.objects.select_related('mgr').filter(eName='King')
    QSLEMO=Emp.objects.select_related('mgr').filter(mgr__eName__contains='e')
    QSLEMO=Emp.objects.select_related('mgr').filter(eName__regex='^B\w+')
    QSLEMO=Emp.objects.select_related('mgr').filter(sal__gte=1600)
    QSLEMO=Emp.objects.select_related('mgr').filter(mgr__sal__lte=2975)
    QSLEMO=Emp.objects.select_related('mgr').filter(job='Salesman')
    QSLEMO=Emp.objects.select_related('mgr').filter(mgr__job='Manager')
    
    QSLEMO=Emp.objects.select_related('mgr').filter(deptNo__in=(10,20), sal__gte=1600)
    QSLEMO=Emp.objects.select_related('mgr').filter(Q(job='Salesman')|Q(mgr__deptNo=10))
    
    
    # QSLEMO=Emp.objects.select_related('mgr').all()
    D={'QSLEMO':QSLEMO}
    return render(request, 'EmpToMgrJoin.html', D)

def EmpToMgrDeptJoin(request):
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').all()
    
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').all().order_by(Length('mgr__eName'))
    
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(deptNo__dName='Research')
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(deptNo__loc='Chicago')
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(deptNo__deptNo=10)
    
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(mgr__ename__contains='e')
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(mgr__ename__startswith='k')
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(sal__gte=1600)
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(Q(job='Salesman')|Q(mgr__deptNo=10))
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter((Q(job='Salesman')|Q(mgr__deptNo=10)) & Q(eName__contains='e') )
    
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(Q(job='Salesman') & Q(mgr__deptNo=30))
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').filter(mgr__ename__regex='^\w+e$')
    QSLEDMO=Emp.objects.select_related('mgr','deptNo').all()
    D={'QSLEDMO':QSLEDMO}
    return render(request, 'EmpToMgrDeptJoin.html', D)


def DeptToEmpJoin(request):
    ADEO=Dept.objects.prefetch_related('emp_set').all()
    
    ADEO=Dept.objects.prefetch_related('emp_set').filter(dName='Research')
    ADEO=Dept.objects.prefetch_related('emp_set').filter(loc='New York')
    
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(sal__gte=1600))).filter(loc='New York')
    
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(sal__gte=1600))).all()
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(ename__contains='e'))).all()
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter((Q(job='Salesman')|Q(job='Manager')) & Q(sal__lte=4000)))).all()
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(empno=7369))).all()
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(comm__isnull=True))).all()
    
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(comm__isnull=False))).all()
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(deptNo=20))).all()
    ADEO=Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(empno=7369))).all()
    
    D={'ADEO':ADEO}
    return render(request, 'DeptToEmpJoin.html', D)
