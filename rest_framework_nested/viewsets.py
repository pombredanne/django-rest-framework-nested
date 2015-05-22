__author__ = 'jrparks'
from rest_framework import viewsets
import mixins


class ModelViewSet(mixins.NestedListModelMixin,
                   viewsets.ModelViewSet):
    """
    A nested viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass