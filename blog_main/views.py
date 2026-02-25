
# from django.http import HttpResponse- 01
from django.shortcuts import render
from blogs.models import Blog, Category



def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status ='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status ='Published')
    
    

    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        }
    # return HttpResponse('<h2>Homepage</h2>')- 01
    return render(request,'home.html', context)