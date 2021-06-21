import webbrowser

trademePre = "https://www.trademe.co.nz/a/motors/cars/search?bof=PucvXiAC&user_region=2"

facebookPre = 'https://www.facebook.com/marketplace/category/vehicles?'

carjamPre = "https://www.carjam.co.nz/car/?plate="

plate='a'

print("Car Program")
print("Minimum Value?: ")
minVal = input()
print("Maximum Value?: ")
maxVal = input()
print("Odo max: ")
odo = input()

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

trademePost = (trademePre+"&odometer_max="+odo+"&price_max="+maxVal+"&price_min="+minVal+"&sort_order=motorsbuynowasc")
facebookPost = (facebookPre+"minPrice="+minVal+"&maxPrice="+maxVal+"&exact=false")

print("Searching")

webbrowser.get("chrome").open(trademePost)
webbrowser.get("chrome").open(facebookPost)

while plate!= "STOP":
    print("Enter carjam plate or enter STOP to stop")
    plate = input()
    if plate == "STOP":
        break
    carjamPost = (carjamPre + plate)
    webbrowser.get("chrome").open(carjamPost)

print("Program complete")


