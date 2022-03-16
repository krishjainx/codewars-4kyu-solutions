def order(sentence):
  # code here
		arrayOfWords = []  
		if sentence == "":
			return " "
		else:
			arrayOfUnordered = sentence.split(" ")
			arrayOfWords = [None] * len(arrayOfUnordered)
			for i in arrayOfUnordered:
				arrayOfWords[int(''.join(filter(lambda x: x.isdigit(), i)))-1] = i
		return arrayOfWords

	
