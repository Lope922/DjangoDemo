from django.shortcuts import render
# to include models we need to import it 
from .models import Post
from django.utils import timezone 

# returns the blog/post_list webpage upon request
def post_list(request):
	# defines a post , which is sorted by publish date
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

	