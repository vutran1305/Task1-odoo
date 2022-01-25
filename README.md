# Task1-odoo
Sale Order Force Code (2h)
 
We wanna have a special group (1. Advanced Sale) which can modify customer discount code.
The customer has this code will have discount on any products of store
The valid code is VIP_10, VIP_20
(Valid code format VIP + ‘_’ + integer)


When we create a sale order, depend on customer all sale order lines (products) will have discounts

E.g all customer has code VIP_10 will have discount 10% on any products
All customers has code VIP_20 will have discount 20% on any products
 
Requirements:
1. Create custom field to store the customer discount code
	customer_discount_code
	Field text

2. Create a group
Name “1. Advanced Sale”
Only users in this group can see and edit customer discount code in customer form


3. Create custom field to display estimated discount total
	Sale_order_discount_estimated
	Calculated discount total

4.Show up customer code on customer form, customer tree view
	Put this field anywhere (convenient position in form view and tree view)

5.Create a filter to filter all order/quotation has special customer
The orders has customer (partner) with discount code

6.Create a menu to display all customers which has valid code
	VIP_8 is valid code
	VIPP_10, vip_1 is invalid

7.Create a action to mass update all selected customer discount code

8. If order contain valid customer code show up on my cart (frontend), any where
	Applied Customer Code: VIP_10
