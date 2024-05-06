# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be false (an infinite loop). Inside the loop, print a statement. Then, use a break 
# statement to exit the loop after 5 iterations.

attempts = 1
while attempts >= 0:
   print(f"You are on attempt number {attempts}")
   attempts += 1
   if attempts == 6:
       break



# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop 
# should terminate naturally once the condition is met.

attempts = 1
while attempts <= 10:
    print(f"You are on attempt number {attempts}")
    attempts += 1
else:
    print("You are out of attempts. Please try again later.")