from djpanel.models import *
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse

def list(request):
	r = Panel.objects.all()
	urls = [a.url() for a in r if a.owner == request.user or a.public]
	return HttpResponse(simplejson.dumps(urls))

def panel(request, panel):
	from django.template import Context, Template
	p = Panel.objects.get(name = panel)
	t = Template(p.template.content)
	c = Context(simplejson.loads(p.template_configuration))
	t = t.render(c)
	print t
	for element in p.template_elements.all():
		b = Template(element.block.markup)
		j = Template(element.block.javascript)
		c = Context(simplejson.loads(element.block_configuration))
		b = b.render(c)
		print b
		j = j.render(c)
		print j
		t = t.replace('@markup@@'+element.template_key+'@@@', b)
		t = t.replace('@script@@'+element.template_key+'@@@', j)
	
	return HttpResponse(t)
	
	