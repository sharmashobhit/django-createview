# django-createview
ROR type view creation for Django

This is a WIP, this project aims at creation of ROR type auto generated views in Django.

#### Sample Code
```
python manage.py create_view app.views.SampleViewName --type="CreateView"
```

This will generate a view with required imports.

The available views are
* CreateView
* TemplateView
* Function Based View
