from django.shortcuts import render, redirect, HttpResponse
from learningApp import models
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth  import authenticate ,  login, logout



import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# Create your views here.


def index(request):
	data = {
		"courses": models.AddCourse.objects.all,
		"username" : request.user.username,
	}
	return render(request, 'index.html', data)
	

	
    


def about(request):
    return render(request, 'about.html')



def addCourse(request):
	if request.method=='POST':
		print("\naddCourse is Post method \n")


		courseid = request.POST['id']
		coursename = request.POST['coursename']
		price = request.POST['price']
		trainer = request.POST['trainer']
		sortdesc = request.POST['detail']
		image = request.POST['image']
		video  = request.POST['video']
		button  = request.POST['button']
		fulldesc = request.POST['desc']
		print(courseid, coursename, price, trainer, sortdesc, image, video, button, fulldesc)

		addcourse_instance = models.AddCourse(courseid=courseid,
		coursename=coursename,
		price=price,
		trainer=trainer,
		sortdesc=sortdesc,
		image=image,
		video=video,
		button=button,
		fulldesc=fulldesc)

		addcourse_instance.save()
		print("Save data to database")
	

	return render(request, 'addCourse.html')


def courses(request):

	data = {
		"courses": models.AddCourse.objects.all
	}

	return render(request, 'courses.html', data)





def trainers(request):
    return render(request, 'trainers.html')



def events(request):
    return render(request, 'events.html')


# def pricing(request):
#     return render(request, 'pricing.html')



def course_details(request):
	data = {
		"courses": models.AddCourse.objects.all()
	}
	req_id = request.GET.get('id')

	for course in data['courses']:
		if str(course.courseid) == req_id:
			course_data = {
				"courseid" : course.courseid,
				"coursename" : course.coursename,
				"price" : course.price,
				"trainer" : course.trainer,
				"sortdesc" : course.sortdesc,
				"image" : course.image,
				"video"  : course.video,
				"button"  : course.button,
				"fulldesc" : course.fulldesc,
			}
	user = {
		"username" : request.user.username,

	}
	return render(request, 'course_details.html', course_data)

def edit(request):
	return render(request, 'edit.html')



def handelSignup(request):
	if request.method=="POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			myuser = User.objects.create_user(email, email, password1)
			myuser.first_name = firstname
			myuser.last_name = lastname
			myuser.save()
		else:
			messages.error(request, "Both Password are not Match")
			return render(request, 'signup.html')		

		return redirect('login')
	else:
		return render(request, 'signup.html')


def handelLogin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		# fetch data from User Database
		

		
		user = authenticate(username=username, password=password)
		if user is not None:
			 login(request, user)
			 print("\n\nUser Name in login handle  ", user.username)
			#  messages.success(request, "Successfully Logged In")
			 return redirect("index")

		else:
			messages.error(request, "Invalid credentials! Please try again")
			return redirect("login")


	return render(request, 'login.html')

def my_enrolled_courses(request):
	if request.user.is_authenticated:
		print("login")
		user = {
		"username" : request.user.username,

		}
	else:
		print("not logged in")
		user = {
		"username" : "First Login please",

		}

	print("\n\nUser Name in my enrolled courses  ", request.user.username)
	buydata = models.BuyCourse.objects.all()
	# i = 1
	enrolled_main = []
	
	for x in buydata:
		if x.username == request.user.username:
			list_of_course = x.courseids.split(',')			
			# print(list_of_course)
			addCourseData = models.AddCourse.objects.all()
			for course in addCourseData:
				enrolled_row = {}
				if str(course.courseid) in list_of_course:
					print("avaible " , course.courseid)
					enrolled_row.update({'courseid': course.courseid})
					enrolled_row.update({'coursename': course.coursename})
					enrolled_row.update({'price' : course.price})
					enrolled_row.update({'trainer' : course.trainer})
					enrolled_row.update({'sortdesc' : course.sortdesc})
					enrolled_row.update({'image' : course.image})
					enrolled_row.update({'video' :	course.video})
					enrolled_row.update({'button' : course.button})
					enrolled_row.update({'fulldesc' :course.fulldesc})
					enrolled_main.append(enrolled_row)
					
			# print(enrolled_main)
	enrolled_main_main = {"enrolled": enrolled_main}
	
	return render(request, 'my_enrolled_courses.html', enrolled_main_main)



def handelLogout(request):
    logout(request)
    return redirect('index')







# Payment Start here __________________________



# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def homepage_2(request):
	currency = 'INR'
	amount = 20000 # Rs. 200

	# Create a Razorpay Order
	razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
	razorpay_order_id = razorpay_order['id']
	callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['callback_url'] = callback_url

	return JsonResponse(context)

	# return render(request, 'payment.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()

	