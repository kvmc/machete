import sys
from bs4 import BeautifulSoup as bs4

toolbar_width = 40
#setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '["

userInput = "old.html"

header = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<HTML>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<Title>Bookmarks</Title>\n<H1>Bookmarks</H1>\n<DT><H3 FOLDED>IMPORTED</H3>\n'    

footer = '<DL><p>\n\t\n\n\t</DL><p>\n</HTML>\t\n'

with open(userInput,"r") as f:
	parsedFile = bs4(f,"lxml").select('a')


for i in range(toolbar_width):

	with open("test.html","w") as f:
		f.write(header)
		for tag in set(parsedFile):
			f.write("\t\t<DT>")
			f.write(str(tag))
			f.write("\n")
		sys.stdout.write("-")
		sys.stdout.flush()
		f.write(footer)

sys.stdout.write("\n")
