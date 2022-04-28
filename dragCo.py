import time

startTime = time.time()
Output = open() #I nsert the Txt file Location inside the brackets

velocity = 0 # Meter per second 
density = 1.225 # kg/m^3
area = 0 # Meters^2 

DF = []
MinCodrag = 0 # Min Coefficent of drag
MaxCodrag = 0 # Max Coefficent of drag
steps = 0.005 # Steps between min & max
DataResolution = 100 # Loop times

I = MinCodrag 
r = 0 
print("start")
while I < (MaxCodrag+steps):
    # Prints the new Coefficient Number 
    RI = round(I, 5)
    print("CoDrag: ", RI)
    Output.writelines(" (CoDrag: " + str(RI)+") ")

    i = 0 
    velocity1 = velocity
    while i < DataResolution: 
        # Drag Force 
        # = Coefficent of Drag * (density * velocity/2) * Surface area 
        dragForce = I * (density*(velocity1*velocity1)/2)*area
        DFOutput = round(dragForce, 5)
        Output.writelines(" " + str(DFOutput))
        i = i + 1
        # Increases the velocity by +1 mps per loop
        velocity1 = velocity + (i-velocity+1)
        r = r + 1
    I=I + steps


# Shows the number of Calculations Done
executionTime = (time.time() - startTime)
print("Calculations performed =", round((I-(MinCodrag+steps))*100*DataResolution))
print("Execution Time = ", str(executionTime), "seconds")