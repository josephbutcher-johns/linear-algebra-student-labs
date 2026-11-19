# Lab 05 Exercise 1: Explanation

Submit this file (or a `.txt` version) alongside your code, filled in with your own explanation.

Explain how floating-point rounding errors affect the orthogonality of the computed basis vectors and identify which of the three error measures captures this effect most clearly.

The main issue comes when making the vectors perpendicular. Computers cannot store infintley long decimals, so have to store them rounded. For this problem, roudning numbers during calculations causes rounding errors meaning that the vectors will not be exactly perpendicular. This means that rather than being orthogonal, they are almost orthogonal. The big problem comes when using the eps. The eps get smaller and smaller, so the algorithm is working with smaller numbers that are much more similar - the accuracy gets worse and worse as the computer cannot store an infinite amount of decimals. Error2 is whats measuring this, Q^TQ is getting further and further away from I_N as the numbers get smaller due to rounding errors. In an ideal world, Error 2 should be 0 but computers cannot deal with such small and similar floating-point numbers. 