# ============================================
# Log Analyzer - Step 1
# Reading a log file and counting log levels
# ============================================

# Step 1: Open the log file and read all lines
print("Opening log file...")

with open("sample_logs.txt", "r") as file:
    lines = file.readlines()

print(f"Found {len(lines)} log entries")
print("---")

# Step 2: Set up counters (start at zero)
error_count   = 0
warning_count = 0
info_count    = 0

# Step 3: Go through every line and count
for line in lines:
    if "ERROR" in line:
        error_count = error_count + 1
    elif "WARNING" in line:
        warning_count = warning_count + 1
    elif "INFO" in line:
        info_count = info_count + 1

# Step 4: Print the summary
print("===== LOG SUMMARY =====")
print(f"INFO     : {info_count}")
print(f"WARNING  : {warning_count}")
print(f"ERROR    : {error_count}")
print("=======================")
print(f"Total logs: {len(lines)}")