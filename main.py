import pickle
import re
import sys

def get_word_list(text):
   # Receives a string containing a document
   text = text.lower()  #convert all uppercase strings to lowercase
   emptyList = []      # Created empty list
   words = ''        #
   for i in text:
      if ord(i)>=97 and ord(i)<=122:
         words = words + i
      else:
         if len(words)>0:
            emptyList.append(words)
            words = ''
   return emptyList
def main():
   inputFile = sys.argv[1]
   outputFile = sys.argv[2]
   files = open(inputFile, 'r', encoding="utf8")
   text = files.read()
   files.close()
   text = get_word_list(text)
   text = sorted(text)
   dict = {}
   for word in text:
      if word not in dict:
         dict[word] = 1
      else:
         dict[word] = dict[word]+ 1
   files = open(outputFile, "w")
   for word in dict:
      files.write(word+" "+str(dict.get(word))+"\n")
   files.close()
   if __name__== "__main__":
      main()
