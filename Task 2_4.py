countries_temperature = [
["Thailand", [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
["Germany", [57.2, 55.4, 59, 59, 53.6]],
["Russia", [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
["Poland", [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
from statistics import mean
for b in countries_temperature:
  a=(mean(b[1]) - 32 * 5 / 9) 
  print(b[0],":",a)
