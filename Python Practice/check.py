# -*- coding: cp1252 -*-

def tester(givenstring = "Too short"):
	if len(givenstring) < 10:
		result = "Too short"
		return result
	else :
		if "X" in givenstring:
			return True
		

def main():
	while True:
		userstring = input("Write something (quit ends): ")
		if userstring == "quit":
			break
		result = tester(userstring)
		if result == True :
			print(userstring)
			print("X spotted!")
		else:
			print(result)
		
	
	
if __name__ == "__main__":
	main()