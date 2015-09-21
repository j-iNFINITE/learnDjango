import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()
from west.models import Character
def add_Character(name):
    C = Character.objects.get_or_create(name=name)
    return print(C)
def pu():
    add_Character('Vamei')
    add_Character('Django')
    add_Character('John')
if __name__=='__main__':
    print('aa')
    pu()
