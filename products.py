products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	
	#p = []
	#p.append(name)
	#p.append(price)
	
	#p = [name, price]

	products.append([name, price])

print('總計消費清單: ', products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('購買商品,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')