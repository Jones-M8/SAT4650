# 7. importing the math module
import math

total_fuel = 0
fuel_readings = []

while True:
    # 1. ask for input of fuel usage readings
    fuel_usage_reading = float(input("Please Enter fuel usage readings (0-500, or -1 to stop): "))
    # 2. use of sentinel value -1
    if fuel_usage_reading == -1:
        break
    # 3. rejection of invalid readings
    elif fuel_usage_reading < -1 or fuel_usage_reading > 500:
        continue
    # 5. storing valid readings in a list
    fuel_readings.append(fuel_usage_reading)

# 6.a Using for loop with range() to:Display each reading with its index
for i in range(len(fuel_readings)):
    # '+1' can be included for better user readability of output
    print("Reading", i, ":", fuel_readings[i])

    # 6.b Computing total fuel usage
    total_fuel = total_fuel + fuel_readings [i]


# 7. using imported math module to round up average fuel calculation
avg_fuel_used = total_fuel / len(fuel_readings)
rounded_up_avg = math.ceil(avg_fuel_used)

print("Total number of engine cycles: " + str(len(fuel_readings)) + "\n" +
      "Average fuel usage: " + str(avg_fuel_used) + "kg" + "\n" +
      "Rounded-up average fuel usage: " + str(rounded_up_avg) + "kg")
