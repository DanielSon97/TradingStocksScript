class Item:
	def __init__(self, name, amount, instant):
		self.name = name
		self.amount = amount
		self.instant = instant

def parse():
	#open html code
	htmlStream = open('element.txt', 'r')
	code = htmlStream.read()
	htmlStream.close()

	#find all items and info
	index = 0
	count = 0
	while True:
		#resetting defaults
		name = ""
		amount = ""
		instant = False

		#finding item name
		index = code.find('"row', index)
		if index == -1: break
		index += 1
		index = code.find('href="items.php', index) + 1
		index = code.find('class="', index) + 1
		index = code.find('>', index) + 1
		while True:
			if code[index] == '<':
				break
			name += code[index]
			index += 1

		#finding amount to buy
		index = code.find('center', index) + 1
		index = code.find('>', index) + 1
		while True:
			if code[index] == ' ':
				if code[index + 1] == 'I':
					instant = True
				break
			elif code[index] == '<':
				if code[index + 1] == 'b':
					index = code.find('>', index) + 1
				else:
					break
			else:
				amount += code[index]
				index += 1

		#inserting into buy list
		buyList.append(Item(name, int(amount.replace(',','')), instant))
		count += 1

def main():
	global buyList
	buyList = []
	parse()
	for i in range(len(buyList)):
		print(buyList[i].name + ' ' + str(buyList[i].amount) + ' ' + str(buyList[i].instant))

main()