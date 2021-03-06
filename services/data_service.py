from typing import List, Optional
import datetime
import bson
from Data.customer import Customer
from Data.phone import Phone
from Data.attribute import *
from mongoengine.queryset.visitor import Q
from connect_mongo import *

#0 find phone in database
# take attribute as input and look for the device, if not exist use 
# #2 add phone to database df
def add_phone(imei, model, storage, color, grade, product_id):
	phone = Phone()
	phone.imei = imei
	phone.model = model
	phone.storage = storage
	phone.color = color
	phone.grade = grade
	phone.product_id = product_id
	generate_full_name(phone)
	phone.save()
	return phone

def generate_full_name(phone : Phone) -> str:
	phone.full_name = phone.model + " " + phone.storage + "GB [" + phone.grade + " Grade] [" + phone.color +"]"
	return phone.full_name

def display_phone_new_qty():
	update_list = Phone.objects.filter(change_checked=False).distinct(field="full_name")
	for full_name in update_list:
		qty = Phone.objects(full_name=full_name).count()
		print ("{}: {}".format(full_name,qty))

def mark_phone_updated(full_name):
	Phone.objects(full_name=full_name,change_checked=False).update(change_checked=True,date_modified=datetime.datetime.now)

def search_by_imei(imei):
	phone = Phone.objects.filter(imei__iendswith=imei)
	return phone

def add_customer(name="",company="",mobile="",email="") -> Customer:
	if company != "":
		customer = Customer(name=name,company=company,mobile=mobile,email=email)
		customer.save()
		return customer
	else:
		print("company required")
		

def search_for_customer(keywords):
	customer_list = Customer.objects(Q(name__icontains=keywords) | Q(company__icontains=keywords) | Q(mobile__icontains=keywords) | Q(email__icontains=keywords))
	return customer_list

def search_for_phone(keywords):
	phone_list = Phone.objects(full_name__icontains=keywords)
	return phone_list

def mark_phone_sold(phone:Phone,customer:Customer):
	phone.customer_id = customer.id
	phone.date_out = datetime.datetime.now()
	phone.date_modified = datetime.datetime.now()
	return phone.save()

def customer_summary_report(customer:Customer):
	phone_list = Phone.objects(customer_id=customer.id)
	return phone_list

def print_phone_list(phone_list):
	for phone in phone_list:
		print("{}, imei {}".format(phone.full_name,phone.imei))

def display_inventory_summary():
	invenotry_list = Phone.objects(customer_id__exists=False).distinct(field="full_name")
	for phone in invenotry_list:
		qty = Phone.objects(full_name=phone).count()
		print ("{}: {}".format(phone,qty))

def add_attribute(name="",value=""):
	#name = attribute_name: model, storage, grade, color
	#value is the attribute value
	#add attribute_value to value list if value not already exists.
	#case insensitive
	if name != "":
		attribute=Attributes.objects.get(name = name)
		if value.lower() not in [x.lower() for x in attribute.value]:
			attribute.value.append(value)
			attribute.save()
			print ("{}={}".format(attribute.name,attribute.value))
		else:
			print("{} \"{}\" already exists".format(name,value))
					  
def get_attribute_list(name):
	try:
		return Attributes.objects.get(name=name).value
	except:
		pass
	