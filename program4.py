tasks = []

while True:
    print("\n--- Task Scheduler ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Run Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Enter priority (high/low): ")
        tasks.append((task, priority))
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks scheduled.")
        else:
            print("\nScheduled Tasks:")
            for task, priority in tasks:
                print("Task:", task, "| Priority:", priority)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to run.")
        else:
            print("\nRunning Tasks:")
            
            for task, priority in tasks:
                if priority == "high" and task != "":
                    print("Executing high priority task:", task)
                elif priority == "low" or task != "":
                    print("Executing task:", task)
                else:
                    print("Task cannot be executed.")

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice. Please try again.")