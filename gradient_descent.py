'''
To find the deepest point in the sand-pit this function uses a hybrid method.
This tries the Hessian unless the step would be too big, or it would point backwards, 
in which case it goes back to using steepest descent.
'''

def next_step(f, J, H) :
    gamma = 0.5
    step = -linalg.inv(H) @ J
    if step @ -J <= 0 or linalg.norm(step) > 2 :
        step = -gamma * J
    return step
