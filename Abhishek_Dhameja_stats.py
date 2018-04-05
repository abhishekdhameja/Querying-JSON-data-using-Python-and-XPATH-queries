import sys
import json
import string

with open(sys.argv[1]) as data_file:
    json_data = json.load(data_file)
#print json_data['data'][0]['paragraphs'][0]['qas'][2]['answers'][0]

counts={'how':0,'how many':0,'how much':0,'what':0,'when':0,'where':0,'which':0,'who':0,'whom':0}
keys=counts.keys()
exclude = set(string.punctuation)
count=0
for data in json_data['data']:
    for para in data['paragraphs']:
        for qa in para['qas']:
            count+=1
            q = qa['question']
            firstword=q.strip().split(' ',2)[0].lower()
            secondword=q.strip().split(' ',2)[1].lower()
            if(firstword=='how' and (secondword=='much' or secondword=='many')):
                q=firstword+' '+secondword
            else:
                q=firstword
            q = ''.join(ch for ch in q if ch not in exclude)
            #print q
            for key in keys:
                if q.startswith(key):
                    if (key=='how' and (q=='how many' or q=='how much')):
                         continue
                    if (key=='who' and q=='whom'):
                         continue
                    counts[key]+=1
                #print q
# print count
#print counts
out=json.dumps(counts)
print out

with open('1a.json', 'w') as outfile:
    json.dump(counts, outfile)
print '1a.json file created.'