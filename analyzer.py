# ============================================
# Log Analyzer - Step 3
# Calculating outage duration from timestamps
# ============================================

from datetime import datetime   # NEW: Python's built-in time tool

# Step 1: Open and read the file
print("Opening log file...")
with open("sample_logs.txt", "r") as file:
    lines = file.readlines()

print(f"Found {len(lines)} log entries")
print("---")

# Step 2: Set up counters and lists
error_count   = 0
warning_count = 0
info_count    = 0
error_lines   = []
warning_lines = []

# Step 3: Count and collect
for line in lines:
    line = line.strip()
    if "ERROR" in line:
        error_count = error_count + 1
        error_lines.append(line)
    elif "WARNING" in line:
        warning_count = warning_count + 1
        warning_lines.append(line)
    elif "INFO" in line:
        info_count = info_count + 1

# Step 4: Summary
print("===== LOG SUMMARY =====")
print(f"INFO     : {info_count}")
print(f"WARNING  : {warning_count}")
print(f"ERROR    : {error_count}")
print("=======================")
print(f"Total logs: {len(lines)}")

# Step 5: Show errors and warnings
print("\n===== ERRORS DETECTED =====")
for error in error_lines:
    print(f"  ❌ {error}")

print("\n===== WARNINGS DETECTED =====")
for warning in warning_lines:
    print(f"  ⚠️  {warning}")

# Step 6: NEW — Calculate payment service outage duration
print("\n===== OUTAGE ANALYSIS =====")

# We know from the logs:
# 08:05:23 — payment service failed (ERROR)
# 08:06:20 — payment service timeout (ERROR)
# 09:01:15 — TIBCO reconnection attempt started

# Let's calculate how long the payment outage lasted
time_format = "%Y-%m-%d %H:%M:%S"   # tells Python how the date looks

payment_down     = datetime.strptime("2024-01-15 08:05:23", time_format)
payment_timeout  = datetime.strptime("2024-01-15 08:06:20", time_format)
tibco_down       = datetime.strptime("2024-01-15 09:00:00", time_format)
tibco_restored   = datetime.strptime("2024-01-15 09:02:30", time_format)

# Calculate the difference
payment_outage_seconds = (payment_timeout - payment_down).seconds
tibco_outage_seconds   = (tibco_restored - tibco_down).seconds

print(f"  🔴 Payment service outage  : {payment_outage_seconds} seconds")
print(f"  🔴 TIBCO EMS outage        : {tibco_outage_seconds} seconds ({tibco_outage_seconds // 60} min {tibco_outage_seconds % 60} sec)")
print(f"\n  📊 Total errors     : {error_count}")
print(f"  📊 Total warnings   : {warning_count}")

# Step 7: Health score (simple calculation)
total = len(lines)
health_score = round((info_count / total) * 100)
print(f"\n  💚 System health score : {health_score}%")

if health_score >= 70:
    print("  ✅ System status: HEALTHY")
elif health_score >= 50:
    print("  ⚠️  System status: DEGRADED")
else:
    print("  🚨 System status: CRITICAL")