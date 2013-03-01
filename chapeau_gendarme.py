from sympy import S, Eq, solve, cos, sin, pi
from sympy.plotting import plot

H, R, alpha, l, a , C = S('H R alpha l a C'.split())

equations = [
  Eq(H, 2*R*(1-cos(alpha))+l*sin(alpha)),
	Eq(C, a+2*R*sin(alpha)+l*cos(alpha))
	]

sol = solve(equations, l, a)
params = {R:42, C:150, H:30}


fun_l = sol[l].subs(params)
fun_a = sol[a].subs(params)

angle = pi/3

a = float(fun_a.subs({alpha : angle}))
b = a + float(params[R]*angle)
c = b + float(fun_l.subs({alpha : angle}))
d = c + float(params[R]*angle*2)
e = d + float(fun_l.subs({alpha : angle}))
f = e + float(params[R]*angle)

print "a = %s" % str(a)
print "b = %s" % str(b)
print "c = %s" % str(c)
print "d = %s" % str(d)
print "e = %s" % str(e)
print "f = %s" % str(f)





