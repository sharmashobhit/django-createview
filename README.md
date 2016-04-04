# django-createview
ROR type view creation for Django

This is a WIP, this project aims at creation of ROR type auto generated views in Django.

#### Sample Code
```
python manage.py create_view app.views.SampleViewName --type="CreateView"
```

#### This will generate following code:
```
### AUTOMATED IMPORT. MOVE THIS TO TOP OF THE FILE###
from django.views.generic.edit import CreateView

class SampleViewName(CreateView):
      template_name = 'SampleViewName.html'
      success_url = '<success_url>'
      # form_class = <SubstituteYourForm>
```

This will generate a view with required imports.

The available views are
* CreateView
* TemplateView
* Function Based View
