from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


# Create your views here.
# def books(request):
#     form = BookForm()
#     return render(request, 'app/bookform.html', context={"form": form})


def addbook(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(book_name=request.POST["bookname"], author=request.POST["author"],
                                page=request.POST["page"], price=request.POST["price"])
            #print(form.cleaned_data['bookname'])
            return redirect("/showbook/")


    return render(request, "app/bookform.html", context={"form": form})


def showbook(request):
    data = Book.objects.all()
    return render(request, 'app/book.html', context={"data": data})


def update(request, id):
    data = Book.objects.get(id=id)
    initial = {'bookname': data.book_name, 'author': data.author, 'page': data.page, 'price': data.price}
    form = BookForm(initial=initial)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            data.book_name = request.POST.get('bookname')
            data.author = request.POST.get('author')
            data.page = request.POST.get('page')
            data.price = request.POST.get('price')
            data.save()
        return redirect('/showbook/')

    return render(request, "app/update.html", context={"form": form, 'data': data})


def delete(request, id):
    del_book = Book.objects.get(id=id)
    del_book.delete()
    return redirect("/showbook/")
