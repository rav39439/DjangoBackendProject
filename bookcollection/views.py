from django.shortcuts import render,HttpResponse,get_object_or_404
from bookcollection.models import Book, Review
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):

    return render(request,'index.html')

def contact(request):

    return HttpResponse ('This is contact page')

def test(request):

    return HttpResponse ('This is test page')

@csrf_exempt
def addBook(request):
   if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            genre = data.get('genre')
            description = data.get('description')
            year = data.get('year')

            # Create and save the book
            Book.objects.create(
                title=title,
                author=author,
                genre=genre,
                published_year=year,
                description=description
            )

            return JsonResponse({'message': 'Book added successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def getBook(request):
    books = Book.objects.all().values('id', 'title', 'author', 'genre', 'published_year')
    return JsonResponse(list(books), safe=False)
    # books = Book.objects.all()

    # # Create a simple string to show book info
    # output = []
    # for book in books:
    #     output.append(book)
    #     # output += f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Year: {book.published_year}<br>"

    # return HttpResponse(output)

@csrf_exempt
def getBookbyId(request, id):
    book = get_object_or_404(Book, id=id)
    data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'published_year': book.published_year,
        'description': book.description,
    }
    return JsonResponse(data, safe=False)

@csrf_exempt
def addReviews(request,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        rating = data.get('rating')
        comment = data.get('comment')
        username = data.get('username')

        book = Book.objects.get(id=id)  # Get the book by ID
        Review.objects.create(
            book=book,
            username=username,
            comment=comment,
            bookid=book.id,
            rating=rating
        )
    return HttpResponse ('This is test page')
@csrf_exempt
def getReviews(request, id):
    if request.method == 'GET':
        reviews = Review.objects.filter(book_id=id)
        reviews_data = [
            {
                'id': review.id,
                'rating': review.rating,
                'username':review.username,
                'comment': review.comment,
                'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S') if review.created_at else '',
                # Add more fields if needed
            }
            for review in reviews
        ]
        return JsonResponse({'reviews': reviews_data})
    return JsonResponse({'error': 'GET method only'}, status=405)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already taken.')

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # hash the password!
        )
    return HttpResponse('User registered successfully!')

    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Log the user in
            return HttpResponse(f"Welcome, {user.username}!")
        else:
            return HttpResponse("Invalid username or password.")

# Create your views here.
