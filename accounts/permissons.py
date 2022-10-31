from rest_framework.permissions import BasePermission
from .models import Role, UserRole
from main.models import Blog


class DirectorPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            role = UserRole.objects.get(user=request.user)
            user_role = Role.objects.get(name='director')
            return role.id == user_role.id
        except:
            return False
            
        