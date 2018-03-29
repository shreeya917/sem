# Here v=u+at where v is velocity, u is initial velocity, and t is time. And value for each is as follows: v=25m/s. u=0m/s, t=10 seconds.
# Find the acceleration a. [Rearrange the equation, also use proper formatting syntax while displaying the answer.]


def f(v,u,t):
    a=(v-u)/t
    return(a)


velocity= 25
initial_velocity=0
time=10
acceleration=f(velocity,initial_velocity,time)

print("\nAcceleration(a)=(v-u)/t\n\t\t\t\t=({}-{})/{}\n\t\t\t\t={}".format(velocity,initial_velocity,time,acceleration))
