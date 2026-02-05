import math
fuel_readings = []

while True:
    reading = float(input("Enter fuel usage in kg (-1 to stop): "))

    if reading == -1:
        break

    if reading < 0 or reading > 500:
        print("Invalid reading. Must be between 0 and 500 kg.")
        continue
    fuel_readings.append(reading)

# Display readings with index and compute total
total_fuel = 0

for i in range(len(fuel_readings)):
    print(f"Cycle {i}: {fuel_readings[i]} kg")
    total_fuel += fuel_readings[i]

# Calculations
num_cycles = len(fuel_readings)

if num_cycles > 0:
    average = total_fuel / num_cycles
    rounded_avg = math.ceil(average)
else:
    average = 0
    rounded_avg = 0
# Output results
print("\nSummary")
print("Number of engine cycles:", num_cycles)
print("Average fuel usage:", average)
print("Rounded-up average fuel usage:", rounded_avg)
