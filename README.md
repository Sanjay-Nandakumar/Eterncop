# Eterncop
**Eterncop is a computer vision project done for learning the purpose of gender and age detection by capturing the visuals of the human face in real-time. The front end is built using Django and the back end has been fed with various deep learning libraries such as OpenCV, Keras, and Pygame**

[![Capture.png](https://i.postimg.cc/HksLHDmQ/Capture.png)](https://postimg.cc/GHVRJfH2)

## Requirements

* Python 2.7+ or Python 3.4+ (Whatever is supported by your version of Django)

## Installation

Use the requirements.txt [pip](https://pip.pypa.io/en/stable/) to install project.

```bash
pip install -r requirements.txt
```


## Format Support

* XML: lxml 3 (http://lxml.de/) and defusedxml (https://pypi.python.org/pypi/defusedxml)
* YAML: pyyaml (http://pyyaml.org/)
* binary plist: biplist (https://bitbucket.org/wooster/biplist)


What's It Look Like?
A basic example looks like:

```
# myapp/api.py
# ============
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# urls.py
# =======
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  
from django.urls import path  
from myproject import views  
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('hello/', views.hello,name="hello"), 
    path('output/', views.output,name="output"),   
    path('output2/', views.output2,name="output2"),   
    url(r'^$',views.index)
]  
```

## Execution

Use the django command to execute project.

```bash
python manage.py runserver
```

## Reference Material
* https://django-tastypie.readthedocs.io/en/latest/
* https://github.com/django-tastypie/django-tastypie/tree/master/tests/basic shows basic usage of tastypie
* http://en.wikipedia.org/wiki/REST
* http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
* http://www.ietf.org/rfc/rfc2616.txt
* http://jacobian.org/writing/rest-worst-practices/
