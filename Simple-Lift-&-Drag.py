# This program calculates the lift and drag of an airplane.

# Equations:
# - Lift = Coefficient of lift * 0.50 * Density * Velocity² * WingSurfaceArea 
# - Drag = 0.50 * Density * TotalSurfaceArea * Coefficient of lift * Velocity²

# Wing Parameters
WingSurfaceArea = 0.85 # Meters^2 (Wing Surface Area Only)
WingSpan = 2.7 #Meters
CoLift = 0.45 

# Airplane Parameters 
TotalSurfaceArea = 2 # Meters^2 (Surface Area of the fuselage, Tail and Wing)
CoDrag = 0.09

# Simulation Parameters 
Velocity = 5 # Meters per second (Speed of the plane)
Density = 1.225 # kg/m^3 (Atmospheric pressure)

def Lift(): # Lift Equation
    Lift = CoLift * 0.50 * Density * pow(Velocity, 2) * WingSurfaceArea
    return Lift

def Drag(): # Drag Equation
    Drag = 0.50 * Density * TotalSurfaceArea * CoDrag * pow(Velocity, 2)
    return Drag 

print("Outputs: ")
print("Lift: " + str(Lift()) + " KG ")
print("Drag: " + str(Drag()) + " KG ")