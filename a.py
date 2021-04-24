# R : (2 column :x,y)
# S : (2 column :y,z)
import time
import sys
import math
import heapq
import os
import ast

def sort_each_file(filename,col_number):
	input_content = open(filename,"r") 
	content1= input_content.readlines()
	content=[]
	for x in content1:
		x=x.split(" ")
		content.append(x)
	

	content.sort(key=lambda content:content[col_number]) 
	for x in content:
		x.insert(0,x[col_number])

	
	f=open(filename, "w")
	#print("writing to file:")
	for x in content:
		aa=""
		for x1 in x:
			aa=aa+x1+" "
		f.write(aa.rstrip()+"\n")
	f.close()
	
def mergeFiles(output_file, no_of_file,name):
	fp=[0]
	f=open(output_file,"w")
	heap=[]
	#print("No of files=")
	#print(no_of_file)
	d=dict()
	for i in range(1,int(no_of_file)+1) :
		ff=str(name+str(i)+".txt")
		chunks=open(ff,"r")
		temp=chunks.readline()
		if(temp==""):
			continue
		d[i]=temp
		temp=temp.strip("\n").split(" ")
		key=""
		key=key+temp[0] 
		
		heap.append((key,i))
		fp.append(chunks)

	heapq.heapify(heap)
	
	while(len(heap)>0):
		temp=heapq.heappop(heap)
		key,index=temp[0],temp[1]
		next_file=fp[index]
		next=next_file.readline()
		fp[index]=next_file
		a=d[index].split(" ")
		aainfile=""
		for aa in a[1:]:
			aainfile+= aa +" "
		f.write(aainfile.rstrip().strip("\n ")+"\n")
		d[index]=next
		next=next.strip("\n").split(" ")
		if(next[-1]==""):
			next=next[:-1]
		if(len(next)>0):
			key=""
			key=key+temp[0] 
			heapq.heappush(heap,(key,index))
			
	f.close()
	for i in range(1,int(no_of_file)+1):
		#print("Removing file")
		os.remove(name+str(i) +".txt")
	return

def open1(r_data,s_data,m):
	#1 sublist of size max m*100 tuples
	#Create sorted sublists for R and S, each of size M blocks.
	#r_data=r_data[:-1]
	no_of_lines_R=len(r_data)
	subfiles_R= math.ceil(no_of_lines_R/(int(m)*100))

	#create_small files now
	i=0
	number=int(1)
	filename="R"+str(number)
	filesize=int(m)*100

	while(i<=no_of_lines_R and i+filesize<=no_of_lines_R):
		output_content=r_data[i:i+filesize]
		f = open(str(filename)+".txt", "w")
		for x in output_content:
			f.write(x)
		f.close()
		number= int(number)+1
		filename="R"+str(number)
		i=i+filesize
	
	if i<no_of_lines_R:
		output_content=r_data[i:]
		f = open(str(filename)+".txt", "w")
		for x in output_content:
			f.write(x)
		f.close()
	#print("*****")
	#print(number)
	i=1
	while(i<=subfiles_R):
		filename="R"+str(i)
		sort_each_file(filename+".txt",1)	
		i=i+1

	mergeFiles("sorted_R.txt", subfiles_R,"R")
	#print("Sorted R merged file created!!!!!!!")

	i=0
	number=int(1)
	filename="R"+str(number)
	filesize=int(m)*100

	with open("sorted_R.txt", 'r') as f:
		r_data = f.readlines()
	f.close()

	no_of_lines_R=len(r_data)
	while(i<no_of_lines_R and number<=subfiles_R):
		output_content=[]
		xx=0
		while xx<int(m)*100 and i<no_of_lines_R:
			if r_data[i]!='\n':
				output_content.append(r_data[i])	
				xx+=1
			i=i+1
		#print("Opening file",filename)
		f = open(str(filename)+".txt", "w")
		for x in output_content:
			f.write(str(x.split()))
			f.write(str('\n'))
			#print("write",x)
		f.close()
		number= int(number)+1
		filename="R"+str(number)
	
	no_of_lines_S=len(s_data)
	subfiles_S= math.ceil(no_of_lines_S/(int(m)*100))

	#create_small files now
	i=0
	number=int(1)
	filename="S"+str(number)
	filesize=int(m)*100

	while(i<=no_of_lines_S and i+filesize<=no_of_lines_S):
		output_content=s_data[i:i+filesize]
		f = open(str(filename)+".txt", "w")
		for x in output_content:
			f.write(x)
		f.close()
		number= int(number)+1
		filename="S"+str(number)
		i=i+filesize
	
	if i<no_of_lines_S:
		output_content=s_data[i:]
		f = open(str(filename)+".txt", "w")
		for x in output_content:
			f.write(x)
		f.close()
	#print("*****")
	#print(number)
	i=1
	while(i<=number):
		filename="S"+str(i)
		sort_each_file(filename+".txt",0)	
		i=i+1

	mergeFiles("sorted_S.txt", number,"S")
	#print("Sorted S merged file created!!!!!!!")

	i=0
	number=int(1)
	filename="S"+str(number)
	filesize=int(m)*100

	with open("sorted_S.txt", 'r') as f:
	    s_data = f.readlines()
	f.close()

	no_of_lines_S=len(s_data)
	while(i<no_of_lines_S and number<=subfiles_S):
		output_content=[]
		xx=0
		while xx<int(m)*100 and i<no_of_lines_S:
			if s_data[i]!='\n':
				output_content.append(s_data[i])	
				xx+=1
			i=i+1
		#print("Opening file",filename)
		f = open(str(filename)+".txt", "w")
		for x in output_content:
			f.write(str(x.split()))
			f.write(str('\n'))
			#print("write",x)
		f.close()
		number= int(number)+1
		filename="S"+str(number)
	

	os.remove("sorted_R.txt")	
	os.remove("sorted_S.txt")	

	return subfiles_R,subfiles_S

def getnext1(subfiles_R,subfiles_S,output_file):
	#print("enyering")
	i=1 #file itertaor for R
	j=1 #file iterator for S
	flag=1

	iter_in_r=0
	iter_in_s=0

	with open("R"+str(i)+".txt", 'r') as f:
		r_rows = f.readlines()
		r_length=len(r_rows)
	f.close() 
	
	with open("S"+str(j)+".txt", 'r') as f:
		s_rows = f.readlines()
		s_length=len(s_rows)
	f.close() 
	
	f = open(output_file, "w")
	f.close()	
	#print("output file created")
	mark_s=[0,1] # (iter_in_s , then j)
	
	tuple_s = ast.literal_eval(s_rows[iter_in_s])
	tuple_r = ast.literal_eval(r_rows[iter_in_r])	
	#print("**************")
	#print(tuple_r)
	#print(tuple_s)
	while (i<=subfiles_R): #first while
		with open("S"+str(j)+".txt", 'r') as f:
			s_rows = f.readlines()
			s_length=len(s_rows)
		f.close() 
		with open("R"+str(i)+".txt", 'r') as f:
			r_rows = f.readlines()
			r_length=len(r_rows)
		f.close() 
		#print("!!!!!!!!!!!!!!!!!")
		#print(s_length)
		#print(r_length)
		tuple_s = ast.literal_eval(s_rows[iter_in_s])
		tuple_r = ast.literal_eval(r_rows[iter_in_r])	
		while(iter_in_r<r_length and iter_in_s<s_length): #2nd while
				#flag=1
				#print("enter 2nd while")
				tuple_s = ast.literal_eval(s_rows[iter_in_s])
				tuple_r = ast.literal_eval(r_rows[iter_in_r])	
				if mark_s[0]==0 and mark_s[1]==1:
					
					if ast.literal_eval(s_rows[0])[0]!=tuple_r[1]: 
						tuple_s = ast.literal_eval(s_rows[iter_in_s])
						tuple_r = ast.literal_eval(r_rows[iter_in_r])
						if iter_in_r==r_length  or iter_in_s==s_length:
							#print("break 1")
							break
						while((iter_in_r<r_length  and iter_in_s<s_length) and ast.literal_eval(r_rows[iter_in_r])[1]<tuple_s[0]):
							#print("enter 1")
							iter_in_r+=1
							#tuple_r = ast.literal_eval(r_rows[iter_in_r])
							#print("leave 1")	
						if iter_in_r==r_length  or iter_in_s==s_length:
							#print("break 1")
							break
						
						tuple_s = ast.literal_eval(s_rows[iter_in_s])
						tuple_r = ast.literal_eval(r_rows[iter_in_r])
						while((iter_in_r<r_length  and iter_in_s<s_length) and tuple_r[1]>ast.literal_eval(s_rows[iter_in_s])[0]):
							#print("enter 2")
							iter_in_s+=1
							#print("leave 2")

						if iter_in_r==r_length  or iter_in_s==s_length:
							#print("break 2")
							break
						tuple_r = ast.literal_eval(r_rows[iter_in_r])
						tuple_s = ast.literal_eval(s_rows[iter_in_s])
						mark_s=[iter_in_s,j]
				
				tuple_r = ast.literal_eval(r_rows[iter_in_r])
				tuple_s = ast.literal_eval(s_rows[iter_in_s])
				if tuple_r[1]==tuple_s[0]:
					#print("wohooo")
					#print(flag)
					flag+=1
					#print("")
					file1 = open(output_file, 'a')
					file1.write(tuple_r[0]+" "+tuple_r[1]+" "+tuple_s[0] + "\n")
					file1.close()
					iter_in_s+=1
					"""
					mark_s[0]=j
					mark_s[1]=iter_in_s
					mark_s=[0,1]
					"""

				else:
					#print("are yr")
					j=mark_s[1]
					iter_in_s=mark_s[0]
					iter_in_r+=1

					mark_s=[0,1]
					with open("S"+str(j)+".txt", 'r') as f:
						s_rows = f.readlines()
						s_length=len(s_rows)

					f.close() 
		if iter_in_s==s_length:
			iter_in_s=0
			j=j+1
			
		if j>subfiles_S:
			j=mark_s[1]
			iter_in_s=mark_s[0]
			iter_in_r+=1
			mark_s=[0,1]
			
		if iter_in_r==r_length:
			iter_in_r=0
			i=i+1
		#print("yayayya")	
	#print("finalllllyyyyyyyyyyyy")
	return 1



def close1():
	
	return


def sortMergeJoin(r_data,s_data,m,output_file):
	#1block = 100 tuples max
	subfiles_R,subfiles_S=open1(r_data,s_data,m) #Create sorted sublists for R and S, each of size M blocks.
	
	A=getnext1(subfiles_R,subfiles_S,output_file) #Use 1 block for each sublist and get minimum of R & S. Join this minimum Y value with the other table and return. 
	
	close1() # close all files
"""
Join condition (R.Y==S.Y).
Use 1 block for output which is filled by row returned by getnext() and when it gets full,
append it to the output file and continue.
"""

def polynomialRollingHash(str,m):
    p=31
    power_of_p=1
    m=int(m)
    hash_val=0
    for i in range(len(str)):
        hash_val=((hash_val + (ord(str[i]) - ord('a') + 1) * power_of_p) % m)
        power_of_p=(power_of_p * p) % m
    
    return int(hash_val)

def open2(r_data,s_data,m):
	
	no_of_lines_R=len(r_data)
	no_of_lines_S=len(s_data)
	m=int(m)
	for i in range(0,m):
		f = open("R"+str(i)+".txt", "w")
		f.close()
		f = open("S"+str(i)+".txt", "w")
		f.close()

	#create_small files now
	filesize=int(m)*100
	i=0
	while(i<=no_of_lines_R and i+filesize<=no_of_lines_R):
		output_content=r_data[i:i+filesize]
		for x in output_content:
			a=polynomialRollingHash(x.split(" ")[1].strip().strip("\n"),m)
			f = open("R"+str(a)+".txt", "a+")
			f.write(x)
			f.close()
			#print("***********")
			#print(a + " " +x,end="--")
		
		i=i+filesize
	
	if i<no_of_lines_R:
		output_content=r_data[i:]
		for x in output_content:
			a=polynomialRollingHash(x.split(" ")[1].strip().strip("\n"),m)
			f = open("R"+str(a)+".txt", "a+")
			f.write(x)
			f.close()
	
	i=0
	while(i<=no_of_lines_S and i+filesize<=no_of_lines_S):
		output_content=s_data[i:i+filesize]
		for x in output_content:
			a=polynomialRollingHash(x.split(" ")[0].strip().strip("\n"),m)
			f = open("S"+str(a)+".txt", "a+")
			f.write(x)
			f.close()
			#print("***********")
			#print(a + " " +x,end="--")
		
		i=i+filesize
	
	if i<no_of_lines_S:
		output_content=s_data[i:]
		for x in output_content:
			a=polynomialRollingHash(x.split(" ")[0].strip().strip("\n"),m)
			f = open("S"+str(a)+".txt", "a+")
			f.write(x)
			f.close()

	return

def getnext2(m,output_file):

	filename=output_file
	f = open(filename, "w")
	f.close()

	m=int(m)
	for i in range(0,m):
		with open("R"+str(i)+".txt", 'r') as f:
			r_rows = f.readlines()
			r_length=len(r_rows)
		f.close() 

		with open("S"+str(i)+".txt", 'r') as f:
			s_rows = f.readlines()
			s_length=len(s_rows)
		f.close()
		for x in r_rows:
			for y in s_rows:
				a=x.split(" ")[1].strip().strip("\n") 
				b=y.split(" ")[0].strip().strip("\n") 
				if a==b:
					f=open(filename, 'a+')
					f.write(x.rstrip("\n") + " "+ y.split(" ")[1].strip().strip("\n") +"\n" )
					f.close()	

	return


def close2(m):
	m=int(m)
	for i in range(0,m):
		os.remove("R"+str(i)+".txt")
		os.remove("S"+str(i)+".txt")
	return

def hashJoin(r_data,s_data,m,output_file):
	#1block = 100 tuples max
	open2(r_data,s_data,m)
	getnext2(m,output_file)
	close2(m)

start_time = time.time()
R_path = str(sys.argv[1])
S_path = str(sys.argv[2])
join_type= str(sys.argv[3])
m=str(sys.argv[4])

"""
print(R_path)
print(S_path)
print(join_type)
print(m)
"""
try:
	with open(R_path, 'r') as f:
	    r_data = f.readlines()
	f.close()    
	with open(S_path, 'r') as f:
	    s_data = f.readlines()
	f.close()

except:
	print("Invalid file path")

#print(r_data)
#print(s_data)

output_file=R_path+"_"+S_path+"_join.txt"

if(join_type=='sort'):
	sortMergeJoin(r_data,s_data,m,output_file)
elif join_type=='hash':
	hashJoin(r_data,s_data,m,output_file)
else:
	print("Invalid join type")

print("--- %s seconds ---" % (time.time() - start_time))
print("done")