#二維清單 記帳

import os #operating system

def read_file(filename):
	product = []
	with open(filename , 'r' , encoding = 'utf-8') as f :
		for line in f :
			if '商品,價格' in line :
				continue #跳到下一迴圈
			name, price = line.strip().split(',')
			product.append([name,price])
	return product

def user_input(product):
	while True :
		name = input('商品名稱 : ')
		if name == 'q' :
			break
		price = input('商品價格 : ')
		price = int(price)
		product.append([name , price])
	print(product)
	return product

def print_product(product):
	for p in product :
		print(p[0] , '價格是' , p[1])
	print('總共', len(product) ,'幾筆')

def write_file(filename,product):
	with open(filename , 'w' , encoding = 'utf-8') as f :
		f.write('商品,價格\n')
		for p in product :
			f.write(p[0] + ',' + str(p[1]) + '\n')



def main():
	
	filename = 'product.csv'
	if os.path.isfile(filename):
		print('yes!')
		product = read_file('product.csv')

	else :
		print('no!')

	product = user_input(product)
	print_product(product)
	write_file('product.csv',product)

#讓程式不要馬上執行
if __name__ == '__main__':
	main()

