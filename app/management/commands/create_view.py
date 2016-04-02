from django.core.management.base import BaseCommand, CommandError
import importlib
import os


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
        print args
        print options
        view_path = options['view_name'][0].split('.')
        view_name = view_path[-1]
        try:
            module = importlib.import_module('.'.join(view_path[:-1]))
        except ImportError:
            raise
        view_exists = hasattr(module, view_name)
        view_type = options['view_type']
        if not view_exists:
            with open('/'.join(view_path[:-1])+".py", "a") as myfile:
                myfile.write(getattr(self, view_type)(*args, **options))
        else:
            raise CommandError('View "{0}" already exists'.format(view_name))
        print "Success"

    def CreateView(self, *args, **options):
        assert False, options['view_type']

    def fbv(self, *args, **kwargs):
        return "def {0}(request):\
        \n\ttemplate_name='{0}.html'\
        \n\treturn render(template_name)"

    def TemplateView(self, *args, **kwargs):
        return "class {0}(TemplateView):\
        \n\ttemplate_name='{0}.html'\
        \n\n\tdef get_context_data(self, **kwargs):\
        \n\t\tcontext = super({0}, self).get_context_data(**kwargs)\
        \n\t\treturn context"
