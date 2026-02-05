import os

count = 0
# 1. Automatically accessing the folder
for root, dirs, files in os.walk("."):
    for filename in files:
        # 2. Locating the file
        if filename == "outdated_output.bin":
            # creating path of found file
            file_path = os.path.join(root, filename)
            print(f"Found: {file_path}")
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        
        # 5. Locating and renaming reactor file 
        elif filename == "reactor_output.bin":
            old_path = os.path.join(root, filename)
            new_name = "reactor_output_20260123.bin"
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

# Problem 2
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename == "process_log.txt":
            log_file_path = os.path.join(root, filename)
            break
if log_file_path:
    # 1. opens and reads content of process log file
    with open(log_file_path,'r') as file:
        all_lines = file.readlines()
    unsafe_keywords = ["ALERT", "ANOMALY", "CRITICAL", "WARNING", "FAILURE", "EXCEEDED"]
    unsafe_lines = []
    # 2. Identifies lines with unsafe indications
    for line in all_lines:
        if any(keyword in line for keyword in unsafe_keywords):
            unsafe_lines.append(line.strip())
    # 3. Prints unsafe conditions
    print("\nUNSAFE CONDITIONS FOUND: ")   
    for line in unsafe_lines:
        print(line)
    
    # 4. Writing to flagged_events.txt
    output_path = os.path.join(os.path.dirname(log_file_path), "flagged_events.txt")
    
    with open(output_path, 'w') as output_file:
        for line in unsafe_lines:
            output_file.write(line + "\n")
else:
    print("ERROR: process_log.txt not found!")
    



