from django.shortcuts import redirect, render
from .models import register_info, product, category, order
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def base(request):
    return render(request,'base.html')

def signup(request):
    return render(request, 'signup.html')

def home(request):
    if request.method=='POST':
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id = request.session.get('cart')

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity -1
                else:
                    cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1

        else:
            cart_id = {}
            cart_id[product_id] = 1

        request.session['cart'] = cart_id
        print(request.session['cart'])

        

    

    cat = category.objects.all()    

    cat_id = request.GET.get('id')

    if cat_id:
        path = product.objects.filter(category_id = cat_id)

    else:
        path = product.objects.all()

    
    
    return render(request, 'home.html',{'path':path, 'cat':cat})

def save(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        save_info = register_info(fname = fname,
        lname = lname,
        gender = gender,
        email=email,
        password = make_password(password))

        save_info.save()

        return redirect('home')


    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        password = request.POST.get('password')

        try:
            fetch_info = register_info.objects.get(fname = fname)

            if fetch_info.fname == fname:
                flag = check_password(password, fetch_info.password)
                print(flag)
                errormsg = None
                if flag:
                    errormsg = "congrats successful login..."
                    param = {'errormsg' : errormsg}
                    request.session['fname_global'] = fetch_info.fname
                    # add this line
                    request.session['customer_id'] = fetch_info.id
                    print(request.session['fname_global'])
                    return redirect('home')
                
                else:
                    errormsg = "Please enter valid password."
                    param = {'errormsg' : errormsg}
                    return render(request,'home.html', param)


        except:
            errormsg = "please enter valid UserName"
            param = {'errormsg' : errormsg}
            return render(request, 'home.html', param)

def logout(request):
    print()
    request.session.clear()
    return redirect('home')

def cart(request):
    cart_has_value = request.session.get('cart')

    if cart_has_value:
        print("cart has value\n")
        if request.session.get('cart').keys():

            print(list(request.session.get('cart').keys()))
            ids = list(request.session.get('cart').keys())

            cart_pro=product.objects.filter(id__in=ids)   
            print(cart_pro)
            # if id in x = (id__in = ids)

            return render(request, 'cart.html', {'cart_pro':cart_pro})

    print("cart has value 2 \n")
    return render(request, 'cart.html')

def checkout(request):
    if request.method=='POST':
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        customer_id = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = product.objects.filter(id__in = list(cart.keys()))

        for pro in products:
            save_order_dtls = order(customer = register_info(id=customer_id),
            product = pro,
            price = pro.price,
            quantity = cart.get(str(pro.id)),
            address = address,
            phone = mobile
            )
            print(f"{register_info(id=customer_id)}\n {pro} \n {pro.price} \n {cart.get(str(pro.id))} \n {address} \n {mobile}\n\n\n")
            save_order_dtls.save()

        request.session['cart'] = {}
    
    return render(request,'checkout.html')


def order_dtl(request):
    customer = request.session.get('customer_id')
    if customer:
        order_dtls = order.objects.filter(customer=customer).order_by('-date')

    tp = 0
    for i in order_dtls:
        tp = tp + (i.price * i.quantity)

    return render(request, 'order.html',{'order_dtls':order_dtls, 'tp':tp})

def js(request):
    return render(request, 'js.html')
    


