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
#					if (i+3 == l):
#						if word[i] == 't' and (word[i+2] == 'd' or word[i+2] == 's'):
#							vcount += 1
#							break
					#if i + 3 < l:
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

	rn = random.randint(0,7)

	if rn < 5:
		n = random.randint(0,len(two)-1)
		phrase = two[n] + " "
	else:
		p1 = MakeOneClause()
		p2 = MakeOneClause()
		phrase = p1 + p2

	return phrase

def MakeThreeClause():

	rn = random.randint(0,8)

	if rn == 0:
		n = random.randint(0,len(three)-1)
		phrase = three[n] + " "

	elif rn < 4:
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







#de-facto main function initialization
ReadWords()

#print words

#print ('a' in vowels)

#print CountSyllables('underwritten')

GetSyllableCounts()

print CountSyllables('relax')
print CountSyllables('anal')

print CountSyllables('mounts')
print CountSyllables('output')

print "\n\n\n\n"


print MakeThreeClause()
print MakeThreeClause()
print MakeThreeClause()
print MakeThreeClause()
print MakeThreeClause()

print "\n hey \n"


print MakeFiveClause()
print MakeFiveClause()
print MakeFiveClause()
print MakeFiveClause()
print MakeFiveClause()
print MakeFiveClause()








