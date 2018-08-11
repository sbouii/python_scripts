def print_line_that_starts_with_char():
  with open("file.txt", "r") as f:
   for l in f.readlines():
    if l[0] == 't':
      print l

def print_line_that_contains_word():
  with open("file.txt", "r") as f:
   for l in f.readlines():
    words = l.split()
    print words
    for word in words:
     if word == 'test':
       print l
       print words

def find_out_if_a_line_starts_with_a_word():
 with open("file.txt", "r") as f:
  for l in f.readlines():
   if l.startswith("test mariem"):
     print l

def remove_empty_lines_from_file():
 for line in fileinput.FileInput("file.txt", inplace=1):
   line = line.rstrip()
   if line != '':
    print line

def remove_spaces_from_a_line():
 l = "mariem sbouii testing"
 sentence = ''.join(l.split())
 print sentence

def number_lines_of_file():
 with open("file.txt", "r") as f:
  print len(f.readlines())

def put_the_lines_of_file_in_dictionary():
 with open("file.txt", "r") as f:
  d = {}
  i = 0
  for line in f.readlines():
   d.update({i:line})
   i = i + 1

if __name__ == "__main__":

