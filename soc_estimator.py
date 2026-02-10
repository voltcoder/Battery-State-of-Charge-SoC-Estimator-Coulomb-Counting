def estimate_soc(capacity_ah, current_a, time_h, initial_soc):
    discharged_ah = current_a * time_h
    soc_drop = (discharged_ah / capacity_ah) * 100
    remaining_soc = initial_soc - soc_drop

    return max(remaining_soc, 0)


try:
    capacity = float(input("Enter battery capacity (Ah): "))
    current = float(input("Enter discharge current (A): "))
    time = float(input("Enter time duration (hours): "))
    initial_soc = float(input("Enter initial SoC (%): "))

    if capacity <= 0 or current < 0 or time < 0:
        print("Invalid input values.")
    elif initial_soc > 100 or initial_soc < 0:
        print("Initial SoC must be between 0 and 100.")
    else:
        soc = estimate_soc(capacity, current, time, initial_soc)
        print(f"\nEstimated remaining SoC: {soc:.2f}%")

except ValueError:
    print("Please enter valid numeric values.")
