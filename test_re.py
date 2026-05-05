import re

str1 = "cell10"
str2 = "10"

id_1 = re.findall(r"\d+", str1)
id_2 = re.findall(r"\d+", str2)

print(type(id_1[0]))
print(id_2[0])