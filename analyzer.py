# ============================================
# Log Analyzer - Step 2
# Now showing the actual error details too
# ============================================

# Step 1: Open the log file and read all lines
print("Opening log file...")

with open("sample_logs.txt", "r") as file:
    lines = file.readlines()

print(f"Found {len(lines)} log entries")
print("---")

# Step 2: Set up counters AND empty lists to store lines
error_count   = 0
warning_count = 0
info_count    = 0

error_lines   = []   # this will store the actual error lines
warning_lines = []   # this will store the actual warning lines

# Step 3: Go through every line and count + collect
for line in lines:
    line = line.strip()   # removes extra spaces/blank lines
    if "ERROR" in line:
        error_count = error_count + 1
        error_lines.append(line)      # save the full line
    elif "WARNING" in line:
        warning_count = warning_count + 1
        warning_lines.append(line)    # save the full line
    elif "INFO" in line:
        info_count = info_count + 1

# Step 4: Print the summary
print("===== LOG SUMMARY =====")
print(f"INFO     : {info_count}")
print(f"WARNING  : {warning_count}")
print(f"ERROR    : {error_count}")
print("=======================")
print(f"Total logs: {len(lines)}")

# Step 5: Print each error line
print("")
print("===== ERRORS DETECTED =====")
for error in error_lines:
    print(f"  ❌ {error}")

# Step 6: Print each warning line
print("")
print("===== WARNINGS DETECTED =====")
for warning in warning_lines:
    print(f"  ⚠️  {warning}")