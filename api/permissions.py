from rest_framework.permissions import BasePermission

# from organizations.models import Organization
# from catalog.models import District, Region
# from role.models import RegionRole, OrganizationRole
#
#
# class IsOrganizationAdmin(BasePermission):
#     """Permission for admin region"""
#     message = "Просмотр только своего организации"
#     # def has_object_permission(self, request, view, obj):
#     #     return request.user in obj.group.members.all() or obj.group.fonder == request.user
