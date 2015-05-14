# django-rest-framework-nested
Work in progress for nested support for django-rest-framework


Installation
------------

```pip install ```


Quickstart
----------

#### settings.py
```
REST_FRAMEWORK = {
    ...
    'DEFAULT_FILTER_BACKENDS': ('rest_framework_nested_test.filters.NestedFilterBackend',)
    ...
}
```

#### urls.py
```
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from django.conf.urls import url, include, patterns
import views
...

api_router = routers.DefaultRouter()

api_router.register(r'parent', views.ParentViewSet)
api_parent_router = nested_routers.NestedSimpleRouter(api_router, 'parent', lookup='parent')
api_parent_router.register(r'child', views.ChildViewSet)
...

urlpatterns = patterns(''
    ...
    url(r'^api/', include(api_router.urls)),
    ...
)
```

#### serializers.py
```
from rest_framework import serializers
from rest_framework_nested import serializers as nested_serializers
import models
...

class ChildSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    class Meta:
        model = models.Child


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Parent

    values = ChildSerializer(many=True, required=False, read_only=True)
```

#### views.py
```
from rest_framework import viewsets
import models, serializers
...

class ParentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Parent to be viewed or edited.
    """
    queryset = models.Parent.objects.get_queryset()
    serializer_class = serializers.ParentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Child to be viewed or edited.
    """
    queryset = models.Child.objects.get_queryset()
    serializer_class = serializers.ChildSerializer
```

License
=======

This package is licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
and can undestand more at http://choosealicense.com/licenses/apache/ on the
sidebar notes.

Apache Licence v2.0 is a MIT-like licence. This means, in plain English:
- Its trully open source
- You can use it as you wish, for money or not
- You can sublicence it (change the licence!!)
- This way, you can even use it on your closed-source project
As long as:
- You cannot use the authors name, logos, etc, to endorse a project
- You keep the authors copyright notices where this code got used, even on your closed-source project
(come on, even Microsoft kept BSD notices on Windows about its TCP/IP stack :P)