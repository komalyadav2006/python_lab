import os
import sys

# Current directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# List contents of current directory
print("\nContents of Current Directory:")
for item in os.listdir(current_dir):
    print(item)

# Create a workspace folder
workspace = os.path.join(current_dir, "workspace")

if not os.path.exists(workspace):
    os.mkdir(workspace)
    print("\nWorkspace folder created.")
else:
    print("\nWorkspace folder already exists.")

# List Python files in current directory
print("\nPython Files:")
for item in os.listdir(current_dir):
    if item.endswith(".py"):
        print(item)

# Command-line argument for log file
if len(sys.argv) > 1:
    log_file = sys.argv[1]
else:
    log_file = "activity.log"

log_path = os.path.join(workspace, log_file)

# Safely create/read log file using context manager
if os.path.exists(log_path):
    with open(log_path, "r") as file:
        content = file.read()

    print("\nLog File Content:")
    print(content)
else:
    with open(log_path, "w") as file:
        file.write("File Management Utility Started.\n")
        file.write("Workspace created successfully.\n")

    print("\nNew log file created:", log_path)

# Navigate into workspace
os.chdir(workspace)

print("\nCurrent Directory After Navigation:")
print(os.getcwd())

# Display files in workspace
print("\nFiles in Workspace:")
for item in os.listdir():
    print(item)

print("\nProgram completed successfully.")