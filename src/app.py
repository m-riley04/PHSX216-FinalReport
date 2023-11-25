from launcher import Launcher

class App:
    def __init__(self):
        self.launcher = Launcher()
    def run(self):
        # Begin main loop
        while True:
            try:
                target = float(input("Enter a target distance in centimeters: \n>> "))
            except ValueError:
                print("ERROR: Please enter a valid float for the target distance.")
            else:
                # Predict the angle(s) needed for the target's distance
                angles = self.launcher.predict(target)
                
                # Print output
                print(f"\nTarget Distance: {target} cm")
                for key, val in angles.items():
                    print(f"'{key}' Possible Angles: ")
                    # Check if no angles exist
                    if (all(v is None for v in val)):
                        print(f"\t> No possible angles found for power level '{key}'")
                    else:
                        # Print all angles except None values
                        for angle in val:
                            if (angle):
                                print(f"\t> {angle} degrees")
            print("\n--------------------------------\n")