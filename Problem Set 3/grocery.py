
#for i in sorted_list:
 #   for x in i:
  #      print(x, end=" ")



grocery_list = {}
try:
    while True:
        item = input().upper().strip()
        grocery_list[item] = grocery_list.get(item, 0) + 1

except EOFError:
        print()

sorted_list = dict(sorted(grocery_list.items()))



for key, value in sorted_list.items():
    print(value, key)