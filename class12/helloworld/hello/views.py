# Create your views here.
from django.http import HttpResponse
from django.template import context, loader
def howdy(request):
	t = loader.get_template('hello/howdy.html')
	d = {'greeting': 'hola', 'my_list': 'my_list'}
	my_list = ['hi', 'hey', 'yo']
	c = Context(d)
	return httpResponse
	
def index(request):
	t = loader.get_template('hello/index.html')
	d = {'greeting': 'hello'}
	c = Context(d)
	return httpResponse
