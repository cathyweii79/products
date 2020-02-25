#先讀取舊的檔案再存新的, 跳過首欄說明文字
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '購買商品,商品價格' in line:
			continue
		name, price = line.strip().split(',') 
		products.append([name, price])

print(products)

#讓使用者輸入資料
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

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('購買商品,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')