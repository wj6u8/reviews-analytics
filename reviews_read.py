data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('讀取完畢,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('每筆留言平均用了', sum_len/len(data), '個字')

less_than100 = []
for d in data:
	if len(d) < 100:
		less_than100.append(d)
print('一共有', len(less_than100), '筆留言低於100個字' )

mention = []
for d in data:
	if 'Taiwan' in d:
		mention.append(d)
print('一共有', len(mention), '筆留言提到Taiwan')

#list comprehension (清單快寫法)

fast = [d for d in data if 'python' in d]
print('一共有', len(fast), '筆留言提到python')

#文字計數

word_count = {}
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word],'次')
		
print('留言中總共有', len(word_count),'個字')

while True:
	word = input('請輸入想查詢的字: ')
	if word == 'q':
		print('感謝使用本查詢功能')
		break
	if word in word_count:
		print(word, '總共出現', word_count[word], '次')
	else:
		print('留言中沒有這個字喔!')