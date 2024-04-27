import pyshorteners

print("URL shortener")

url = input("Enter the url:")

short_url = pyshorteners.Shortener().tinyurl.short(url)

print("Short url : ", short_url)