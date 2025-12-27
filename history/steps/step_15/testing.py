with open("dayereh.txt", "r") as file:
    content = file.read()
    print(content)
nume=content.split(",")
nums=[int(i)+1 for i in nume]
print(len(nums))
# middle number
middle_index = len(nums) // 2
gp1 = nums[:middle_index+1]
gp2 = nums[middle_index:]
print(gp1)
print(gp2)
print(len(gp1))
print(len(gp2))
print(gp1[-5:])
print(gp2[:5])
gp1=[str(i) for i in gp1]
gp2=[str(i) for i in gp2]
gp2=gp2[::-1]
print("Ramin: "," → ".join(gp1))
print("Mahsa: "," → ".join(gp2))