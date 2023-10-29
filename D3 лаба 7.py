RNA=str(input())
dict_RNA_in_DNA1={'A':'T', 'U':'A', 'G':'C', 'C':'G'}
dict_DNA1_in_DNA2={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
DNA1=''
DNA2=''
for i in RNA:
    DNA1=DNA1+str(dict_RNA_in_DNA1.get(i))
DNA1=DNA1.replace(' ','')
print(DNA1)

for j in DNA1:
    DNA2=DNA2+str(dict_DNA1_in_DNA2.get(j))
DNA2=DNA2.replace(' ','')
print(DNA2)
