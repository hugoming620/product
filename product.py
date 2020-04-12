#二維清單 記帳

#讀取檔案
product = []
with open('product.csv' , 'r' , encoding = 'utf-8') as f :
	for line in f :
		if '商品,價格' in line :
			continue #跳到下一迴圈
		name, price = line.strip().split(',')
		product.append([name,price])
print(product)

#讓使用者輸入商品價格
while True :
	name = input('商品名稱 : ')
	if name == 'q' :
		break
	price = input('商品價格 : ')
	price = int(price)
	product.append([name , price])

print(product)

#印出所有購買紀錄
for p in product :
	print(p[0] , '價格是' , p[1])

print('總共', len(product) ,'幾筆')


#寫入檔案
with open('product.csv' , 'w' , encoding = 'utf-8') as f :
	f.write('商品,價格\n')
	for p in product :
		f.write(p[0] + ',' + str(p[1]) + '\n')





