print ("Введите слово:")
word = input()
word1 = len(word)
word = list(word)
a = (word1 // 2 - 1)
b = (word1 // 2)
if (word1) % 2==0 :
 print ("Результат:" + word[a] + word[b])
else:
  print ("Результат:"+word[b])
