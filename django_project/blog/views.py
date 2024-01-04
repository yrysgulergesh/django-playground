from django.shortcuts import render

posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'Yrysgul Ergesh',
        'content': 'Beautiful is better than ugly',
        'published_at': 'January 4, 2024.'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Yrysgul Ergesh',
        'content': 'Explicit is better than implicit',
        'published_at': 'January 4, 2024.'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Zen of Python'
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html')
