import webbrowser

trademePre = "https://www.trademe.co.nz/a/motors/cars/search?bof=PucvXiAC&user_region=2"

facebookPre = 'https://www.facebook.com/marketplace/category/vehicles?'

carjamPre = "https://www.carjam.co.nz/car/?plate="

turnersPre1 = "https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?"
turnersPre2 = "&locations=botany,manukau,otahuhu,north%20shore,panmure,penrose%20-%20great%20south%20road,westgate&pageno=1&sortorder=2&pagesize=120"

autotraderPre1 = "https://www.autotrader.co.nz/used-cars-for-sale/#!#0=0&1=0&2=0&3="
autotraderPre2 = "&8=1&9=10&10=0&11=48&12=&13=&14=&15=&16=&17=&18=&19=0&20=0&21=0&22=0&23=0&24=0&25=&26=&27=&28=&29=&30=&31=&32=&33=&34=&35=&36=&37=&38=&39=0&40=20&41=&42=&43=top&44=&45=0&46=&a0=%5B%5D&a1=%5B%5D&a2=%5B%5D&a3=%5B%5D&a4=%5B%5D&a5=%5B%5D&a6=%5B2433%5D&a7=%5B%5D&a8=%5B%5D&a9=%5B%5D&a10=%5B%5D&a11=%5B%5D&d="

plate='a'

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

print("Use default values? Y/N (500-6000 Odo: 160,000)")
defaultVal = input()
if defaultVal == 'Y':
    webbrowser.get("chrome").open("https://www.trademe.co.nz/a/motors/cars/search?bof=PucvXiAC&user_region=2&odometer_max=160000&price_max=5000&price_min=500&sort_order=motorsbuynowasc")
    webbrowser.get("chrome").open("https://www.facebook.com/marketplace/category/vehicles?minPrice=500&maxPrice=5000&exact=false")
    webbrowser.get("chrome").open("https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=2&pagesize=120&pageno=1&locations=botany,manukau,otahuhu,north%20shore,panmure,penrose%20-%20great%20south%20road,westgate&odoto=160000&pricefrom=500&priceto=6000")
    webbrowser.get("chrome").open("https://www.autotrader.co.nz/used-cars-for-sale/#!#0=0&1=0&2=0&3=160000&4=0&5=0&6=1000&7=6000&8=1&9=10&10=0&11=48&12=&13=&14=&15=&16=&17=&18=&19=0&20=0&21=0&22=0&23=0&24=0&25=&26=&27=&28=&29=&30=&31=&32=&33=&34=&35=&36=&37=&38=&39=0&40=20&41=&42=&43=top&44=&45=0&46=&a0=%5B%5D&a1=%5B%5D&a2=%5B%5D&a3=%5B%5D&a4=%5B%5D&a5=%5B%5D&a6=%5B2433%5D&a7=%5B%5D&a8=%5B%5D&a9=%5B%5D&a10=%5B%5D&a11=%5B%5D&d=")
    
else:
    print("Minimum Value?: ")
    minVal = input()
    print("Maximum Value?: ")
    maxVal = input()
    print("Odo max: ")
    odo = input()

    trademePost = (trademePre+"&odometer_max="+odo+"&price_max="+maxVal+"&price_min="+minVal+"&sort_order=motorsbuynowasc")
    facebookPost = (facebookPre+"minPrice="+minVal+"&maxPrice="+maxVal+"&exact=false")
    turnersPost = (turnersPre1+"odoto="+odo+"&pricefrom="+minVal+"&priceto="+maxVal+""+turnersPre2)
    autotraderPost = (autotraderPre1+odo+"&4=0&5=0&6="+minVal+"&7="+maxVal+""+autotraderPre2)

    print("Searching")

    webbrowser.get("chrome").open(trademePost)
    webbrowser.get("chrome").open(facebookPost)
    webbrowser.get("chrome").open(turnersPost)
    webbrowser.get("chrome").open(autotraderPost)

while plate!= "STOP":
    print("Enter carjam plate or enter STOP to stop")
    plate = input()
    if plate == "STOP":
        break
    carjamPost = (carjamPre + plate)
    webbrowser.get("chrome").open(carjamPost)

print("Program complete")


