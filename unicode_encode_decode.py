def printer(text):
	print "------starting"
	print "TEXT: ", text
	temp = text.split('\t')
	for elem in temp:
		print elem.encode('utf-8')

if __name__ == '__main__':
	text = raw_input("Enter String: ").decode('utf-8')
	printer(text)
