from rest_framework import  viewsets, permissions
from .models import Alternative
from .serializers import AlternativeSerializer


class AlternativeViewSet(viewsets.ModelViewSet):
    serializer_class = AlternativeSerializer
    permissions = [permissions.AllowAny]
    queryset = Alternative.objects.filter(published=True)

    # def get_queryset(self):
    #     """Форма запроса из базы"""
    #     alternative = Alternative.objects.filter(published=True)
    #     return alternative


# class AlternativeListView(generics.ListAPIView):
#     """Вывод всех выбранных учебников"""
#     serializer_class = AlternativeListSerializers
#
#     def get_queryset(self):
#         """Форма запроса из базы"""
#         alternative = Alternative.objects.filter(published=True)
#         return alternative
#
#
# class AlternativeCreateView(generics.CreateAPIView):
#     """Добавление выбранного алтернативного учебника"""
#     serializer_class = AlternativeCreateSerializers
#
#
# class AlternativeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """Вывод одного выбранного учебника, редактирование, удаление"""
#     serializer_class = AlternativeDetailSerializer
#
#     def get_queryset(self):
#         """Форма запроса из базы"""
#         alternative = Alternative.objects.filter(published=True)
#         return alternative
