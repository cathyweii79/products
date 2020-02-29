import os #operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'):    #os系統模組裡的path模組的isfile功能(檢查檔案在不在)
	print('找到檔案')

	with open('products.csv', 'r', encoding='utf-8') as f:   #先讀取舊的檔案再存新的, 跳過首欄說明文字
		for line in f:
			if '購買商品,商品價格' in line:
				continue  #繼續
			name, price = line.strip().split(',') 
			products.append([name, price])
	print(products)

else:
	print('找不到檔案...')


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