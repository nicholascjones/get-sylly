#!/usr/bin/env python

## GetSylly.py
## Nicholas Jones
## Course Project 2 -- Syllable Counter

#imports
import random
import string

#List Initialization for Syllable Counts

words = []
one = []
two = []
three = []
vowels = ['a','e','i','o','u']
vowels = set(vowels)

#functions

#reading words in from file
def ReadWords(inf='wordlist.10000'):

	#ensures readable words

	lst = open(inf,'r')
	for n in lst:
		n = n.rstrip() #sanitization
		if len(n) > 3:
			vc = 0
			ii = 0
			while ii < len(n):
				if n[ii] in vowels:
					words.append(n)
					break
				ii+=1




#count syllables in a given word
def CountSyllables(word):

	word = str(word) #ensuring type check
	word = word.lower()
	l = len(word) #length of word

	vcount = 0 #initializes vowel count to be 0
	i = 0 #iterator set to 0

	while (i < l):

		
		if (word[i] in vowels): #if is in vowels
			if i + 1 == l:
				if word[i] == 'e':
					break
				else:
					vcount+=1
					break
			elif (i + 2 == l) and (word[i] == 'e') and (word[i+1] == 'd'):
				vcount += 1
				i+=1
				continue
			elif word[i+1] in vowels:
					i+=1
					continue
			else:
				vcount += 1
		elif word[i] == 'y':
			if i == 0:
				i+=1
				continue
			elif word[i-1] not in vowels:
				if i + 1 == l:
					vcount+=1
				elif word[i+1] not in vowels:
					vcount+=1

		else:
			if word[i] not in vowels:
				if (i + 3 == l) or (i + 4 == l):
					if word[i+1] == 'l' and word[i+2] == 'e':
						vcount+=1
						break

		i+=1

	
	return vcount

#gets syllables for each word in list and assigns words to appropriate list
def GetSyllableCounts(inlist=words):

	for w in inlist:
		syl = CountSyllables(w)

		if syl == 1:
			one.append(w)
		elif syl == 2:
			two.append(w)
		elif syl == 3:
			three.append(w)

#		print w
#		print syl

	return


def MakeOneClause():

	n = random.randint(0,len(one)-1)
	phrase = one[n] + " "
	return phrase

def MakeTwoClause():

	rn = random.randint(0,2)

	if rn == 0:
		n = random.randint(0,len(two)-1)
		phrase = two[n] + " "
	else:
		p1 = MakeOneClause()
		p2 = MakeOneClause()
		phrase = p1 + p2

	return phrase

def MakeThreeClause():

	rn = random.randint(0,2)

	if rn == 0:
		n = random.randint(0,len(three)-1)
		phrase = three[n] + " "

	elif rn == 1:
		p1 = MakeTwoClause()
		p2 = MakeOneClause()
		phrase = p1 + p2
	else:
		p1 = MakeOneClause()
		p2 = MakeTwoClause()
		phrase = p1 + p2

	return phrase

def MakeFiveClause():

	rn = random.randint(0,2)


	if rn == 0:
		p1 = MakeThreeClause()
		p2 = MakeTwoClause()
		phrase = p1 + p2

	elif rn == 1:
		p1 = MakeTwoClause()
		p2 = MakeThreeClause()
		phrase = p1 + p2
	else:
		p1 = MakeOneClause()
		p2 = MakeThreeClause()
		p3 = MakeOneClause()
		phrase = p1 + p2 + p3
	return phrase


def MakeSevenClause():

	rn = random.randint(0,17)

	if rn < 5:
		p1 = MakeOneClause()
		p2 = MakeFiveClause()
		p3 = MakeOneClause()
		phrase = p1 + p2 + p3
	elif rn < 10:
		p1 = MakeTwoClause()
		p2 = MakeFiveClause()
		phrase = p1 + p2
	elif rn < 15:
		p1 = MakeFiveClause()
		p2 = MakeTwoClause()
		phrase = p1 + p2
	elif rn == 15:
		p2 = MakeOneClause()
		p1 = MakeThreeClause()
		p3 = MakeThreeClause()
		phrase = p1 + p2 + p3
	elif rn == 16:
		p1 = MakeOneClause()
		p2 = MakeThreeClause()
		p3 = MakeThreeClause()
		phrase = p1 + p2 + p3
	else:
		p3 = MakeOneClause()
		p2 = MakeThreeClause()
		p1 = MakeThreeClause()
		phrase = p1 + p2 + p3
	return phrase

def MakeHaiku():
	phrase = ""
	phrase += MakeFiveClause()
	phrase += "\n"
	phrase += MakeSevenClause()
	phrase += "\n"
	phrase += MakeFiveClause()
	phrase += "\n"
	return phrase


#de-facto main function initialization

#initialization at startup
ReadWords()
GetSyllableCounts()

#instructions
print "\n"
print "Hello, welcome to Nick's Syllable Counter and Random Haiku Generator!!"
print "\n"
print "Enter an 'h' to receive a Haiku!"
print "Enter a word to see how many syllables it has!"
print "Enter 'Q' to quit."
print "\n"
response = 'x' #generic response as to not cause problems

while (response != 'Q'): #case switch kills it all

	#prompt given with responses used to control flow
	response = raw_input("What would you like to do?\n")
	if response == 'Q':
		break
	elif response == 'h':
		print MakeHaiku()
	else: 
		try:
			print CountSyllables(response)
			print "\n"
		except ValueError:
			print "Invalid input. Please try again."
			continue
		


print "\n" #newline easy to print
#end execution









