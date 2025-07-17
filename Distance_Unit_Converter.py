# The goal is to make a simple converter where you can either input km or mi and get the other out.

def main():
    user_choice()
    
def user_choice():
    while True:
        input_units = input("Would you like to do?\n1.Convert Miles to KM.\n2.Convert KM to Miles.\n3. Exit.\nEnter choice: ").strip().lower()
        if input_units == "1":
            distance = float(input("What is the distance you would like converted? "))
            print(f"{distance} miles is {round(distance * 1.60934, 3)} kilometers!")            
            
        elif input_units == "2":
            distance = float(input("What's the distance you would like converted? "))
            print(f"{distance} kilometers is {round(distance * 0.621371, 3)} miles!")
            
        elif input_units == "3":
            print("Goodbye!")
            return
        else:
            print("Please use the numbers 1, 2, or 3 to define your choice\nIf there's been an error, please yell at the programmer!\nhttps://github.com/Yukinononono")
            

main()

#I think this worked out well, I started out pretty overcomplicated but made it simpler in my opinion. No error handling is less than ideal though, I guess I could use something to get the type of error and use that for a customized output.