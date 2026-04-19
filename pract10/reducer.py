#!/usr/bin/env python3
import sys

year_temps = {}

for line in sys.stdin:
    line = line.strip()
    try:
        year, temp = line.split("\t")
        temp = float(temp)
        if year not in year_temps:
            year_temps[year] = []
        year_temps[year].append(temp)
    except Exception:
        continue

# Calculate average temperature per year
avg_temps = {}
for year, temps in year_temps.items():
    avg_temps[year] = sum(temps) / len(temps)

# Print all year averages
print("\n--- Average Temperature Per Year ---")
for year in sorted(avg_temps):
    print(f"Year: {year}  |  Avg Temp: {avg_temps[year]:.2f}°C")

# Find coolest and hottest year
coolest_year = min(avg_temps, key=avg_temps.get)
hottest_year = max(avg_temps, key=avg_temps.get)

print("\n--- RESULT ---")
print(f"Coolest Year: {coolest_year}  |  Avg Temp: {avg_temps[coolest_year]:.2f}°C")
print(f"Hottest Year: {hottest_year}  |  Avg Temp: {avg_temps[hottest_year]:.2f}°C")
