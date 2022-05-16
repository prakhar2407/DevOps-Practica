import email
from django.shortcuts import render
from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)
db = mongo['ncu_db']
collection = db['customers']

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello from Django...</h1>")

# def index(request):
#     name = "Ravi"
#     return render(request, 'index.html', context={'name' : name})

productList = []
# productList.extend([
#         {'id' : 101, 'name' : 'Apple', 'price' : 55000, 'url' : 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
#         {'id' : 102, 'name' : 'Samsung', 'price' : 45000, 'url' : 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
#         {'id' : 103, 'name' : 'Redmi', 'price' : 12000, 'url' : 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
#         {'id' : 104, 'name' : 'Vivo', 'price' : 25000, 'url' : 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
#         {'id': 107, 'name': 'Redmi', 'price': 13000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
#         {'id': 106, 'name': 'Samsung', 'price': 35000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
#         {'id': 105, 'name': 'Apple', 'price': 65000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
#         {'id': 108, 'name': 'Vivo', 'price': 20000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
#         {'id': 109, 'name': 'Apple', 'price': 75000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
#         {'id': 110, 'name': 'Samsung', 'price': 25000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
#         {'id': 111, 'name': 'Redmi', 'price': 10000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
#         {'id': 112, 'name': 'Vivo', 'price': 18000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
#     ])

def login(request):
    return render(request, 'login.html')

def index(request):
    username = request.POST['u_name']
    password = request.POST['u_password']
    cursor = collection.find()
    for item in cursor:
        productList.append(item)
    if username == "ravi" and password == "1234":
        msg = "Login Success..."
    else:
        msg = "Login Failed..."
    return render(request, 'index.html', context={'msg':msg, 'name':username, "data" : productList})

def register(request):
    username = request.POST['u_name']
    usermail = request.POST['u_mail']
    password = request.POST['u_password']
    age = request.POST['u_age']
    collection = db['users']
    collection.insert_one({
        "user_id" : usermail,
        "user_name" : username,
        "user_pwd" : password,
        "age" : age
    })
    msg = "Register Successfull..."
    
    return render(request, 'index.html', context={'msg':msg, 'name':username, "data" : productList})