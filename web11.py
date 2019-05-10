#inporting packages
from bs4 import BeautifulSoup
import urllib.request
import requests
from selenium import webdriver
from tkinter import *
#declaring gui window
root=Tk()
#label is text visible on screen
l1=Label(root,text='Enter Topic:{min 4 chars}:')
#placing above label in root grid will help us place in particular position
l1.grid(row=0,column=0)
#find function receives data from gui and prints it in gui
def find():
    #receiving data from gui
    data=e.get()
    #calling function of selenium and webscrapping
    s=enter(data)
    #printing answer
    ans.configure(text=data)
    l2.configure(text=s[0])
    l3.configure(text=s[1])
    l4.configure(text=s[2])
    l5.configure(text=s[3])
    l6.configure(text=s[4])
    l7.configure(text=s[5])
    l8.configure(text=s[6])
    l9.configure(text=s[7])
    l10.configure(text='Topic')
#input in gui
e=Entry(root)
#button in gui
button=Button(None,text="Search!",command=find)
e.grid(row=0,column=1,sticky=W)
button.grid(row=1,columnspan=1,sticky=N)
#predefining answer labels
ans=Label(root)
l2=Label(root)
l3=Label(root)
l4=Label(root)
l5=Label(root)
l6=Label(root)
l7=Label(root)
l8=Label(root)
l9=Label(root)
l10=Label(root)
#position of answer labels
l10.grid(row=2,column=0,sticky=W)
ans.grid(row=2,column=1,sticky=W)
l2.grid(row=3,column=0,sticky=W)
l3.grid(row=3,column=1,sticky=W)
l4.grid(row=4,column=0,sticky=W)
l5.grid(row=4,column=1,sticky=W)
l6.grid(row=5,column=0,sticky=W)
l7.grid(row=5,column=1,sticky=W)
l8.grid(row=6,column=0,sticky=W)
l9.grid(row=6,column=1,sticky=W)
#gui dimensions
root.geometry('600x400')
#returns book name after searching
def enter(data):
    key=data
    #invoking browser through webdriver
    driver=webdriver.Chrome()
    #searching the required
    driver.get('http://libgen.io/')
    #filling the search bar
    s=driver.find_element_by_id('searchform')
    s.send_keys(key)
    #clicking on search
    driver.find_elements_by_xpath("//input[@value='Search!']")[0].click()
    #retrieving url
    my_url=driver.current_url
    #closing driver
    driver.quit()

    #opening static url
    r=requests.get(my_url)
    #scrapping web page
    html_content=r.text
    soup=BeautifulSoup(html_content,'html.parser')
    #getting table values
    table=soup.find('table',{'class':'c'})
    for row in table.find_all('tr')[1:2]:
        cells=row.find_all('td')
        #printing only first row
        s='id:',cells[0].text,'Authors:',cells[1].text,'Title:',cells[2].text,'Publisher:',cells[3].text
    return s
