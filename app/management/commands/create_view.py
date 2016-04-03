from django.core.management.base import BaseCommand, CommandError
import importlib
import os
import re
import inspect

IMPORTS = {
        "CreateView": "django.views.generic.edit",
        "FormView": "django.views.generic.edit",
        "UpdateView": "django.views.generic.edit",
        "DeleteView": "django.views.generic.edit",
        "TemplateView": "django.views.generic.base",
        }


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('view_name', nargs='+', type=str)
        parser.add_argument('url_name', nargs="+", type=str)
        # Named (optional) arguments
        parser.add_argument('--type', '-t',
            action='store',
            dest='view_type',
            default='fbv',
            type=str,
            choices=["fbv", "CreateView", "TemplateView"],
            help='Delete poll instead of closing it')

    def handle(self, *args, **options):
        view_path = options['view_name'][0].split('.')
        self.view_name = view_path[-1]
        try:
            module = importlib.import_module('.'.join(view_path[:-1]))
        except ImportError:
            raise
        view_exists = hasattr(module, self.view_name)
        view_type = options['view_type']
        if not view_exists:
            with open(inspect.getsourcefile(module), "a") as myfile:
                myfile.write("\n\n")
                if not hasattr(module, view_type) and IMPORTS.get(view_type) is not None:
                    myfile.write("### AUTOMATED IMPORT. MOVE THIS TO TOP OF THE FILE###\n")
                    myfile.write("from {0} import {1}\n\n".format(IMPORTS[view_type], view_type))
                myfile.write(getattr(self, view_type)())
        else:
            raise CommandError('View "{0}" already exists'.format(self.view_name))
        print "Success"

    def CreateView(self):
        return_data = "class {0}(CreateView):"+\
        "\n\ttemplate_name = '{0}.html'"+\
        "\n\tsuccess_url = '<success_url>'"+\
        "\n\t# form_class = <SubstituteYourForm>"
        return return_data.format(self.view_name)

    def fbv(self):
        return "def {0}(request):\
        \n\ttemplate_name='{0}.html'\
        \n\treturn render(template_name)".format(self.view_name)

    def TemplateView(self):
        return_data = "class {0}(TemplateView):"+\
        "\n\ttemplate_name='{0}.html'"+\
        "\n\n\tdef get_context_data(self, **kwargs):"+\
        "\n\t\tcontext = super({0}, self).get_context_data(**kwargs)"+\
        "\n\t\treturn context"
        return return_data.format(self.view_name)
