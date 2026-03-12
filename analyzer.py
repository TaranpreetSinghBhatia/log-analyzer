# ============================================
# Log Analyzer - Complete Version
# ============================================
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import datetime

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

# Step 6: Outage duration
print("\n===== OUTAGE ANALYSIS =====")
time_format      = "%Y-%m-%d %H:%M:%S"
payment_down     = datetime.strptime("2024-01-15 08:05:23", time_format)
payment_timeout  = datetime.strptime("2024-01-15 08:06:20", time_format)
tibco_down       = datetime.strptime("2024-01-15 09:00:00", time_format)
tibco_restored   = datetime.strptime("2024-01-15 09:02:30", time_format)

payment_outage_seconds = (payment_timeout - payment_down).seconds
tibco_outage_seconds   = (tibco_restored - tibco_down).seconds

print(f"  🔴 Payment service outage  : {payment_outage_seconds} seconds")
print(f"  🔴 TIBCO EMS outage        : {tibco_outage_seconds} seconds ({tibco_outage_seconds // 60} min {tibco_outage_seconds % 60} sec)")
print(f"\n  📊 Total errors     : {error_count}")
print(f"  📊 Total warnings   : {warning_count}")

# Step 7: Health score
total        = len(lines)
health_score = round((info_count / total) * 100)
print(f"\n  💚 System health score : {health_score}%")

if health_score >= 70:
    print("  ✅ System status: HEALTHY")
elif health_score >= 50:
    print("  ⚠️  System status: DEGRADED")
else:
    print("  🚨 System status: CRITICAL")

# Step 8: Generate chart
print("\n📊 Generating chart...")
categories = ["INFO", "WARNING", "ERROR"]
counts     = [info_count, warning_count, error_count]
colors     = ["#2ecc71", "#f39c12", "#e74c3c"]

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, counts, color=colors, width=0.5)

for bar, count in zip(bars, counts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        str(count),
        ha="center",
        fontsize=14,
        fontweight="bold"
    )

plt.title("Log Analysis Report — 2024-01-15", fontsize=16, fontweight="bold")
plt.xlabel("Log Level", fontsize=13)
plt.ylabel("Number of Entries", fontsize=13)
plt.ylim(0, max(counts) + 2)
plt.savefig("log_report.png")
print("✅ Chart saved! Look for log_report.png in your project folder on the left.")