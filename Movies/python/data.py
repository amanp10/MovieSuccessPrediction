from sys import argv
import json
import string

script,omdb,cinema=argv

#load and format all the data
fi1=open(omdb)
fi2=open(cinema)
st1=fi1.read()
st2=fi2.read()
j_data1=json.loads(st1)
j_data2=json.loads(st2)
list1=[]

#create data from omdb
for i in j_data1:
	dict1={}
	dict1['imdbID']=i['imdbID']
	dict1['Title']=i['Title']
	dict1['Actors']=i['Actors']
	dict1['Director']=i['Director']
	s1=i['Runtime']
	s1=s1.replace(' min','')
	try:
		i1=int(s1)
	except:
		i1=0
	if i1<60 or i1>180:
		dict1['Runtime']='1'
	elif (i1>60 and i1<90) or (i1<180 and i1>150):
		dict1['Runtime']='3'
	else:
		dict1['Runtime']='5'
	dict1['imdbRating']=i['imdbRating']
	dict1['Genre']=i['Genre']
	list1.append(dict1)

for i in list1:
	id1=i['imdbID']
	for j in j_data2:
		if id1 == j['ImdbId']:
			i1=int(j['Budget'])/100000000
			i['Budget']=str(i1)
			i['ReleaseDate']=j['ReleaseDate']


print len(list1)

fi=open('data.tsv','w')
for i in list1:
	fi.write((i['imdbID']+'\t'+i['Title']+'\t'+i['Actors']+'\t'+i['Director']+'\t'+i['Runtime']+'\t'+i['Budget']+'\t'+i['ReleaseDate']+'\t'+i['Genre']+'\t'+i['imdbRating']+'\t'+'\n').encode('utf-8'))

fi2.close()
fi1.close()
fi.close()

	
