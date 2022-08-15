from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from datetime import date
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return render(request, 'demoapp/index.html')


def l3(request):
    return render(request, 'demoapp/l3.html')


def admin(request):
    return render(request, 'demoapp/adminlogin.html')


def l1(request):
    return render(request, 'demoapp/l1.html')

def tbooking(request):
    return render(request, 'demoapp/tbooking.html')


def treg(request):
    return render(request, 'demoapp/t1.html')


def l2(request):
    return render(request, 'demoapp/l2.html')


def l0(request):
    return render(request, 'demoapp/l0.html')


def l20(request):
    return render(request, 'demoapp/l20.html')


def l30(request):
    return render(request, 'demoapp/l30.html')


def insurance(request):
    return render(request, 'demoapp/insurance.html')

def drivers(request):
    return render(request, 'demoapp/driver.html')


def map(request):
    return render(request, 'demoapp/map.html')


def adminpage(request):
    return render(request, 'demoapp/admin_page.html')


def viewresort(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, image, name, detail, rent, location FROM `addresort`"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/admin_view_resort.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/admin_view_resort.html', {'records': records})

def editresort(request):
    rid = request.POST['rid']
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, image, name, detail, rent, location FROM `addresort` where id='" + rid + "'"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/editresort.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/editresort.html', {'records': records})


def updateresort(request):
    rid = request.POST['rid']

    name = request.POST['name']
    detail = request.POST['detail']
    rent = request.POST['rent']
    location = request.POST['location']
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    q = "update addresort set name='" + name + "',detail='" + detail + "',rent='" + rent + "',location='" + location + "' where id='" +rid + "'"
    mycursor.execute(q)
    mydb.commit()
    query = "SELECT id, image, name, detail, rent, location FROM `addresort` where id='" + rid + "'"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/editresort.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/admin_view_resort.html', {'records': records})

def deleteresort(request):
    rid = request.POST['rid']
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    q = "delete from addresort where id='" + rid + "'"
    mycursor.execute(q)
    mydb.commit()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, image, name, detail, rent, location FROM `addresort` where id='" + rid + "'"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/admin_view_resort.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/admin_view_resort.html', {'records': records})

def vehicles(request):
    return render(request, 'demoapp/vehicle.html')


def agency(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,status FROM agency_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/agency_approval.html', {'mes': 'no courses found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/agency_approval.html', {'records': records})


def agencyapproval(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    id = request.POST["uid"]
    # st1 = request.POST["st1"]
    s = "Accepted"
    s1 = "Rejected"

    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update agency_reg set status ='" + s + "' where id =" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,status FROM agency_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/agency_approval.html', {'records': records})
        elif request.POST.get("status1"):
            query = "update agency_reg set status ='" + s1 + "' where id=" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,status FROM agency_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/agency_approval.html', {'records': records})


# return render(request, 'demoapp/agency_approval.html')

def user(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,status FROM user_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/user_approval.html', {'mes': 'no courses found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/user_approval.html', {'records': records})


def userapproval(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    id = request.POST["uid"]
    # st1 = request.POST["st1"]
    s = "Accepted"
    s1 = "Rejected"

    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update user_reg set status ='" + s + "' where id =" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,status FROM user_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/user_approval.html', {'records': records})
        elif request.POST.get("status1"):
            query = "update user_reg set status ='" + s1 + "' where id=" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,status FROM user_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/user_approval.html', {'records': records})
    return render(request, 'demoapp/user_approval.html')


def driver(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,licensenumber,status FROM driver_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/driver_approval.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/driver_approval.html', {'records': records})

    # return render(request,'demoapp/driver_approval.html')


def driverapproval(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    id = request.POST["uid"]
    # st1 = request.POST["st1"]
    s = "Accepted"
    s1 = "Rejected"
    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update driver_reg set status ='" + s + "' where id =" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,licensenumber,status FROM driver_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/driver_approval.html', {'records': records})
        elif request.POST.get("status1"):
            query = "update driver_reg set status ='" + s1 + "' where id=" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,licensenumber,status FROM driver_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/driver_approval.html', {'records': records})
    return render(request, 'demoapp/driver_approval.html')


def feedback(request):
    return render(request, 'demoapp/feedback.html')


def booking(request):
    return render(request, 'demoapp/booking.html')

def userlogin(request):
    return render(request, 'demoapp/user.html')


def staff(request):
    return render(request, 'demoapp/staff.html')

def addresort(request):
    return render(request, 'demoapp/addresort.html')


def resort(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, image, name, detail, rent, location FROM `addresort`"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/resort.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/resort.html', {'records': records})

def tr_resort(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, image, name, detail, rent, location FROM `addresort`"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/tr_resort.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/tr_resort.html', {'records': records})


def aresort(request):
    if request.method == "POST" and request.FILES['img']:
        #i = request.POST["img"]
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        n = request.POST["name"]
        d = request.POST["detail"]
        r = request.POST["rent"]
        l = request.POST["location"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into addresort(image, name, detail, rent, location) values('" + uploaded_file_url + "','" + n + "','" + d + "','" + r + "','" + l + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'demoapp/addresort.html', {'msg': 'Registration sucessfull'})


def view_resort(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, image, name, detail, rent, location FROM `addresort`"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_resort.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/view_resort.html', {'records': records})

def vehicle(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, image,name, number, arrival, destination FROM car"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_vehicle.html', {'mes': 'no car found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/view_vehicle.html', {'records': records})


def vuser(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,status FROM user_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_user.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/view_user.html', {'records': records})
    # return render(request, 'demoapp/view_user.html')


def vdriver(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,licensenumber,status FROM driver_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_driver.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/view_driver.html', {'records': records})

def view_driver(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,licensenumber,status FROM driver_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/drivers.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/drivers.html', {'records': records})


def vtravel(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,status FROM treg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_travel.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/view_travel.html', {'records': records})

def view_travel(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,status FROM treg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_travelagency.html', {'mes': 'no Users found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/view_travelagency.html', {'records': records})



def travel(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, address, pincode, phone, email,status FROM user_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/travel_approval.html', {'mes': 'no courses found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/travel_approval.html', {'records': records})


def travelapproval(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    id = request.POST["uid"]
    # st1 = request.POST["st1"]
    s = "Accepted"
    s1 = "Rejected"
    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update treg set status ='" + s + "' where id =" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,status FROM treg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/travel_approval.html', {'records': records})
        elif request.POST.get("status1"):
            query = "update treg set status ='" + s1 + "' where id=" + id + " "
            mycursor.execute(query)
            mydb.commit()
            query1 = "SELECT id, name, address, pincode, phone, email,status FROM treg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            return render(request, 'demoapp/travel_approval.html', {'records': records})
    return render(request, 'demoapp/travel_approval.html')


def trvl(request):
    return render(request, 'demoapp/travel.html')



def tl(request):
    return render(request, 'demoapp/tlogin.html')


def book(request):
    return render(request, 'demoapp/book.html')


def travels(request):
    return render(request, 'demoapp/travel.html')


def tlogin(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["Password"]
        s = "Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "select * from treg where email='" + u + "' and password='" + p + "'and status='" + s + "' "
        mycursor.execute(q)
        mycursor.fetchall()
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/tlogin.html', {'msg': 'invalid username or password'})
        else:
            return render(request, 'demoapp/travel.html')


def alogin(request):
    uname = request.POST["username"]
    pas = request.POST["password"]
    print(uname + pas)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from admin where username='" + uname + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/adminlogin.html', {'mes': 'invalid username and password'})
    else:
        return render(request, 'demoapp/admin_page.html')


def user_signup(request):
    if request.method == "POST":
        n = request.POST["Name"]
        a = request.POST["address"]
        p = request.POST["pincode"]
        ph = request.POST["phonenumber"]
        e = request.POST["email"]
        psw = request.POST["password"]
        status = "Not Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into user_reg(`name`, `address`, `pincode`, `phone`, `email`, `password`, `status`) values('" + n + "','" + a + "'," + p + "," + ph + ",'" + e + "','" + psw + "','" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'demoapp/l1.html', {'msg': 'Registration sucessfull'})


def tregg(request):
    if request.method == "POST":
        n = request.POST["Name"]
        a = request.POST["address"]
        p = request.POST["pincode"]
        ph = request.POST["phonenumber"]
        e = request.POST["email"]
        psw = request.POST["password"]
        status = "Not Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into treg(`name`, `address`, `pincode`, `phone`, `email`, `password`, `status`) values('" + n + "','" + a + "'," + p + "," + ph + ",'" + e + "','" + psw + "','" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'demoapp/treg.html', {'msg': 'Registration sucessfull'})


def driver_signup(request):
    if request.method == "POST":
        n = request.POST["name"]
        a = request.POST["address"]
        p = request.POST["pincode"]
        ph = request.POST["phonenumber"]
        e = request.POST["email"]
        l = request.POST["licencenumber"]
        psw = request.POST["password"]
        status = "Not Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into driver_reg(`name`, `address`, `pincode`, `phone`, `email`, `licensenumber`, `password`, `status`) values('" + n + "','" + a + "'," + p + "," + ph + ",'" + e + "','" + l + "','" + psw + "','" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'demoapp/l2.html', {'msg': 'Registration sucessfull'})


def agency_signup(request):
    if request.method == "POST":
        n = request.POST["agencyname"]
        a = request.POST["agencyaddress"]
        p = request.POST["pincode"]
        ph = request.POST["phonenumber"]
        e = request.POST["email"]
        psw = request.POST["password"]
        status = "Not Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into agency_reg(`name`, `address`, `pincode`, `phone`, `email`, `password`, `status`) values('" + n + "','" + a + "'," + p + "," + ph + ",'" + e + "','" + psw + "','" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'demoapp/l3.html', {'msg': 'Registration sucessfull'})


def user_login(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["Password"]
        s = "Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "select * from user_reg where email='" + u + "' and password='" + p + "'and status='" + s + "' "
        mycursor.execute(q)
        mycursor.fetchall()
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/l0.html', {'msg': 'invalid username or password'})
        else:
            v = "select email from user_reg where email='" + u + "' and password='" + p + "'and status='" + s + "' "
            mycursor.execute(v)
            ((u,),) = mycursor.fetchall()
            vw = "select name from user_reg where email='" + u + "' and password='" + p + "'and status='" + s + "' "
            mycursor.execute(vw)
            ((ue,),) = mycursor.fetchall()
            request.session['username'] = u
            request.session['useremail'] = ue
            print(u)
            return render(request, 'demoapp/user.html')


def driver_login(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["Password"]
        s = "Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "select * from driver_reg where email='" + u + "' and password='" + p + "'and status='" + s + "' "
        mycursor.execute(q)
        mycursor.fetchall()
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/l20.html', {'msg': 'invalid username or password'})
        else:
            return render(request, 'demoapp/driver.html')


def agency_login(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["Password"]
        s = "Accepted"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "select * from agency_reg where email='" + u + "' and password='" + p + "'and status='" + s + "' "
        mycursor.execute(q)
        mycursor.fetchall()
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/l30.html', {'msg': 'invalid username or password'})
        else:
            return render(request, 'demoapp/staff.html')


def tinsurance(request):
    t = request.POST["travel"]
    u = request.POST["startdate"]
    v = request.POST["enddate"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    q = "insert into insurance values('" + t + "','" + u + "','" + v + "')"
    mycursor.execute(q)
    conn.commit()
    return render(request, 'demoapp/driver.html')


def payment(request):
    id = request.POST["rid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from payment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/payment.html', {'mes': 'Transaction Error'})
    else:
        query = "SELECT id, image, name, detail, rent, location FROM `addresort` where id= " + id + ""
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/payment.html', {'mes': 'Transaction Error'})
        else:
            records = mycursor.fetchall()

            return render(request, 'demoapp/resortbooking.html', {'records': records})


def cpayment(request):
    id = request.POST["rid"]
    return render(request, 'demoapp/payment.html', {'id': id})


def flight(request):
    if request.method == "POST" and request.FILES['img']:
        n = request.POST["name"]
        #i = request.POST["img"]
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        d = request.POST["departure"]
        r = request.POST["arrival"]
        l = request.POST["destination"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into flight (name, image, departure, arrival, destination) values('" + n+ "','" + uploaded_file_url + "','" + d + "' ,'" + r + "','" + l + "')"
        mycursor.execute(q)
        mydb.commit()
    return render(request, 'demoapp/flight.html', {'msg': 'Registration sucessfull'})

def flight_view(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name,image, departure, arrival, destination FROM flight"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/flight_view.html', {'mes': 'no Flight found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/flight_view.html', {'records': records})




def fpayment(request):
    id = request.POST["fid"]
    return render(request, 'demoapp/fpayment.html', {'id': id})


def flightpayment(request):
    id = request.POST["fid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from fpayment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/fpayment.html', {'mes': 'Transaction Error'})
    else:
        query = "SELECT id,name, image, departure, arrival, destination FROM flight where id= " + id + ""
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/fpayment.html', {'mes': 'Transaction Error'})
        else:
            records = mycursor.fetchall()

            return render(request, 'demoapp/flightbooking.html', {'records': records})


def train(request):
    if request.method == "POST" and request.FILES['img']:
        n = request.POST["name"]
       # i = request.POST["img"]
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        d = request.POST["departure"]
        r = request.POST["arrival"]
        l = request.POST["destination"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into train (name, image, departure, arrival, destination)values('" + n  + "','" + uploaded_file_url + "','" + d + "','" + r + "','" + l + "')"
        mycursor.execute(q)
        mydb.commit()
    return render(request, 'demoapp/train.html', {'msg': 'Registration sucessfull'})

def train_view(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT * FROM train"
    mycursor.execute(query)
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/train_view.html', {'mes': 'no Train found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/train_view.html', {'records': records})


def tpayment(request):
    id = request.POST["tid"]
    return render(request, 'demoapp/tpayment.html', {'id': id})

def trainpayment(request):
    id = request.POST["tid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from tpayment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/tpayment.html', {'mes': 'Transaction Error'})
    else:
        query = "SELECT * FROM train where id= " + id + ""
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/tpayment.html', {'mes': 'Transaction Error'})
        else:
            records = mycursor.fetchall()

            return render(request, 'demoapp/trainbooking.html', {'records': records})

def cruiser(request):
    if request.method == "POST"and request.FILES['img']:
        n = request.POST["name"]
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #i = request.POST["img"]
        d = request.POST["departure"]
        r = request.POST["arrival"]
        l = request.POST["destination"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into cruiser (name, image, departure, arrival, destination)values('" + n + "','" + uploaded_file_url + "','" + d + "','" + r + "','" + l + "')"
        mycursor.execute(q)
        mydb.commit()
    return render(request, 'demoapp/cruiser.html', {'msg': 'Registration sucessfull'})

def cruiser_view(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT * FROM cruiser"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/cruiser_view.html', {'mes': 'no ship found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/cruiser_view.html', {'records': records})



def spayment(request):
    id = request.POST["cid"]
    return render(request, 'demoapp/spayment.html', {'id': id})

def shippayment(request):
    id = request.POST["cid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from spayment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/spayment.html', {'mes': 'Transaction Error'})
    else:
        query = "SELECT * FROM cruiser where id= " + id + ""
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/spayment.html', {'mes': 'Transaction Error'})
        else:
            records = mycursor.fetchall()
            return render(request, 'demoapp/shipbooking.html', {'records': records})

def car(request):
    if request.method == "POST"and request.FILES['img']:
        n = request.POST["name"]
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #i = request.POST["img"]
        d = request.POST["number"]
        r = request.POST["arrival"]
        l = request.POST["destination"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into car (name, image, number, arrival, destination)values('" + n + "','" + uploaded_file_url + "','" + d + "','" + r + "','" + l + "')"
        mycursor.execute(q)
        mydb.commit()
    return render(request, 'demoapp/car.html', {'msg': 'Registration sucessfull'})

def capayment(request):
    id = request.POST["carid"]
    return render(request, 'demoapp/cpayment.html', {'id': id})


def car_view(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id, name, image, number, arrival, destination FROM car"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/car_view.html', {'mes': 'no car found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/car_view.html', {'records': records})


def carpayment(request):
    id = request.POST["carid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from carpayment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/cpayment.html', {'mes': 'Transaction Error'})
    else:
        query = "SELECT  id,name, image, number, arrival, destination FROM car where id= " + id + ""
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/cpayment.html', {'mes': 'Transaction Error'})
        else:
            records = mycursor.fetchall()
            return render(request, 'demoapp/carbooking.html', {'records': records})





def addpack(request):
    if request.method == "POST":
        n = request.POST["name"]
        i = request.POST["route"]
        d = request.POST["location"]
        r = request.POST["itinerary"]
        l = request.POST["cost"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
        q = "insert into tpack (name, route, location, itinerary, cost)values('" + i + "','" + n + "','" + d + "','" + r + "','" + l + "')"
        mycursor.execute(q)
        mydb.commit()
    return render(request, 'demoapp/add_pack.html', {'msg': 'Registration sucessfull'})

def package(request):
    return render(request, 'demoapp/view_pack.html')


def viewpack(request):
    t1 = request.POST["location"]
    print(t1)
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query10 = "select id,name,route,location,itinerary,cost from tpack where location='" +t1+"' "
    mycursor.execute(query10)
   # records = mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_pack.html', {'mes': 'no package found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/view_pack.html', {'record': records})


def viewpack1(request):
    id = request.POST["pid"]
    u = request.session['username']
    dat=date.today()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
    mycursor = mydb.cursor()
    query = "SELECT id,name,cost FROM tpack where id='" + id + "'"
    mycursor.execute(query)
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/view_pack.html', {'mes': 'no package found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'demoapp/package _booking.html', {'records': records,'username':u,'dat':dat})


def packagebooking(request):
    if request.method == "POST":
        u = request.session['username']
        ue = request.session['useremail']
        i = request.POST['id']
        j = request.POST['pk_name']
        k = request.POST['cost']
        np = request.POST["person"]
        d = request.POST["date"]
        v = request.POST["jdate"]
        print(u+" " +i+" "+j+" "+k+" "+np+" "+d+" "+v)
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        mycursor = mydb.cursor()
      #  p = "select (`id`,`name`, `cost`) from tpack  "
        vw = "select id from user_reg where email='" + u + "' and name='" + ue + "'"
        mycursor.execute(vw)
        ((jd,),) = mycursor.fetchall()
        mydb.commit()
        request.session['id'] = i
        request.session['pk_name'] = j
        request.session['cost'] = k
        request.session['person'] = np
        request.session['date'] = d
        request.session['jdate'] = v
        return render(request, 'demoapp/ppayment.html', {'msg': 'Registration sucessfull','uid':jd,'pid':i})


def packagepayment(request):
    pid = request.POST["pid"]
    uid = request.POST["uid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    b = "select balance from ppayment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(b)
    ((ba,),) = mycursor.fetchall()
    print(ba)
    u = request.session['useremail']
    i = request.session['id']
    j = request.session['pk_name']
    c = request.session['cost']
    w = request.session['person']
    d = request.session['date']
    v = request.session['jdate']
    print(c, w)
    qw = int(c) * int(w)
    qww = str(qw)
    print(qww)
    if ba >= qw:
        q = "insert into packagebooking(username,packageId,name,cost,noperson,date,djourney)  values('" + u + "','" + i + "','" + j + "','" + qww+ "','" + w + "','" + d + "','" + v + "')"
        mycursor.execute(q)
        conn.commit()
        nb = ba - qw
        newbal = str(nb)
        print()
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="voyage_venture")
        query = "update ppayment set balance = '" + newbal + "' "
        mycursor.execute(query)
        mydb.commit()
        del request.session['id']
        del request.session['pk_name']
        del request.session['cost']
        del request.session['person']
        del request.session['date']
        del request.session['jdate']
        return render(request, 'demoapp/booked_package.html', {'u': u, 'i': i, 'j': j, 'qw': qww, 'w': w, 'd': d, 'v': v})
    else:
        return render(request, 'demoapp/ppayment.html', {'mes': 'Transaction Error'})


def viewbkd(request):
    u = request.session['username']
    ue = request.session['useremail']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    b =" SELECT `username`, `packageId`, `name`, `cost`, `noperson`, `date`, `djourney` FROM packagebooking"
    mycursor.execute(b)
    record = mycursor.fetchall()
    return render(request, 'demoapp/viewbkd_package.html', {'records': record})

def carrpayment(request):
    id = request.POST["carid"]
    return render(request, 'demoapp/crpayment.html', {'id': id})

def crrpayment(request):
    id = request.POST["carid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from crpayment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/crpayment.html', {'mes': 'Transaction Error'})
    else:
        query = "SELECT  id,name, image, number, arrival, destination FROM car where id= " + id + ""
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/crpayment.html', {'mes': 'Transaction Error'})
        else:
            records = mycursor.fetchall()
            return render(request, 'demoapp/vehiclebooking.html', {'records': records})

def tresortbook(request):
    id = request.POST["rid"]
    return render(request, 'demoapp/trpayment.html', {'id': id})

def t_payment(request):
    id = request.POST["rid"]
    cname = request.POST["Name"]
    num = request.POST["number"]
    exp = request.POST["expiry"]
    cvv = request.POST["cvv"]
    pas = request.POST["password"]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voyage_venture')
    mycursor = conn.cursor()
    query = "select * from t_payment where name='" + cname + "' and number='" + num + "' and expiry='" + exp + "' and cvv='" + cvv + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request, 'demoapp/t_payment.html', {'mes': 'Transaction Error'})
    else:
        query = "SELECT id, image, name, detail, rent, location FROM `addresort` where id= " + id + ""
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            return render(request, 'demoapp/t_payment.html', {'mes': 'Transaction Error'})
        else:
            records = mycursor.fetchall()
            return render(request, 'demoapp/tresortbooking.html', {'records': records})