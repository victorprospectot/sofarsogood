def zip_equal(it1, it2):
    if len(it1) != len(it2):
        raise ValueError("Lengths of iterables are different")
    return zip(it1, it2)

def create_paypal_shopping_order(order_description, currency, custom, list_of_products):
	"""Returns a list of parameters about products
	   in order to be used at the SetExpressCheckout
	   operation (based on API version 124).
	   
	   Parameters
	   ----------

	   order_description:
	   		   type: string
	   		   description: Description of the order to be paid

	    currency:
	           type: string
	           description: The currency to paid
	           example: USD, MXN, EUR

	   list_of_products: 
	           type: list of lists
	           description: List of lists(up to 10) of products to be sent to PayPal in order to be paid
	           syntax: [[AMOUNT, NAME, DESCRIPTION, QUANTITY] .... up to 10 lists]
	           example: [[100, 'Coffee', 'Coffee ultra mega expensive for rich people', 1]]

	"""
	default_parameters = ["PAYMENTREQUEST_0_AMT", "PAYMENTREQUEST_0_CURRENCYCODE", "PAYMENTREQUEST_0_DESC", "PAYMENTREQUEST_0_CUSTOM"]
	product_parameters = ["L_PAYMENTREQUEST_0_AMTn", "L_PAYMENTREQUEST_0_NAMEn", "L_PAYMENTREQUEST_0_DESCn", "L_PAYMENTREQUEST_0_QTYn"]
	total_order = sum(map(lambda x: x[0], list_of_products))
	values = [total_order, currency, order_description, custom]
	zipped = zip_equal(default_parameters, values)
	zipped_product = [zip_equal(product_parameters, x) for x in list_of_products]
	total_zipped = zipped + zipped_product
	print total_zipped
# &METHOD=SetExpressCheckout
# &RETURNURL=http://...
# &CANCELURL=http://...
# &PAYMENTREQUEST_0_CURRENCYCODE=USD
# &PAYMENTREQUEST_0_AMT=300
# &PAYMENTREQUEST_0_ITEMAMT=200
# &PAYMENTREQUEST_0_TAXAMT=100
# &PAYMENTREQUEST_0_DESC=Summer Vacation trip
# &PAYMENTREQUEST_0_INSURANCEAMT=0
# &PAYMENTREQUEST_0_SHIPDISCAMT=0
# &PAYMENTREQUEST_0_SELLERPAYPALACCOUNTID=seller-139@paypal.com
# &PAYMENTREQUEST_0_INSURANCEOPTIONOFFERED=false
# &PAYMENTREQUEST_0_PAYMENTACTION=Order
# &PAYMENTREQUEST_0_PAYMENTREQUESTID=CART26488-PAYMENT0
# &PAYMENTREQUEST_1_CURRENCYCODE=USD
# &PAYMENTREQUEST_1_AMT=200
# &PAYMENTREQUEST_1_ITEMAMT=180
# &PAYMENTREQUEST_1_SHIPPINGAMT=0
# &PAYMENTREQUEST_1_HANDLINGAMT=0
# &PAYMENTREQUEST_1_TAXAMT=20
# &PAYMENTREQUEST_1_DESC=Summer Vacation trip
# &PAYMENTREQUEST_1_INSURANCEAMT=0
# &PAYMENTREQUEST_1_SHIPDISCAMT=0
# &PAYMENTREQUEST_1_SELLERPAYPALACCOUNTID=seller-140@paypal.com
# &PAYMENTREQUEST_1_INSURANCEOPTIONOFFERED=false
# &PAYMENTREQUEST_1_PAYMENTACTION=Order
# &PAYMENTREQUEST_1_PAYMENTREQUESTID=CART26488-PAYMENT1
# &L_PAYMENTREQUEST_0_NAME0=Depart San Jose Feb 12 at 12:10PM Arrive in Baltimore at 10:22PM
# &L_PAYMENTREQUEST_0_NAME1=Depart Baltimore Feb 15 at 6:13 PM Arrive in San Jose at 10:51 PM
# &L_PAYMENTREQUEST_0_NUMBER0=Flight 522
# &L_PAYMENTREQUEST_0_NUMBER1=Flight 961
# &L_PAYMENTREQUEST_0_QTY0=1
# &L_PAYMENTREQUEST_0_QTY1=1
# &L_PAYMENTREQUEST_0_TAXAMT0=50
# &L_PAYMENTREQUEST_0_TAXAMT1=50
# &L_PAYMENTREQUEST_0_AMT0=50
# &L_PAYMENTREQUEST_0_AMT1=150
# &L_PAYMENTREQUEST_0_DESC0=SJC Terminal 1. Flight time: 7 hours 12 minutes
# &L_PAYMENTREQUEST_0_DESC1=BWI Terminal 1. Flight time: 7 hours 38 minutes
# &L_PAYMENTREQUEST_1_NAME0=Night(s) stay at 9990 Deereco Road,Timonium, MD 21093
# &L_PAYMENTREQUEST_1_NUMBER0=300
# &L_PAYMENTREQUEST_1_QTY0=1
# &L_PAYMENTREQUEST_1_TAXAMT0=20
# &L_PAYMENTREQUEST_1_AMT0=180
# &L_PAYMENTREQUEST_1_DESC0=King No-Smoking; Check in after 4:00 PM; Check out by 1:00 PM
