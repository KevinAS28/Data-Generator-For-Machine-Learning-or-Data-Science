from combinator import main, linked_list
from time import sleep

#First, lets try the main method from the combinator
#so you can understand what exactly what the combinator do
input("To stop the loop, press CTRL+C. press enter to continue ")
try:
	main()
except KeyboardInterrupt:
	pass
#after you run the code above, you will see 100 of lists of number.
#each time the number reach the maximum base (which is 10. you can adjust it in combinator), the right side increased by 1

#We can use those lists, to creating the combination of our data

#lets define our data first.
data0 = ["a", "b", "c"]
data1 = ["d", "e", "f"]
data2 = ["g", "h", "i"]

print("\n"*3)

#looping
index = 0
while True:
	try:
		#initializing the linked list with max_size = 3 and the base_number = 3
		LL = linked_list(3, 3) 

		#increase the node by index
		LL[0]+=index 

		#get the combination List
		combination = LL.get_data() 

		#indexing our data with the combination list
		one_data = [data0[int(combination[0])], data1[int(combination[1])], data2[int(combination[2])]]

		#printing the combinated data
		print(one_data)
		
		index+=1
	except TypeError: #it will indicate the linked_list is reaching the maximum of size (3)
	 	print("Finish")
	 	break