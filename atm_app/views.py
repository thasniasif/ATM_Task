from django.shortcuts import render,redirect,HttpResponse
import random
from .models import tb_atm,trans

# Create your views here.

def home(request):

    return render(request,'home.html')
def register(request):
    # u_accn="xxxxxxxxxx"
    if request.method == 'POST':
        # print("hi")
        u_fname = request.POST.get('fname')
        # print(u_fname)
        u_lname = request.POST.get("lname")
        u_email = request.POST.get("email")
        u_pwd=request.POST.get("password")
        u_phone = request.POST.get("phone")
        u_gender = request.POST.get("gender")

        s=tb_atm.objects.filter(password=u_pwd)
        # for i in s:
        #     print(i.fname)
        if s.count()>0:
            return HttpResponse("Password is already taken!!!")
        else:
            u_accn=random.randint(1000000001,9999999999)
            c=tb_atm.objects.filter(accn_num=u_accn)

            while(c.count()>0):
                u_accn = random.randint(1000000001, 9999999999)
                c = tb_atm.objects.filter(accn_num=u_accn)
                if (c.count()==0):
                    break

            if(c.count()==0):
                rec=tb_atm(accn_num=u_accn,fname=u_fname, lname=u_lname, email=u_email, password=u_pwd, phone=u_phone, gender=u_gender,amount='0')
                rec.save()
                # return HttpResponse("Thank You For Creating A bank Account Number is ",u_accn)
            rec = tb_atm.objects.filter(accn_num=u_accn, password=u_pwd)
            if rec:
                request.session["user"] = u_accn
                return redirect('dashboard')


        return redirect('dashboard')



    return render(request, 'register.html')




    # return render(request, 'register.html')


def login(request):

    if(request.method=='POST'):

        u_accn=request.POST.get("accn_num")
        u_pwd=request.POST.get("password")
        rec=tb_atm.objects.filter(accn_num=u_accn,password=u_pwd)
        # for i in rec:
        #     fname=i.fname
        if rec:
            request.session["user"]=u_accn
            operation='deposit'
            op=0
            return redirect('dashboard')


        else:
            return HttpResponse('Please enter valid Username or Password.')

        # return render(request,'dash')

    else:

        return render(request,'login.html')
# # def reg_dash(request):
# #     if 'reg_user' in request.session:
# #         reg_user=request.session["user"]
# #         s=tb_atm.objects.filter(accn_num=reg_user)
# #         context={
# #             'current_user' : reg_user,
# #             's' :s
# #
# #         }
# #         return render(request, 'base_login.html',context)
# #     else:
# #         return render(request,'reg_dash.html')
# #
def dashboard(request):
    # print(op)

    if 'user' in request.session:
        current_user=request.session["user"]
        s=tb_atm.objects.filter(accn_num=current_user)
        context={
            'current_user' : current_user,
            's' :s,
            'r' : 1

        }
        return render(request, 'base_login.html',context)
    else:
        return render(request,'dashboard.html')
def deposit(request,id):
    print("hi")
    # op=0
    print(id)
    if(request.method=='POST'):
        u_amnt = request.POST.get("amount")
        print(u_amnt)
        s = tb_atm.objects.get(id=id)

        int_amnt = int(s.amount)
        int_amnt += int(u_amnt)
        # if(int_amnt>=2000):
        s.amount=int_amnt
        s.save()
        t=trans(t_type='deposit',t_amount=u_amnt,p_id=s)
        t.save()
        # else:




        # rec=tb_atm(amount=int_amnt,instance=s)
        # rec.save()

    return redirect('d_dash')
def d_dash(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = tb_atm.objects.filter(accn_num=current_user)
        print(current_user)
        context = {
            'current_user': current_user,
            'deposit': 1,
            's': s

        }
        return render(request, 'base_login.html', context)
    else:
        return render(request, 'dashboard.html')


def w_btn(request):

    if 'user' in request.session:
        current_user=request.session["user"]
        s=tb_atm.objects.filter(accn_num=current_user)
        print(current_user)
        context={
            'current_user' : current_user,
            'withdraw' :1,
            's' : s

        }
        return render(request, 'base_login.html',context)
    else:
        return render(request,'dashboard.html')
    # return render(request, 'base_login.html', param)

def withdraw(request,id):
    op=1
    print("hi")
    if (request.method == 'POST'):
        u_amnt = request.POST.get("w_amount")
        print(u_amnt)
        s = tb_atm.objects.get(id=id)
        int_amnt = int(s.amount)
        int_amnt -= int(u_amnt)
        s.amount = int_amnt
        s.save()
        t = trans(t_type='withdraw', t_amount=u_amnt, p_id=s)
        t.save()
    return redirect('w_btn')
def balance(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = tb_atm.objects.filter(accn_num=current_user)
        # for i in s:
        #     x=i.id
        # print(x)
        context = {
            'current_user': current_user,
            'balance': 1,
            's': s
            # 'x' : x

        }
        return render(request, 'base_login.html', context)
    else:
        return render(request, 'dashboard.html')

def history(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = tb_atm.objects.filter(accn_num=current_user)
        # print(current_user)
        # print(s.id)
        for i in s:
            x=i.id
        print(type(x))
        # dataa=trans.objects.oderby()
        rec=trans.objects.filter(p_id=x).order_by('-t_date')
        # for i in rec:
        #     print(i.t_type)
        context = {
            'current_user': current_user,
            'history': 1,
            'id' : x,
            'rec' : rec,
            's' : s

        }
        return render(request, 'base_login.html', context)
    else:
        return render(request, 'dashboard.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('home')
    return redirect('home')


