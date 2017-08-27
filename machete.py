import sys
from bs4 import BeautifulSoup as bs4


header = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<HTML>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<Title>Bookmarks</Title>\n<H1>Bookmarks</H1>\n<DT><H3 FOLDED>IMPORTED</H3>\n'    
footer = '<DL><p>\n\t\n\n\t</DL><p>\n</HTML>\t\n'

with open("old.html","r") as f:
	parsedFile = bs4(f,"lxml").select('a')

with open("importme.html","w") as f:
	f.write(header)
	for tag in set(parsedFile):
		f.write("\t\t<DT>")
		f.write(str(tag))
		f.write("\n")
	f.write(footer)


#if __name__ == "__main__":
