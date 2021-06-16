
data = []
count = 0
with open('reviews.txt', 'r') as f: #開檔案
	for line in f:					#一筆筆
		data.append(line)			#每筆加入data[]清單
		count += 1 					#計數每一筆(疊加)
#		if count % 10000 == 0: # %餘數 count 如果是1000的倍數
		x = len(data)			#總筆數
print('總共有', x, '筆')

#print(data[0])
#sum_len = 0  					#初終值
new = []
for d in data:					#data(清單)中每個
	if len(d) < 100:
 		new.append(d)
print('小於100字的留言有', len(new), '筆')
print(new[0])		
#	sum_len += len(d) 			#計數清單中的字數
#print('平均長度為:', sum_len/x)	#疊加字數/總筆數

good = []
for d in data:
 	if 'good' in d:
 		good.append(d)
print('一共有', len(good), '筆提到good')
print(good[0]) 





#文字計數

w_c = {} # word_count
for d in data:  			#將一筆一筆的讀
	words = d.split() 	#用空分出來的字,spolt預設即是空白鍵,不需(' ')
	for word in words:    	#將一個字一個字的讀
		if word in w_c:		#如果字有在字典中
			w_c[word] += 1	#將字在字典的數+1
		else:
			w_c[word] = 1 	#新增新的key進w_c字典

for word in w_c:
	if w_c[word] > 1000000:
		print(word, w_c[word])

print('出現過的字: ', len(w_c))
while True:
	keyin = input('請輸入要查詢的字: ')
	if keyin == 'q':
		break
	if keyin in w_c:
		print(keyin,'出現的次數為: ', w_c[keyin])
	else:
		print('查沒有這個字!!')

print('Thank You')






















