import math

class Launcher:
    
    def predict(self, target):
        """Predits all possible angles of a given target, accounting for all possible power levels. Returns a dictionary of it's findings."""
        lowAngles = self.low(target)
        mediumAngles = self.medium(target)
        highAngles = self.high(target)
        
        # Remove invalid angles from low
        for i, angle in enumerate(lowAngles):
            if (angle != None and angle < -0.1 and angle >= 91):
                lowAngles[i] = None
                
        # Remove invalid angles from medium
        for i, angle in enumerate(mediumAngles):
            if (angle != None and angle < -0.1 and angle >= 91):
                mediumAngles[i] = None
                
        # Remove invalid angles from high
        for i, angle in enumerate(highAngles):
            if (angle != None and angle < -0.1 and angle >= 91):
                highAngles[i] = None
        
        # Return data
        return {"Low": lowAngles,
                "Medium": mediumAngles,
                "High": highAngles}
    
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
            angles[1] = round(-(-7.8803 + math.sqrt(-0.3956 * distance + 103.06746))/(0.1987), 3)
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
            angles[1] = round(-(-15.083 + math.sqrt(-0.7124 * distance + 334.620477))/(0.3562), 3)
        except ValueError:
            # Out of range
            pass
        except:
            print("ERROR: Unknown error has occurred during - side of high power setting calculation")
        
        return angles