import nltk
import matplotlib.pyplot as plt
import numpy

#run pos tagger, change classes of words

dictionary - {
	"astrology" : "ASTROLOBOTOMY",
	"language" : "LANGUAG",
	"" : ""
}

sample = 'Critical explorations that deal with music as well as language often analyze ‘music as language’. In this translation, many sonic, and often, embodied aspects of music cognition and perception are missed. For example, treating melodic lines as notes has often missed the aspects of contour perception, and the motor aspects of melodic production. Exaggerated contour explorations are particularly common in infant babble---a slow exploration of the apparatus of enunciation, from vocables and vowels to non-speech sounds. Children repeat melodic contours and melodic phrases over and over during play. These infant melodies are essential to the development of speech and hearing. Specifically, contour acquisition is equally important to understand emotional nuances of speech as it is for remembering musical melodies. Whether our nuanced understanding of contours is developed for either speech or music is not a question this thesis explores; throughout history'

tokens = nltk.word_tokenize(sample)
print("tokens:", tokens)

tagged = nltk.pos_tag(tokens)

def convert(string):
	string = punctuation(string)
	string = capitalization(string)
	string = 
	return[complaintString]

def punctuation(string):
	return[punctustring]

def capitalization(string):
	return[capstring]

def changewords(string):
	#if find unique words in dictionary, change them to alternate spellings
	
