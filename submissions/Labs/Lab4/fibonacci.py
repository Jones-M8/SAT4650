import statistics
import json

def analyze_ratios(ratios):
    # If the list is empty or if the user asked for only 1 item
    if not ratios:
        return "Not enough data to calculate ratios."
            
    # creating a dictionary to store results
    stats = {
        "minimum": round(min(ratios), 9),
        "maximum": round(max(ratios), 9),
        "mean": round(statistics.mean(ratios), 9),
        "median": round(statistics.median(ratios), 9),
        "mode": round(statistics.mode(ratios), 9),
        "final_ratio": round(ratios[-1], 9),
        # protective measure as the standard deviation requires at least two numbers
        "standard_deviation": round(statistics.stdev(ratios), 9) if len(ratios) > 1 else 0.0
    }
    return stats

def generate_fibonacci (n, start1, start2):

    if n <= 0:
        print("Error: Number of terms must be positive!")
        return []
    
    elif n == 1:
        print(f"Fibonacci sequence: {[start1]}")
        # No ratios possible with 1 number
        return []
    
    elif n == 2:
        print(f"Fibonacci sequence: {[start1, start2]}")
        # since one ratio exists here
        return [start2 / start1] if start1 != 0 else [] 
        
    fibo_series = [start1, start2]

    print(f"Starting sequence: {fibo_series}\n")

    for i in range (2, n):
        next_term = sum(fibo_series[-2:])
        fibo_series.append(next_term)

    print(f"Final Fibonacci sequence: {fibo_series}\n")

    # generating ratios
    ratios = []
    for i in range (1, len(fibo_series)):
        if fibo_series[i-1] != 0:
            current_ratio = fibo_series[i]/fibo_series[i-1]
            ratios.append(current_ratio)

    return ratios

# Getting user input (to use as parameters in function)
start1 = int(input("Enter first term or number of sequence: "))
start2 = int(input("Enter second term or number of sequence: "))
n = int(input("Enter the number of terms desired for your sequence: "))

# running the sequence generator for the sequence and ratios
ratios_list = generate_fibonacci(n, start1, start2)

ratio_analysis = analyze_ratios(ratios_list)

if type(ratio_analysis) == dict:
    final_output = {
        "sequence_length": n,
        "starting_values": [start1, start2],
        "ratio_statistics": ratio_analysis  # Nesting the stats here
    }
    for key, value in ratio_analysis.items():
        # Replace underscores with spaces and capitalize words for a clean look
        clean_key = key.replace("_", " ").title()
        print(f"{clean_key}: {value}")

    file_name = "fibonacci_stats.json"
    with open(file_name, "w") as json_file:
        # 'indent=4' used for improved readability
        json.dump(final_output, json_file, indent=4)

    print(f"Result saved to {file_name}")
else:
    # If it's not a dictionary, it must be an error
    print(ratio_analysis)