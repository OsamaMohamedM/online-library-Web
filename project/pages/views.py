from django.shortcuts import render# type: ignore
from django.core.serializers import serialize# type: ignore
from django.http import JsonResponse# type: ignore
from .models import books 
from .models import user 
from django.db.models import Q# type: ignore
from django.shortcuts import get_object_or_404# type: ignore

def library(request):
    return render(request,'library.html')
def signup(request):
    users = user.objects.all()
    users_json=serialize('json',users)
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('pass')
        c = request.POST.get('age')
        e = request.POST.get('tel')
        f = request.POST.get('email')
        x = request.POST.get('type')
        
        existing_user = user.objects.filter(email=f).exists()
        print(x)
        if not existing_user:
            data = user(name=a, age=c, phone=e, email=f, password=b, type=x)
            data.save()
            users = user.objects.all()
            users_json=serialize('json',users)
            return render(request,'sign.html',{'users':users_json})    
 
    return render(request,'signup.html',{'users':users_json})

def sign(request):

    users = user.objects.all()
    users_json=serialize('json',users)
    return render(request,"sign.html",{'users': users_json})




def main_user(request):
   
    y =user.objects.all() 
    x =books.objects.all() 
    a = serialize('json', x)
    b =serialize('json', y)
    if request.method == 'POST':
         user_id = request.POST.get('user_id')
         book_id = request.POST.get('book_id')
         c =x.get(pk=book_id) 
         d =y.get(pk=user_id) 
         if not d.borrowedBooks.filter(pk=c.pk).exists():
           d.borrowedBooks.add(c)
           d.save() 
           
    Y =user.objects.all() 
    X =books.objects.all() 
    A = serialize('json', X)
    B =serialize('json', Y)      
    return render(request,'main_user.html',{'books':A ,'users':B})
def main_admin(request):
    x =books.objects.all()
    a=serialize('json',x)
    return render(request,'main_admin.html',{ 'books':a})

def search_books(request):
    query = request.GET.get('query', '')
    if query!='':
       x = list(books.objects.filter(
         Q(tittle__icontains=query) | 
        Q(author__icontains=query) | 
        Q(category__icontains=query)
        ).values())  
    else:
        x = list(books.objects.all().values())
    return JsonResponse(x, safe=False)
def search_book(request):
    query = request.GET.get('query', '')
    if query!='':
       x = list(books.objects.filter(pk=query))  
    else:
        x =[]
    return JsonResponse(x, safe=False)
 


def AddBook(request):
     if request.method == 'POST':
        a = request.POST.get('tittle')
        b = request.POST.get('author')
        c = request.POST.get('des')
        e = request.POST.get('lang')
        f = request.POST.get('book')
        g = request.FILES.get('poster')
        h = request.POST.get('price') 
        i = request.POST.get('number')
        j = request.POST.get('year')
        k = request.POST.get('category')
        l = request.POST.get('id')
        print(g)
        existing_book = books.objects.filter(tittle=f ).exists()

        if not existing_book:
            data = books(id=l,tittle=a, description=c, author=b, language=e, book_link=f, image=g,price=h,num_of_pages=i,year=j,category=k)
            data.save()
     return render(request,'Add-book.htm')


def delete(request):
    if request.method == 'POST':
       l = request.POST.get('id')
       x =books.objects.get(pk=l)
       print(l)
       x.delete()
    return render(request,'delete-book.htm')
def edit(request):
     x =books.objects.all()
     a=serialize('json',x)
     return render(request,'Edit-book.htm',{ 'books':a})



def Edit(request):
    x =books.objects.all()
    y =serialize('json',x)
    if request.method == 'POST':
        title = request.POST.get('tittle')
        author = request.POST.get('author')
        description = request.POST.get('des')
        language = request.POST.get('lang')
        book_type = request.POST.get('book')
        poster = request.POST.get('poster')
        price = request.POST.get('price')
        number = request.POST.get('number')
        year = request.POST.get('year')
        category = request.POST.get('category')
        book_id = request.POST.get('id')
        if(book_id!=None):
          book_instance = get_object_or_404(books, id=book_id)
          book_instance.tittle = title
          book_instance.author = author
          book_instance.description = description
          book_instance.language = language
          book_instance.book_link = book_type
          book_instance.poster = poster
          book_instance.price = price
          book_instance.number = number
          book_instance.year = year
          book_instance.category = category
          book_instance.save()
          print(book_id)
          x =books.objects.all()
          y =serialize('json',x)
        return render(request, 'Edit-book.htm',{'book':y})
    
    return render(request, 'Edit.html',{'books':y})
def borrow(request):
    x =books.objects.all()
    a = serialize('json', x)
    return render(request,'BorrowBook.html',{'books':a})
def borrowed(request):
    x =books.objects.all()
    y =user.objects.all() 
    a = serialize('json', x)
    b =serialize('json', y)
    return render(request,'borrowed_books.html',{'users':b,'books':a})
def bookDetails(request):
        x =books.objects.all()
        y =user.objects.all() 
        if request.method == 'POST':
         user_id = request.POST.get('user_id')
         book_id = request.POST.get('book_id')
         c =x.get(pk=book_id) 
         d =y.get(pk=user_id) 
         if not d.borrowedBooks.filter(pk=c.pk).exists():
           d.borrowedBooks.add(c)
         d.save()
         
        a = serialize('json', x)
        b =serialize('json', y)   
        return render(request,'bookdetails.html',{'books':a,'users':b})
      

def borrowUser(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')

        User = user.objects.get(pk=user_id)
        book = books.objects.get(pk=book_id)

        if not User.borrowedBooks.filter(pk=book.pk).exists():
            user.borrowedBooks.add(book)
            user.save()
            return JsonResponse({'success': True, 'message': 'Book borrowed successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})