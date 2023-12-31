import math

class Launcher:
    """
    The Launcher class is designed to predict the angle that is needed to launch a projectile 
    through the air to hit a specific target.\n
    The projectile launcher that is being used is from the University of Kansas physics department 
    for PHSX 216 - Physics I Laboratory. The angle of the launch is measured from 0 degrees to 90
    degrees directly on the launcher's body itself.\n
    The launcher also has 3 modes: low, medium, and high. The power of the launch is determined by
    these modes.\n
    The projectile that the launcher is using is a yellow 10 gram hollow plastic sphere that came 
    with the kit. A metal 67kg sphere is also provided which may provide more accurate short-distance 
    results, and implementation of such may be added in the future.
    """
    
    def predict(self, target):
        """Predits all possible angles of a given target, accounting for all possible power levels. Returns a dictionary of it's findings."""
        lowAngles = self.low(target)
        mediumAngles = self.medium(target)
        highAngles = self.high(target)
        angles = [lowAngles, mediumAngles, highAngles]
        
        # Remove invalid angles from low
        for setting in angles:
            for i, angle in enumerate(setting):
                if (angle == None):
                    break
                if (angle < -0.1 or angle >= 91):
                    setting[i] = None
        
        # Return data
        return {"Low": angles[0],
                "Medium": angles[1],
                "High": angles[2]}
    
    def low(self, distance):
        """Returns a list of possible angles (floats) in degrees given a distance for the low power setting"""
        angles = [None, None]
        
        # Try + side of equation
        try:
            angles[0] = round(-(-2.5527 + math.sqrt(-0.1464 * distance + 16.32258849))/(0.0732), 3)
        except ValueError:
            # Out of range
            pass
        except:
            print("ERROR: Unknown error has occurred during + side of low power setting calculation")
            
        # Try - side of equation
        try:
            angles[1] = round(-(-2.5527 - math.sqrt(-0.1464 * distance + 16.32258849))/(0.0732), 3)
        except ValueError:
            # Out of range
            pass
        except:
            print("ERROR: Unknown error has occurred during - side of low power setting calculation")
        
        return angles
            
    def medium(self, distance):
        """Returns an float angle in degrees given a distance for the medium power setting"""
        angles = [None, None]
        
        # Try + side of equation
        try:
            angles[0] = round(-(-7.8803 + math.sqrt(-0.3956 * distance + 103.06746))/(0.1987), 3)
        except ValueError:
            # Out of range
            pass
        except:
            print("ERROR: Unknown error has occurred during + side of medium power setting calculation")
            
        # Try - side of equation
        try:
            angles[1] = round(-(-7.8803 - math.sqrt(-0.3956 * distance + 103.06746))/(0.1987), 3)
        except ValueError:
            # Out of range
            pass
        except:
            print("ERROR: Unknown error has occurred during - side of medium power setting calculation")
        
        return angles
        
    def high(self, distance):
        """Returns an float angle in degrees given a distance for the high power setting"""
        angles = [None, None]
        
        # Try + side of equation
        try:
            angles[0] = round(-(-15.083 + math.sqrt(-0.7124 * distance + 334.620477))/(0.3562), 3)
        except ValueError:
            # Out of range
            pass
        except:
            print("ERROR: Unknown error has occurred during + side of high power setting calculation")
            
        # Try - side of equation
        try:
            angles[1] = round(-(-15.083 - math.sqrt(-0.7124 * distance + 334.620477))/(0.3562), 3)
        except ValueError:
            # Out of range
            pass
        except:
            print("ERROR: Unknown error has occurred during - side of high power setting calculation")
        
        return angles