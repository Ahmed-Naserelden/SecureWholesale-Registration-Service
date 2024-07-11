from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .settings import DATABASE_HOST
from django.contrib import messages
# Create your views here.
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId 
from bson import json_util

client = pymongo.MongoClient(f"mongodb://{DATABASE_HOST}:27017/")
db = client["mydb"]

# Start of the block
org_attrs = ['email', 'password', 'org_id', 'license_id', 'org_status', 'org_type', 'org_name', 'org_fin_id', 'finan_limit_from', 'finan_limit_to', 'bank_account', 'org_attch']
cust_attrs = ["org_id", "org_name","org_admin_id", "permission_id","user_status", "bus_user_id", "username", "email", "password", "user_attch"]
perm_attrs = ['email', 'password', 'perm_id', 'org_id', 'org_name', 'org_admin_id', 'user_status', 'super_admin', 'org_admin', 'merchant', 'service_agent' , 'field_agent', 'inventory_worker', 'consumer']

org_mand = ['email', 'password', 'org_id', 'license_id', 'org_status', 'org_type', 'org_name']
cust_mand = ["org_id", "org_admin_id", "permission_id", "user_status", "username", "email", "password", "user_attch"]
perm_mand = ['email', 'password', 'perm_id', 'org_id',  'org_admin_id', 'user_status', 'super_admin', 'org_admin',]
# End of the block

def json_perm_data(data):
    document = {}
    for attr in perm_attrs:
        document[attr] = data.get(attr)
    return json_util.loads(json_util.dumps(document))

def json_org_data(data):
    document = {}
    for attr in org_attrs:
        document[attr] = data.get(attr)
    return json_util.loads(json_util.dumps(document))

def json_cust_data(data):
    document = {}
    for attr in cust_attrs:
        document[attr] = data.get(attr)
    return json_util.loads(json_util.dumps(document))


def signin(request):
    if request.user.is_anonymous == False:
        return redirect(home)
    
    if request.method == 'POST':
    
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
            # pass
        else:
            messages.info(request, 'User is not Exist')

    return render(request, 'login.html')

def signup(request):
    if request.user.is_anonymous == False:
        return redirect(home)
    
    if request.method == 'POST':

        if request.POST['entity'] == 'organization':
            
            email, password = request.POST['email'], request.POST['password']
            
            data = json_org_data(request.POST)
            
            print(data)
            
            try:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                data.pop('password')
                try:
                    collection = db['organizations']
                    result = collection.insert_one(data)
                
                except:
                    messages.info(request, 'User Data Not Valid')
                    return render(request, 'register.html')
            
            except:
                messages.info(request, 'User is Exist')
                return render(request, 'register.html')

        if request.POST['entity'] == 'user':
            
            email, username, password = request.POST['email'], request.POST['username'], request.POST['password']
            
            data = json_cust_data(request.POST)
            
            print(data)
            
            try:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                data.pop('password')
                try:
                    collection = db['users']
                    result = collection.insert_one(data)
                
                except:
                    messages.info(request, 'User Data Not Valid')
                    return render(request, 'register.html')
            
            except:
                messages.info(request, 'User is Exist')
                return render(request, 'register.html')

        if request.POST['entity'] == 'permission':
            
            email, password = request.POST['email'], request.POST['password']
            
            data = json_perm_data(request.POST)
            
            
            # print(data)
            
            try:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                data.pop('password')
                try:
                    collection = db['permissions']
                    result = collection.insert_one(data)
                
                except:
                    messages.info(request, 'permission Data Not Valid')
                    return render(request, 'register.html')
            
            except:
                messages.info(request, 'permission is Exist')
                return render(request, 'register.html')



    return render(request, 'register.html')

def home(request):
    if request.user.is_anonymous:
        return redirect(signin)
    return render(request, 'home.html')

def signout(request):
    logout(request)
    return redirect(signin)


def error_404_view(request, exception):
    return render(request, '404.html', status=404)
