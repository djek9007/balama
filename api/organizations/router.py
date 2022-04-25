# # #app order
from rest_framework import routers
from api.organizations.views import OrganizationsViewSet, MetodicalMemberViewSet, MethodicalAssociationViewSet

router = routers.DefaultRouter()

router.register('', OrganizationsViewSet)
router.register('metodical/', MethodicalAssociationViewSet)
router.register('metodical/member/', MetodicalMemberViewSet)