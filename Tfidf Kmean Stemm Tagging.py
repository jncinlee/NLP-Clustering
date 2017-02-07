#!/usr/bin/python
import codecs, nltk
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

#####Read data#####
q=[]

#read files

with open(r'D:\Berlin Play Data\Python\unclustered_input.txt','r',encoding='utf-8') as f:
    for line in f:
        q.append(line.split('\n'))

r = ['']*len(q)
for i in range(len(r)):
    r[i] = (q[i][0])

#mark up this part when without stemming tagging################
#tokenize
for i in range(0,len(r)):
        r[i] = nltk.word_tokenize(r[i])

#remove period, comma
for i in range(len(r)):
    if ',' in r[i]:
        r[i].remove(',')
    elif '.' in r[i]:
        r[i].remove('.')

#remove special charactor '“''„'
for i in range(len(r)):
    for j in range(len(r[i])):
        if '“' in r[i][j]:
            r[i][j] = r[i][j].strip('“')
        elif '„' in r[i][j]:
            r[i][j] = r[i][j].strip('„')

#taking the stem word (capital substantive)
t = ['']*len(r)
for i in range(len(r)):
    for j in range(len(r[i])):
        if r[i][j].istitle() == True :
            t[i] = t[i]+ ' ' + r[i][j]

for i in range(len(r)):
    t[i] = t[i].lstrip()

#mark up this part when without tagging################
#add keyword tagging 
u = ['']*len(t)
for i in range(len(t)):
    if ('Email' or 'Outlook' or 'Thunderbird') in t[i]:
        u[i] = t[i] + ' email'
    elif ('Install' or 'Admin' or 'Admin-Rechte' or 'Setup') in t[i]:
        u[i] = t[i] + ' setup'
    elif ('Maus' or 'Mauszeiger' or 'Zeiger' or 'Cursor' or 'Trackpad' or 'Mousepad' ) in t[i]:
        u[i] = t[i] + ' mause'
    else:
        u[i] = t[i]
#mark up this part when without tagging################
#mark up this part when without stemming tagging################


#####TFIDF matrix#####
'''
change u to t when without taggint
change u to r when without stemming tagging
'''
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(u)

Y=X.toarray()
word = vectorizer.get_feature_names()

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(u))
weight = tfidf.toarray()

#####Kmeans#####
clst = KMeans(n_clusters=5)
s = clst.fit(weight)
#print(s)

#print the center for 5 cluster
print(clst.cluster_centers_)
#print clustering result for each document
i = 1
while i <= len(clst.labels_):
    print(i, clst.labels_[i-1])
    i = i + 1
#print entropy index
print(clst.inertia_)

#output
simName = "Simple stemm kmean.txt"
result = codecs.open(simName, 'w', 'utf-8')

for j in range(len(clst.labels_)):
    result.write(str(j+1)+' '+ str(clst.labels_[j]))
    result.write('\r\n')
result.close() 
