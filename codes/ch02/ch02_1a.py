file = open("prices.html")
text = file.read()
f.close()
price= text[234:238]
print(price)
