# Text-Book-Recommendor
Expert System that Prints the Text Book name for a given topic
This one of my academic projects.The main aim is to print the name of textbook given a Topic.

I have thought of different approaches:-

i)Using the basic if else conditions or switch case to identify the topic and print its correspinding answer.This method is not dynamic and hard to write all the conditions.

ii)storing in files- this stores in csv files and prints the output.The problem i have faced is it must be updated manually.

iii)storing in databases- I'm new to this although they are fatser but have the same problem like storing in files

iv)WebScraping- This technique is possible only when there is internet.I have used this because I felt internet is not an issue

Packages-

Selenium-Selenium is a portable framework for testing web applications. I have used Selenuim Webdriver to invoke the web browser and search over the internet dynamically and to required page that contains the answer

Beautifulsoup- Beautiful Soup is a Python package for parsing HTML and XML documents.This is used to get information from static web page.

Tkinter-Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface. I have used this to build interface

Working-

Initially when you run the program you will get an interface stating "Enter Topic" and a text input bar as soon as you enter the topic and hit enter selenuim webdriver is automatically invoked(I have kept it visible so you counld clearly see what is exactly going on and modify it when deploying your model).I have chosen librarygenisis since it is the largest repository of books know to me(any new sources let me know and I will update them).The webdriver automatically searches the topic and results page is captured by using url package.The driver quits automatically.

Now,Beautifulsoup takes the static webpage and extracts the required information returns then to the user interface and the UI diaplays the output.
