import webbrowser
from tkinter import *

#Setting Variables
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

trademePre = "https://www.trademe.co.nz/a/motors/cars/search?bof=PucvXiAC&user_region=2"

facebookPre = 'https://www.facebook.com/marketplace/category/vehicles?'

carjamPre = "https://www.carjam.co.nz/car/?plate="

turnersPre1 = "https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?"
turnersPre2 = "&locations=botany,manukau,otahuhu,north%20shore,panmure,penrose%20-%20great%20south%20road,westgate&pageno=1&sortorder=2&pagesize=120"

autotraderPre1 = "https://www.autotrader.co.nz/used-cars-for-sale/#!#0=0&1=0&2=0&3="
autotraderPre2 = "&8=1&9=10&10=0&11=48&12=&13=&14=&15=&16=&17=&18=&19=0&20=0&21=0&22=0&23=0&24=0&25=&26=&27=&28=&29=&30=&31=&32=&33=&34=&35=&36=&37=&38=&39=0&40=20&41=&42=&43=top&44=&45=0&46=&a0=%5B%5D&a1=%5B%5D&a2=%5B%5D&a3=%5B%5D&a4=%5B%5D&a5=%5B%5D&a6=%5B2433%5D&a7=%5B%5D&a8=%5B%5D&a9=%5B%5D&a10=%5B%5D&a11=%5B%5D&d="

plate='a'

#GUI
window = Tk()

window.title("Car Program")

window.geometry('800x800')

title = Label(window, text="Car Program", font=("Arial Bold", 30))
title.grid(column=1, row=0)
minLabel = Label(window, text="Minimum Price")
minLabel.grid(column=0,row=2)
minLabel = Label(window, text="Maximum Price")
minLabel.grid(column=0,row=3)
minLabel = Label(window, text="Odometer Max")
minLabel.grid(column=0,row=4)
minFinal = Label(window, text="Minimum Price: ")
minFinal.grid(column=0,row=5)
maxFinal = Label(window, text="Maximum Price: ")
maxFinal.grid(column=1,row=5)
odoFinal = Label(window, text="Maximum KM's: ")
odoFinal.grid(column=2,row=5)

minPrice = Entry(window,width=20)
minPrice.grid(column=1, row=2)
maxPrice = Entry(window,width=20)
maxPrice.grid(column=1, row=3)
maxOdo = Entry(window,width=20)
maxOdo.grid(column=1, row=4)

def setMin():
    minimum = "Minimum Price: "+minPrice.get()
    minFinal.configure(text= minimum)

def setMax():
    maximum = "Maximum Price: "+maxPrice.get()
    maxFinal.configure(text= maximum)
    
def setOdo():
    odoM = "Minimum KM's: "+maxOdo.get()
    odoFinal.configure(text= odoM)

def search():
    #Add error check to see if values are entered
    #Create links with entry data
    odoVal = maxOdo.get()
    minVal = minPrice.get()
    maxVal = maxPrice.get()
    
    trademePost = (trademePre+"&odometer_max="+odoVal+"&price_max="+maxVal+"&price_min="+minVal+"&sort_order=motorsbuynowasc")
    facebookPost = (facebookPre+"minPrice="+minVal+"&maxPrice="+maxVal+"&exact=false")
    turnersPost = (turnersPre1+"odoto="+odoVal+"&pricefrom="+minVal+"&priceto="+maxVal+""+turnersPre2)
    autotraderPost = (autotraderPre1+odoVal+"&4=0&5=0&6="+minVal+"&7="+maxVal+""+autotraderPre2)
    #Opening pages with user values
    webbrowser.get("chrome").open(trademePost)
    webbrowser.get("chrome").open(facebookPost)
    webbrowser.get("chrome").open(turnersPost)
    webbrowser.get("chrome").open(autotraderPost)

minBtn = Button(window, text="Confirm Minimum Price", command=setMin)
minBtn.grid(column=2, row=2)
maxBtn = Button(window, text="Confirm Maximum Price", command=setMax)
maxBtn.grid(column=2, row=3)
odoBtn = Button(window, text="Confirm Odometer Maximum", command=setOdo)
odoBtn.grid(column=2, row=4)
searchBtn = Button(window,text="Search",command=search)
searchBtn.grid(column=0,row=6)


window.mainloop()
