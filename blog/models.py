from django.db import models
from django.utils import timezone 

# defines a Post 
class Post(models.Model):
	# attributes for each post , along with the input field that will be used. 
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	#method that publishes the post along with the date time property of that current instance
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
		# returns a string value 
	def __str__(self):
		return self.title