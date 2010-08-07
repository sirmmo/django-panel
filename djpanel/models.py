from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Template(models.Model):
	owner = models.ForeignKey(User)
	public = models.BooleanField(default= True)
	name = models.CharField(max_length = 100, unique = True)
	orientation = models.CharField(max_length = 20, choices = (('Vertical','Vertical'), ('Horizontal', 'Horizontal'),))
	content = models.TextField()
	
	def __unicode__(self):
		return self.name
	
class Block(models.Model):
	owner = models.ForeignKey(User)
	public = models.BooleanField(default= True)
	name = models.CharField(max_length = 100, unique = True)
	javascript = models.TextField(blank=True)
	markup = models.TextField(blank=True)
	parameters = models.TextField(blank=True)
	serverside_code = models.CharField(max_length = 1024)
	def __unicode__(self):
		return self.name
	
class TemplateElement(models.Model):
	template_key = models.CharField(max_length = 250)
	block = models.ForeignKey(Block)
	block_configuration = models.TextField(blank=True, default = "{}")	
	def __unicode__(self):
		return self.block.name + " @ " + self.template_key
	
class Panel (models.Model):
	owner = models.ForeignKey(User)
	public = models.BooleanField(default= False)
	name = models.CharField(max_length = 100, unique = True)
	template = models.ForeignKey(Template)
	template_configuration = models.TextField(default = "{}")
	template_elements = models.ManyToManyField(TemplateElement)
	def __unicode__(self):
		return self.name
		
	@models.permalink
	def url(self):
		return ('djpanel.views.panel', [str(self.name)])
		