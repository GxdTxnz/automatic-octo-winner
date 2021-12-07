import random
a = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I G K L M N O P Q R S T U V W X Y Z"
b = "1 2 3 4 5 6 7 8 9 0"
c = "% @ # $ &"
i =  0
d = ""
while i < 4:
	d = d + random.choice(a.split())
	i = i + 1
i = 0
while i < 4:
	d = d + random.choice(b.split())
	i = i + 1
i = 0
while i < 4:
	d = d + random.choice(c.split())
	i = i + 1
print(d)
