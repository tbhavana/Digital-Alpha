print("Enter a sentence with letters and digits")
sentence = input()
count_num = 0
count_letter = 0
for i in sentence:
	if(i.isdigit()):
		count_num += 1
	if(i.isalpha()):
		count_letter += 1
		
print("The number of letters in the sentence are - " + str(count_letter))
print("The number of digits in the sentence are - " + str(count_num))
