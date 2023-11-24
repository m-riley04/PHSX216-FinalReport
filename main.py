import math
from launcher import Launcher

def main():
    launcher = Launcher()
    while True:
        try:
            target = float(input("Enter a target distance: "))
        except ValueError:
            print("ERROR: Please enter a valid float for the target distance.")
        else:
            # Calculate
            angles = launcher.predict(target)
            
            # Print output
            print(f"Target Distance: {target} cm")
            for key, val in angles.items():
                print(f"'{key}' Possible Angles: ")
                # Check if no angles exist
                if (all(v is None for v in val)):
                    print(f"No possible angles found for power level '{key}'")
                else:
                    # Print all angles
                    for angle in val:
                        if (val):
                            print(f"\t> {val} degrees")
            print(f"Angle Needed: {angles} degrees")

if __name__ == '__main__':
    main()