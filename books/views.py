from django.shortcuts import render, redirect
from login.models import User, Book


def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "all_books" : Book.objects.all(),
    }
    return render(request, "books.html", context)


def add_book(request):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        Book.objects.create(title = request.POST['title'], desc = request.POST['description'],
            uploaded_by_id = user,
        )
        book = Book.objects.get(title=request.POST['title'])
        user.liked_books.add(book)      
        # Many-to-Many requires you to instantiate both
        # class with # of related name gets assigned the instantiated other class
    return redirect('/books')

def add_favorite(request):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    user.liked_books.add(book)
    return redirect('/books')

def delete_favorite(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    book.users_who_like.remove(user)
    return redirect('/books')



def book_detail(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "book" : book,
        "this_user" : user,
    }
    return render(request, "book_detail.html", context)

def book_update(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        book = Book.objects.get(id=request.POST['book_id'])
        book.title=request.POST['title']
        book.desc=request.POST['desc']
        book.save()
    return redirect('/books')
    
def book_delete(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books')

def my_view(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "user" : user,
    }
    return render(request, "my_view.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
