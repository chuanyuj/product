products = [] # 有一個叫做 products 的空清單
while True: # 進入迴圈
	name = input('請輸入商品名稱：') # 請使用者輸入商品名稱，創建為 name
	if name == 'q': # 如果使用者輸入 q 
		break # 離開程式
	price = input('請輸入商品價格：') # 請使用者輸入商品價格，創建為 price
	products.append([name, price]) # 把 p 這個清單裝到 products 這個清單裡
print(products)

products[0][0] # products 清單的第  0 格中的第 0 格