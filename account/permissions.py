from rest_framework import permissions
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId 

class IsOwnerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        user = request.user
        if request.method == 'GET' or user.username == 'biruni@biruni.com':
            return True

        pk = view.kwargs.get('pk')
        print("pk, ", pk)

    
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mydb"]


        users_collection, organizations_collection, permissions_collection = \
        db['users'], db['organizations'], db['permissions']

        try:
            usr = users_collection.find_one({'email': user.username}, {'_id': 1})
            print("user, ", f'{usr["_id"]}')
            return pk == f'{usr["_id"]}'
        except:
            try:
                org = organizations_collection.find_one({'email': user.username}, {'_id': 1})
                print("org, ", f'{org["_id"]}')
                return pk == f'{org["_id"]}'
            except:
                try:
                    perm = permissions_collection.find_one({'email': user.username}, {'_id': 1})
                    print("perm, ", f'{perm["_id"]}')
                    return pk == f'{perm["_id"]}'
                except:
                    return False

        return False
    
class IsAdminToUpdate(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET' or request.user.username == 'biruni@biruni.com':
            return True
        
        return False
        