import os #operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:   #先讀取舊的檔案再存新的, 跳過首欄說明文字
		for line in f:
			if '購買商品,商品價格' in line:
				continue  #繼續
			name, price = line.strip().split(',') 
			products.append([name, price])
	return products


#讓使用者輸入資料
def use_input(products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('購買商品,商品價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

#主要執行主程式的function
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):    #os系統模組裡的path模組的isfile功能(檢查檔案在不在)
		print('找到檔案')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	products = use_input(products)
	print_products(products)
	write_file(filename, products)

main()