# Write a function that reverses the
# - order of pages
# - order of lines in each page
# - order of words in each line
# - don't reverse the characters in each word

x = "the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"

def reverse_text(pages):
	curr_words = ""
	curr_line = []
	curr_page = []
    
	reversed_text = []
	final_text = ""
    
	i = 0
	while i < (len(pages)):
		# reached the end of a page
		if pages[i] == "\b":
			page = ""
			for a in range(len(curr_page)-1,-1,-1):
				page += curr_page[a]
				page += "\n"
			page += "\b"    
			reversed_text.append(page)
			curr_page = []
			i += 1
        	# reached the end of a line
		elif pages[i] == "\n":
            		# the last word before \n is not followed by a space
			curr_line.append(curr_words)
			curr_words = ""
			# reverse the current line
			line = ""
			for a in range(len(curr_line)-1,-1,-1):
			    line += curr_line[a]
			    line += " "
			# the last word before \n should not be followed by a space
			line = line[:-1]
			curr_page.append(line)
			curr_line = []
			i += 1
        	# reached the end of a word
		elif pages[i] == " ":
		    curr_line.append(curr_words)
		    curr_words = ""
		    i += 1
		else:
		    curr_words += pages[i]
		    i += 1
	# combine the list to a string
	for a in range(len(reversed_text)-1,-1,-1):
	    final_text += reversed_text[a]

	return final_text

def reverse_text_2(pages):
	return "\b\n".join(["\n".join([" ".join(line.split(" ")[::-1]) for line in page.split("\n")[::-1][1:]]) for page in pages.split("\b")[::-1][1:]])

print("original text:")
print(x)
print("reverse1:")
print(reverse_text(x))   
print("reverse2:")
print(reverse_text_2(x))
