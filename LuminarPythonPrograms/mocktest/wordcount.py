# Q4. "hello hai hello hai" = word count

lines="hello hai hello hai"
words=lines.split()
print(words)
dict={}
for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)

