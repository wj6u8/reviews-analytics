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