import re

def swap(sentences):
	temp = sentences[0]
	sentences[0] = sentences[-1]
	sentences[-1] = temp
	print("The paragraph after swapping first and last sentence is -")
	print("----------------------------------------------------------")
	para = ""
	for i in range(len(sentences)):
		para += (sentences[i] + " ")
	
	print(para)
	
def count(paragraph):
	vowels = ['a','e','i','o','u']
	num_vowels = 0
	num_upper = 0
	num_lower = 0
	num_special = 0
	num_repeating = 0
	
	r = "[^0-9A-Za-z ]"
	
	for i in range(len(paragraph)):
		if paragraph[i].lower() in vowels:
			num_vowels += 1
			
		if paragraph[i].islower():
			num_lower += 1
		elif paragraph[i].isupper():
			num_upper += 1
		elif ( not paragraph[i].isalpha() and  not paragraph[i].isspace()):
			num_special += 1

	
	paragraph = re.sub(r," ",paragraph)
	repeating_words = {}
	words = paragraph.split(" ")
	#print(words)
	for x in range(len(words)):
		if words[x] in repeating_words:
			repeating_words[words[x]] += 1
		else:
			repeating_words[words[x]] = 1
	
	#print("###########################################################")
	print("The number of vowels in the paragraph are %d" %(num_vowels))
	print("The number of uppercases in the paragraph are %d" %(num_upper))
	print("The number of lowercases in the paragraph are %d" %(num_lower))
	print("The number of special characters in the paragraph are %d" %(num_special))
	print("The repeating words in the paragraph are the following -  ")
	for x,y in repeating_words.items():
		if y>=2:
			print(str(x) + "-->" + str(y)+ " times")
			

	print("Paragraph after removing all the special charaters is -")
	print("--------------------------------------------------------------")
	print(paragraph)
	

	
	
paragraph = input()
print("The paragraph entered is -")
print("------------------------------------------------")
print(paragraph) #printing the paragraph
print("------------------------------------------------")
sentences = paragraph.split(".") #assuming that sentences end with a full stop 
size = len(sentences)
middle = "UST Global specializes in Healthcare, Retail & Consumer Goods, Banking & Financial Services, Telecom, Media & Technology, Insurance, Transportation & Logistics and Manufacturing & Utilities."

if(size>=4):
	sentences[size//2] = middle  #updating the middle sentence
	para = ""
	for i in range(len(sentences)):
		para += (sentences[i]+" ")
	count(para)
	swap(sentences)
	
else:
	print("Please enter a paragraph with atleast 4 sentences")

