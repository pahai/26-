#~ 代表0到25
ls = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#~ 十进制数转26进制
def ten_to_26(number):
	if number<26:
		output = ls[number]
	else:	
		output = 	ls[int(number/26)] + ls[number%26]
	print(output)

#~ 26进制转10进制
def decode(word):
	if len(word) == 1:
		output = ls.index(word)
	else:
		output = 26*ls.index(word[0])	+ ls.index(word[1])
	print(output)
	
ten_to_26(159)
decode('CZ')
