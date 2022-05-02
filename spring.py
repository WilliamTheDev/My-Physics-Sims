#Calacutes the power of a spring using hooke's law
#Equations:
# - Spring Force = -k * x
# - Elastic Potential Energy = 1/2 * K * x^2

#Disclaimer: I'm not sure if this works right
#            I would double check the maths.


#E-E9 #0-7 #Spring Factors 
E  = [0.05, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040]
E1 = [0.010, 0.020, 0.020, 0.030, 0.027, 0.035, 0.040, 0.050]
E2 = [0.015, 0.030, 0.025, 0.040, 0.030, 0.040, 0.045, 0.060]
E3 = [0.020, 0.040, 0.030, 0.050, 0.033, 0.045, 0.050, 0.070]
E4 = [0.025, 0.050, 0.035, 0.060, 0.036, 0.050, 0.055, 0.080]
E5 = [0.030, 0.060, 0.040, 0.070, 0.039, 0.060, 0.060, 0.090]
E6 = [0.035, 0.070, 0.045, 0.080, 0.042, 0.070, 0.065, 0.100]
E7 = [0.040, 0.080, 0.050, 0.090, 0.045, 0.080, 0.070, 0.110]
E8 = [0.045, 0.090, 0.055, 0.100, 0.048, 0.090, 0.075, 0.120]
E9 = [0.050, 0.100, 0.060, 0.110, 0.051, 0.100, 0.080, 0.130]

N = 10 #Newtons Meters

def ElasticPotential(N, E):
    K = N/E 
    EP = (1/2) * K * (E*E)
    return EP

i = 0
print("10NM")
while 9 < N < 20: #10NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0 
print("20NM") 
while 19 < N < 30: #20NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0
print("30NM")
while 29 < N < 40: #30NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0
print("40NM")
while 39 < N < 50: #40NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0
print("50NM")
while 49 < N < 60: #50NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0
print("60NM")
while 59 < N < 70: #60NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0
print("70NM")
while 69 < N < 80: #70NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0
print("80NM")
while 79 < N < 90: #80NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1

i = 0
print("90NM")
while 89 < N < 100: #90NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1
    
i = 0
print("100NM")
while 99 < N < 110: #100NM
    print(ElasticPotential(N, E[i]))
    N = N + 1.25
    i=i+1