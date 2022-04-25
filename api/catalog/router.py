from rest_framework import routers

from api.catalog.views import RegionViewSet, DistrictViewSet, LocalityViewSet, TerritorialAffiliationViewSet, \
    LanguageViewSet, ClassRoomView, SubjectView

router = routers.DefaultRouter()

router.register('region', RegionViewSet)
router.register('district', DistrictViewSet)
router.register('locality', LocalityViewSet)
router.register('territorial', TerritorialAffiliationViewSet)
router.register('language', LanguageViewSet)
router.register('classroom', ClassRoomView)
router.register('subject', SubjectView)