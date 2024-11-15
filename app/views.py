from django.shortcuts import render,redirect
from . import db,services
from bson import ObjectId

# Create your views here.
def login(req):
    if(req.method == "POST"):
        qury = req.POST
        email = qury.get("email")
        password = qury.get("password") 
        user = db.coll.find_one({"email":email,"password":password})
        print(user,"user")
        
        if(not user):
            return redirect("reg")
        else:
            id = str(user['_id'])
            print("userId",id)
            req.session["userId"] = id
            print(req.session,"session")
            return redirect("home")
    return render(req,"login.html")

def home(req):
    sessionId = req.session.get("userId")
    print("sessionID",sessionId)
    if(sessionId):
        adminOBJID = ObjectId(sessionId)
        print(adminOBJID,"userId")
        user = db.coll.find_one({"_id":adminOBJID})
        print("user",user)
        return render(req,"home.html",{"user":user})
    else:
        return redirect("login")

def reg(req):
    if(req.method == "POST"):
        qury = req.POST
        email = qury.get("email")
        password = qury.get("password")
        confirmPassword = qury.get("confirmPassword")
        if(confirmPassword == password):
            admins = db.coll.insert_one({"email":email,"password":password,"confirmPassword":confirmPassword})
            print(admins,"admins")
            return redirect("login")
    return render(req,"reg.html")

def logout(req):
    print("logout")
    del req.session["userId"]
    print(req.session.keys())
    return redirect("login")
    