from django.shortcuts import render


# returns the blog/post_list webpage upon request
def post_list(request):
	return render(request, 'blog/post_list.html', {})
	