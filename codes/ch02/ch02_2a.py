file = open("prices-loyalty.html")
text = file.read()
f.close()
where = text.find('>$')
start_of_price = where + 2
end_of_price = start_of_price + 4
price = float(text[start_of_price:end_of_price])
print(price)