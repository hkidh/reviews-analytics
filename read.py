
data = []
count = 0
with open('reviews.txt', 'r') as f: #開檔案
	for line in f:					#一筆筆
		data.append(line)			#每筆加入data[]清單
		count += 1 					#計數每一筆(疊加)
#		if count % 10000 == 0: # %餘數 count 如果是1000的倍數
		x = len(data)			#總筆數
print('總共有', x, '筆')

print(data[0])
sum_len = 0  					#初終值
for d in data:					#data(清單)中每個
	sum_len += len(d) 			#計數清單中的字數
print('平均長度為:', sum_len/x)	#疊加字數/總筆數