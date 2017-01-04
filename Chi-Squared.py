
import time
from msvcrt import getch

inputNum = 0

observed = []

chi = []

print("")

print("Input EXPECTED below. Press ENTER to add OBSERVED. Press SPACE to compile. ")

print("")

expected = float(input("Expected: "))

while True:

	key = ord(getch())

	if key == 32:
		
		break
		
	print("")
	
	observedData = input("Observed #" + str(inputNum + 1) + ": ")
	
	observed.extend([float(observedData)])
	
	inputNum += 1

for number in observed:

	chi.extend([(number - expected) ** 2 / expected])
	
print("")

print("Chi-Squared value: " + str(sum(chi)))

print("")

input("")
	
