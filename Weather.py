from tkinter import*
import requests

root=Tk()
root.title("Wheather Info")
root.geometry("400x400")
root.configure(bg='#17181a')


#78c2cd272dcb82ff19017de3db518bdf
#api.openweathermap.org/data/2.5/weather?q={city name}

def search(city):
    url= 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=78c2cd272dcb82ff19017de3db518bdf'.format(city)
    request=requests.get(url)
    data=request.json()
    name=data['name']
    country=data['sys']['country']
    Des=data['weather'][0]['main']

    temp=data['main']['temp']
    cel=273.15
    tempsR=temp-cel
    temps="{0:.2f}".format(tempsR)

    wind=data['wind']['speed']
    longitude=data['coord']['lon']
    latitude=data['coord']['lat']
    co_ordinates= "Lon-"+str(longitude)+", Lan-"+str(latitude)

    lbl_display['text']="In "+name+" ,"+country
    lbl_display1['text'] = "I'ts "+Des
    lbl_display2['text'] = "Temperature is " +str(temps)+" C"
    lbl_display3['text'] = "Wind Speed is "+str(wind)+ " Km/h"
    lbl_display4['text'] = co_ordinates


title_frame=Frame(root,bg='#17181a')
title_frame.place(relwidth=0.73,relheight=0.10,relx=0.12,rely=0.05)

frame0=Frame(root,bg='#17181a')
frame0.place(relwidth=0.75,relheight=0.11,relx=0.11,rely=0.20)

frame=Frame(root,bg='#bdffcd',borderwidth=5)
frame.place(relwidth=0.73,relheight=0.6,relx=0.49,rely=0.33,anchor='n')

l_title=Label(title_frame,text="Today's Wheather...",bg='#17181a', fg='#bdffcd',font=("helvatica",20,'bold'))
l_title.place(relwidth=0.90,relheight=0.70,relx=0.05,rely=0.15)

city_entry=Entry(frame0,borderwidth=2,bg='#17181a',fg='#bdffcd',font=("helvatica",16))
city_entry.place(relwidth=0.70,relheight=0.70,relx=0.02,rely=0.17)

btn_search=Button(frame0,text="Search",bg='#17181a', fg='#bdffcd',borderwidth=2,font=("helvatica",10,'bold'),command=lambda:search(city_entry.get()))
btn_search.place(relwidth=0.25,relheight=0.70,relx=0.74,rely=0.17)


lbl_display=Label(frame,text='',bg='#17181a',fg='#bdffcd',font=("helvatica",15))
lbl_display.place(relwidth=1,relheight=0.20,relx=0.00,rely=0.00)

lbl_display1=Label(frame,text='',bg='#17181a',fg='#bdffcd',font=("helvatica",15))
lbl_display1.place(relwidth=1,relheight=0.20,relx=0.00,rely=0.17)

lbl_display2=Label(frame,text='',bg='#17181a',fg='#bdffcd',font=("helvatica",15))
lbl_display2.place(relwidth=1,relheight=0.20,relx=0.00,rely=0.34)

lbl_display3=Label(frame,text='',bg='#17181a',fg='#bdffcd',font=("helvatica",15))
lbl_display3.place(relwidth=1,relheight=0.20,relx=0.00,rely=0.51)

lbl_display4=Label(frame,text='',bg='#17181a',fg='#bdffcd',font=("helvatica",15))
lbl_display4.place(relwidth=1,relheight=0.20,relx=0.00,rely=0.69)

lbl_display5=Label(frame,text='---------------------------',bg='#17181a',fg='#bdffcd',font=("helvatica",15))
lbl_display5.place(relwidth=1,relheight=0.14,relx=0.00,rely=0.86)










root.mainloop()