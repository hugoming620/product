#二維清單 記帳


product = []

while True :
	name = input('商品名稱 : ')
	if name == 'q' :
		break
	price = input('商品價格 : ')

	p = []
	p.append(name)
	p.append(price)
	product.append(p)

	
print(product)



