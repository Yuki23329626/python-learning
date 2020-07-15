# test Diffie-Hellman problem
import math

p, g = 23, 5

a=6
A = math.pow(g, a) % p
print("\nAlice chooses a=6, calculates A = g^a mod p = ", A, "and send A to Bob")

b=15
B = math.pow(g, b) % p
print("\nBob chooses b=15, calculates B = g^b mod p = ", B, "and send B to Alice")

s = math.pow(B, a) % p
print("\nAlice gets symmetric key s = B^a mod p = ", s)

s = math.pow(A, b) % p
print("\nBob gets symmetric key s = A^b mod p = ", s)

for i in range(1, 22):
    print("\n", math.pow(g, i) % p)