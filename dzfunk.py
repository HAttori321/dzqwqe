1
# def product(list):
#     product1=1
#     for num in list:
#         product1*=num
#     return product1
# mylist=[1,2,3,4,5]
# result=product(mylist)
# print(f"Добуток елементів списку: {result}")

2
# def findMinimum(list):
#     minimumValue=0
#     for element in list:
#         if element < minimumValue:
#             minimumValue=element
#     return minimumValue
# myList=[8,2,1,7,-3,9]
# result=findMinimum(myList)
# print(f"Minimum:{result}")
3
# def numPrime(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True

# def countNumPrime(list):
#     count=0
#     for element in list:
#         if numPrime(element):
#             count+=1
#     return count
# myList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# result=countNumPrime(myList)
# print(f"Кількість простих чисел: {result}")
5
# def list3(list1,list2):
#     list3=list1+list2
#     return list3
# list1=[1,2]
# list2=[3,4]
# result=list3(list1, list2)
# print("List3:", result)

6
# def stypin(list,exponent):
#     result=[element**exponent for element in list]
#     return result
# myList=[1,2,3,4,5]
# exponent=5
# result=stypin(myList,exponent)
# print(f"Ступінь: {result}")
