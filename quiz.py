print ("Welcome to my computer Quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()
    
print("Alright, let the fun begin!!:)")

answer = input("What is the capital of France? ")

score = 0

if answer.lower() == "paris":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
answer = input("What sport is known as the king of sports? ")

if answer.lower() == "football":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!:(")
    
answer = input("Who wrote the play Romeo and Juliet? ")

if answer.lower() == "william shakespeare":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!:(")
    
answer = input("What is the chemical symbol for water? ")

if answer.lower() == "H2O":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
answer = input("What planet is known as the Red Planet? ")

if answer.lower() == "mars":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!:(")
    
answer = input("What is the largest mammal in the world? ")

if answer.lower() == "blue whale":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
answer = input("How many continents are there on Earth?")

if int(answer) == 7:
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
answer = input("What is the square root of 64? ")

if int(answer) == 8:
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
    
answer = input("Who painted the Mona Lisa?")

if answer.lower() == "leonardo da vinci":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
    
answer = input("What is the fastest land animal? ")

if answer.lower() == "cheetah":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    

answer = input("In which year did the Titanic sink? ")

if int(answer) == 1912:
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    

answer = input("What is the currency of Japan? ")

if answer.lower() == "yen":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
    
answer = input("Who was the first person to walk on the moon? ")

if answer.lower() == "neil armstrong":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")


answer = input("What is the main ingredient in guacamole? ")

if answer.lower() == "avocado":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    

answer = input("What is the most spoken language in the world? ")

if answer.lower() == "mandarin chinese":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!:(")
    
    
print ("You got " + str(score) + " questions correct!")
print("You got " + str(round((score / 15) * 100)) + "%.")

