**Customers APP API**

**Development Journey**

```
(a)Authenctication

After creating the registration  model i will
implement authentucation and have all routes after
logging in protected.

(b)Create a provision for a user to update their profile
   first before making any order.

   In this route i will make sure that a user provides details
   such as telephone used by Africas Talking API.

   These details will be stored in a Customers Table
   which has a relationship with the Users Table

   (user_id) --->Foreign Key.


(c)Making Orders

The customer_id will be a foreign key in the orders table.
This will help me have an endpoint where i can be able to get all
the orders made by a user.

I will implement a utility class to call the AfricasTalking API.
and Send SMS to a user when they make an order.


DB Fields

{customer_id}
{order->Text field}
{created_at}
{updated_at}


```

**Database Used**

```
PostgresSQL

```

**Super User Credetaials**

```
Username  ecommerceadmin
password  admin

```
