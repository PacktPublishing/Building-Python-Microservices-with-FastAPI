


# Building Python Microservices with FastAPI

<a href="https://www.packtpub.com/product/building-python-microservices-with-fastapi/9781803245966?utm_source=github&utm_medium=repository&utm_campaign=9781803245966"><img src="https://static.packt-cdn.com/products/9781803245966/cover/smaller" alt="Building Python Microservices with FastAPI" height="256px" align="right"></a>

This is the code repository for [Building Python Microservices with FastAPI](https://www.packtpub.com/product/building-python-microservices-with-fastapi/9781803245966?utm_source=github&utm_medium=repository&utm_campaign=9781803245966), published by Packt.

**Build secure, scalable, and structured Python microservices from design concepts to infrastructure**

## What is this book about?
FastAPI is an Asynchronous Server Gateway Interface (ASGI)-based framework that can help build modern, manageable, and fast microservices. Because of its asynchronous core platform, this ASGI-based framework provides the best option when it comes to performance, reliability, and scalability over the WSGI-based Django and Flask. When working with Python, Flask, and Django microservices, you’ll be able to put your knowledge to work with this practical guide to building seamlessly manageable and fast microservices.

This book covers the following exciting features: 
* Understand, orient, and implement REST APIs using the basic components of the FastAPI framework
* Build asynchronous as well as synchronous REST services using the built-in pydantic module and asyncio support
* Create small-scale and large-scale microservices applications using features supported by FastAPI
* Build event-driven and message-driven applications using the framework
* Create an asynchronous and synchronous data layer with both relational and NoSQL databases

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1803245964) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter01.

The code will look like the following:
```
@app.get("/ch01/login/")
def login(username: str, password: str):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
```

**Following is what you need for this book:**

This book is for Python web developers, advanced Python users, and backend developers using Flask or Django who want to learn how to use the FastAPI framework to implement microservices. Readers familiar with the REST API and microservices will also benefit from this book. Some parts of the book contain general concepts, processes, and instructions that intermediate-level developers and Python enthusiasts can relate to as well.

With the following software and hardware list you can run all code files present in the book (Chapter 1-11).

### Software and Hardware List

| Chapter  | Software required                   | OS required                                      |
| -------- | ------------------------------------| -------------------------------------------------|
| 1-11     | Python 3.8 or 3.9                   | Windows, macOS, or Linux                         |
| 1-11     | PostgreSQL 13.x                     | 64-bit version of any OS                         |
| 1-11     | VS Code editor                      | Latest version of any OS                         |
| 1-11     | MongoDB 5.x                         | 64-bit version of any OS                         |
| 1-11     | Mongo Database Tools                | 64-bit version of any OS                         |
| 1-11     | Mongo Compass                       | 64-bit version of any OS                         |
| 1-11     | RabbitMQ                            | Latest version of any OS                         |
| 1-11     | Apache Kafka                        | Latest version of any OS                         |
| 1-11     | Spring STS                          | Latest version and configured to use Java 12 JDK |
| 1-11     | Docker Engine                       | Latest version of any OS                         |
| 1-11     | Jaeger                              | Latest version of any OS                         |
| 1-11     | Keycloak                            | Version that works with Java 12                  |
| 1-11     | OpenSSL                             | Latest version of any OS                         |
| 1-11     | Google Chrome                       |                                                  |
| 1-11     | Bootstrap 4.x                       |                                                  |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/ohTNw).


### Related products <Other books you may enjoy>
* Building Python Web APIs with FastAPI [[Packt]](https://www.packtpub.com/product/building-python-web-apis-with-fastapi/9781801076630?_ga=2.180798177.738679754.1661260461-1157268863.1584421665&utm_source=github&utm_medium=repository&utm_campaign=9781801076630) [[Amazon]](https://www.amazon.com/dp/1801076634)

* Python Web Development with Sanic [[Packt]](https://www.packtpub.com/product/python-web-development-with-sanic/9781801814416?_ga=2.188147822.738679754.1661260461-1157268863.1584421665&utm_source=github&utm_medium=repository&utm_campaign=9781801814416) [[Amazon]](https://www.amazon.com/dp/1801814414)

## Get to Know the Author
**Sherwin John Calleja Tragura**
is a subject matter expert on Java, ASP .NET MVC, and Python applications with some background in frontend frameworks. He has managed a team of developers to build various applications related to manufacturing and fixed assets, document management, records management, POS, and inventory systems. He has a background in building laboratory information management systems (LIMS) and hybrid mobile applications as a consultant. He has also provided corporate Bootcamp training services since 2010 for courses on Python, Django, Flask, Jakarta EE, C#, ASP .NET MVC, JSF, Java, and some frontend frameworks. He has authored books such as Spring MVC Blueprints and Spring 5 Cookbook and a Packt video, Modern Java Web Applications with Spring Boot 2.x.


## Other books by the author
* [Spring MVC Blueprints](https://www.packtpub.com/product/spring-mvc-blueprints/9781785888274?utm_source=github&utm_medium=repository&utm_campaign=9781785888274)
* [Spring 5.0 Cookbook](https://www.packtpub.com/product/spring-5-0-cookbook/9781787128316?utm_source=github&utm_medium=repository&utm_campaign=9781787128316)


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781803245966">https://packt.link/free-ebook/9781803245966 </a> </p>