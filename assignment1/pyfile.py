import urllib.request 

link1 = "https://www.hplovecraft.com/writings/texts/fiction/bws.aspx"
#f1= urllib.request.urlopen(link1)
f1=urllib.request.urlopen(link1)
file1= ((f1.read()).lower()).decode('utf-8')
link2 = "https://www.gutenberg.org/files/1342/1342-h/1342-h.htm"
#f2= urllib.request.urlopen(link2)
f2=urllib.request.urlopen(link2)
file2= ((f2.read()).lower()).decode('utf-8')
document1words = file1.split()
document2words = file2.split()

common = set(document1words).intersection(set(document2words))
print(common)
x= len(common)
print("The Number of Common Words is " + str(x))