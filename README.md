# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/dynamic.css' %}">
              
</head>

<body>
    <div class="container">
    <div class="banner">
        Silicon Private Limited.
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/products">Products</a></div> 
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contactus">Contact Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2020 Silicon Private Limited, Developed by Y Chethan.
    </div>
    </div>
</body>

</html>
```

### home.html
```
{% extends "spl/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/building.jpg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}
```

### products.html
```
{% extends "spl/base.html" %}

{% block content %}
<div class="productcontent">
    <h1>Our Premium Products</h1>
    {% for product in products %}
    <div class="productitem">
        <div class="itemimage">
            <img src="/photos/{{product.image}}" alt="product image">
        </div>
        <div class="itemname">{{ product.name }}</div>
        <div class="itemprice">Price: Rs.{{ product.price }} </div>
    </div>
    {% endfor %}
</div>
{% endblock  %}
```

### people.html
```
{% extends "spl/base.html" %}

{% block content %}
{% for people in people %}
    <div class="peopleitem">
        <div class="peopleimage" style="margin-top: 20px;">
            <img src="/photos/{{ people.image }}" alt="people">
        </div>
        <h2 class="peoplename">{{ people.name }}</h2>
        <h3 class="peopledesignation">{{ people.designation }}</h3>
    </div>
    {% endfor %}
{% endblock %}
```

### contactus.html
```
{% extends "spl/base.html" %}

{% block content %}
<img src="/static/img/contactus.png" style="background-repeat: no-repeat;margin-left:25%;margin-top:2%;width: 50%;" alt="contact">
<div class="contact">
    <br>Silicon Private Limited.,<br>
    1/223, Silicon Valley,<br>
    <a href="mailto:someone@example.com" style="text-decoration: none;color: black;">E-mail: someone@example.com</a><br>
    <a href="tel:+4733378901" style="text-decoration: none;color: black;">Phone: +47 333 78 901</a>
</div>
{% endblock %}
```

## OUTPUT:

![output](./static/img/output1.jpg)

![output](./static/img/output2.jpg)

![output](./static/img/output3.jpg)

![output](./static/img/output4.jpg)

## CODE VALIDATION REPORT:

![output](./static/img/html1.jpg)

![output](./static/img/html2.jpg)

![output](./static/img/html3.jpg)

![output](./static/img/html4.jpg)

## ADMIN PAGE:

![output](./static/img/admin1.jpg)

![output](./static/img/admin2.jpg)

## TEMPLATE FOR PRODUCTS AND PEOPLE PAGE:

![output](./static/img/template.jpg)

##  GitHub Repo URL:
https://github.com/Y-CHETHAN/companywebsitedynamic.git

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://chethan.student.saveetha.in:8000/. HTML code is validated.