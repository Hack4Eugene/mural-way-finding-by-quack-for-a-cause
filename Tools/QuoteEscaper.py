
rawText = open('rawText.txt')
lines = rawText.readlines()

for line in lines:
	newLine = line.replace('\"', '\\\"')
	print newLine