import os

f=open('E:\\Ex_Files_Python\\test\hello.txt')

#for i in f:
#    print(i)

#content=f.read()
#print(content)


#print(f.readline())
#print(f.readline())


dummyfile=open('E:\\Ex_Files_Python\\test\hello_copy.txt','w')

for i in f:
    dummyfile.write(i)

f.close()
dummyfile.close()

ref=open('E:\\Ex_Files_Python\\test\hello_copy.txt')

for s in ref:
    print(s)

ref.close()

if os.path.exists('E:\\Ex_Files_Python\\test\hello_copy.txt'):
    os.remove('E:\\Ex_Files_Python\\test\hello_copy.txt')
else:
    print('No file found')


