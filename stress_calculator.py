def calculate_stress(force, area):
    stress = force / area
    return stress

def calculate_factor(yield_stress, actual_stress):
    factor = yield_stress / actual_stress
    return factor

# Get inputs from user
force = float(input("Enter force applied (N): "))
area = float(input("Enter area (m^2): "))
yield_stress = float(input("Enter yield stress (MPa): "))
yield_stress_Pa = yield_stress * 1e6

# Calculate stress and safety factor
stress = calculate_stress(force, area)
factor = calculate_factor(yield_stress_Pa, stress)

required_factor = float(input("Enter required safety factor (example 2): "))

# Show results on screen
print(f"Calculated Stress: {stress/1e6:.2f} MPa")
print(f"Safety Factor: {factor:.2f}")

if factor > required_factor:
    print("Safe")
    status = "SAFE"
else:
    print("Failed")
    status = "FAILED"

# Save results to a file
with open("results.txt", "w") as f:
    f.write("=== Stress & Safety Factor Analysis ===\n")
    f.write(f"Force: {force} N\n")
    f.write(f"Area: {area} m^2\n")
    f.write(f"Yield Stress: {yield_stress} MPa\n")
    f.write(f"Calculated Stress: {stress/1e6:.2f} MPa\n")
    f.write(f"Safety Factor: {factor:.2f}\n")
    f.write(f"Required Factor: {required_factor}\n")
    f.write(f"Status: {status}\n")

print("\nResults saved to results.txt")

# Read back and show file contents to confirm
with open("results.txt", "r") as f:
    print("\n--- FILE CONTENTS ---")
    print(f.read())
