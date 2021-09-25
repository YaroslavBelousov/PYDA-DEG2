boys = ["Peter","Alex","John","Arthur","Richard"]
girls = ["Kate","Liza","Kira","Emma","Trisha"]
if len(boys) != len(girls):
    print("Результат:Внимание, кто-то может остаться без пары!")
else:
  boys_girls = zip(sorted(boys),sorted(girls))
  for element,name in (boys_girls):
    print(element+" и "+ name)
