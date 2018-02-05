
# coding: utf-8

# In[61]:


import math


# First, create functions for each mode of failure - Isolate for desired variable 

# 1.Pin/Bolt failure due to shear [mm, N, MPa]

# In[88]:


def pin_shear(diameter, axial_load, shear_stress, solve_for):
    if(solve_for == "shear_stress"):
        value = axial_load / ((math.pi/4) * math.pow(diameter,2))
        print '{}{}{}'.format("Max Shear Stress = ", value, " MPa")
    elif(solve_for == "axial_load"):
        value = shear_stress * ((math.pi/4) * math.pow(diameter,2))
        print '{}{}{}'.format("Max Load = ", value, " N")
    else:
        print "Invalid values"
pass


# 2.Plate Rupture Due to Tension [mm, N, MPa]

# In[73]:


def plate_rupture(width, diameter, thickness, axial_load, normal_stress, solve_for):
    if(solve_for == "normal_stress"):
        value = axial_load / (thickness * (width - diameter))
        print '{}{}{}'.format("Max Normal Stress = ", value, " MPa")
    elif(solve_for == "axial_load"):
        value = normal_stress * (thickness * (width - diameter))
        print '{}{}{}'.format("Max Load = ", value, " N")
    elif(solve_for == "width"):
        value = ((axial_load / normal_stress) / thickness) + diameter
        print '{}{}{}'.format("Min Width = ", value, " mm")
    else:
        print "Invalid values"

pass


# 3.Plate Tearing Due to Shear [mm, N, MPa] 

# In[119]:


def plate_tearing(dist, thickness, axial_load, shear_stress, solve_for):
    if(solve_for == "shear_stress"):
        value = axial_load / (2 * thickness * dist)
        print '{}{}{}'.format("Max Shear Stress = ", value, " Mpa")
    elif(solve_for == "axial_load"):
        value = 2 * dist * thickness * shear_stress
        print '{}{}{}'.format("Max Load = ", value, " N")
    elif(solve_for == "dist"):
        value = axial_load / (2 * thickness * shear_stress)
        print '{}{}{}'.format("Min Distance from edge = ", value, " mm")
    else:
        print "Invalid values"
pass
        


# 4.Bearing Failure [mm, N, MPa]

# In[133]:


def bearing_failure(diameter, thickness, axial_load, normal_stress, solve_for):
    if(solve_for == "normal_stress"):
        value = axial_load / (thickness * diameter)
        print '{}{}{}'.format("Max Normal Stress = ", value, " MPa")
    elif(solve_for == "axial_load"):
        value = thickness * diameter * normal_stress
        print '{}{}{}'.format("Max Load = ", value, " N")
    else:
        print "Invalid Values"


# Constant Declarations Below (*Note: solve_for must remain 0, whereas we still have to calculate diameter and thicc)

# In[130]:


SOLVE_FOR = 0
DIAMETER = 122
THICKNESS = 10


# Demos:

# In[134]:


print "PIN SHEAR"
pin_shear(DIAMETER, 2000, SOLVE_FOR, "shear_stress")
pin_shear(DIAMETER, SOLVE_FOR, 200, "axial_load")

print "\nPLATE RUPTURE"
plate_rupture(300, DIAMETER, THICKNESS, 2000, SOLVE_FOR, "normal_stress")
plate_rupture(300, DIAMETER, THICKNESS, SOLVE_FOR, 400, "axial_load")
plate_rupture(SOLVE_FOR, DIAMETER, THICKNESS, 2000, 400, "width")

print "\nPLATE TEARING"
plate_tearing(1000, THICKNESS, 2434, SOLVE_FOR, "shear_stress")
plate_tearing(1000, THICKNESS, SOLVE_FOR, 2343, "axial_load")
plate_tearing(SOLVE_FOR, THICKNESS, 200, 2, "dist")

print "\nBEARING FAILURE"
bearing_failure(DIAMETER, THICKNESS, 1000, SOLVE_FOR, "normal_stress")
bearing_failure(DIAMETER, THICKNESS, SOLVE_FOR, 234, "axial_load")

