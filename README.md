# cup-problem
Problem statement: Given a glass of water with some volume of water in it, what is the maximum angle that we can tilt it so that it doesn't spill out?

We solve a similar problem: Given a full glass of water, if we hold it at an angle theta, how much liquid is left?

Given this, we can then interpolate an answer for the first problem.

Assume that a glass has radius 1 and height $h$.

Model this as a cylinder:
$(x-1)^2 + y^2 = 1, 0<=z<=h$

Let the tilt be a plane, e.g. $z = x$, which cuts the glass at a 45 deg angle from the mouth.
For generality we call this $z = mx$, where $m$ is the gradient of the line, from which the angle can be calculated, as $\arctan{m}$

To find the volume of water left, we need to find the $x$ coordinate that the plane intersects the circular base, which is $(x-1)^2 + y^2 = 1, z=h$

This is solved as $h = mx$, so $x = h/m$, notice that there can be a non-intersection with the base, if this value of $x$ does not lie in $[0,2]$.

The volume of air is thus total volume - volume under slope - volume under flat base.

Total volume: $PI*h$

Volume under slope: $\int_0 ^{\min(2,h/m)} \int_{-\sqrt{1-(x-1)^2}} ^ {\sqrt{1-(x-1)^2}}  mx dy dx$

Volume under flat base: $\int_{\min(2,h/m)}^2 \int_{-\sqrt{1-(x-1)^2}} ^ {\sqrt{1-(x-1)^2}} h dy dx$

which Wolfram evaluates to:

Volume under slope: $\frac{m}{3}\sqrt{-(x-2)x}(2x^2-x-3)-2m\arcsin{\sqrt{1-x/2}} + C$, evaluated from $0$ to $\min(2,h/m)$

Volume under flat base: $h(x-1)\sqrt{-(x-2)x} - 2h\arcsin{\sqrt{1-x/2}} + C$, evaluated from $\min(2,h/m)$ to $2$

We evaluate these for cylinders of height 1 to 10, for 1 to 89 degrees of the base from the horizontal:

![image](https://user-images.githubusercontent.com/67411893/214513696-f86f7c57-91b8-4b26-95bd-d2945bdcb018.png)


