task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        message = "is a high priority task"    
    case "medium":
        message = "is a medium priority task"
    case "low":
        message = "is a low priority task"

if time_bound == "yes":
    print(f"Reminder: '{task}' {message} that requires immediate attention today!")
else:
    print(f"Note: '{task}' {message}. Consider completing it when you have free time."


