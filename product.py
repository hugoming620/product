#二維清單 記帳


product = []

while True :
	name = input('商品名稱 : ')
	if name == 'q' :
		break
	price = input('商品價格 : ')
	price = int(price)
	product.append([name , price])

print(product)
	

for p in product :
	print(p[0] , '價格是' , p[1])

print('總共', len(product) ,'幾筆')

with open('product.csv' , 'w' , encoding = 'utf-8') as f :
	f.write('商品,價格\n')
	for p in product :
		f.write(p[0] + ',' + str(p[1]) + '\n')





