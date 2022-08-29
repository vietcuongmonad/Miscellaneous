k = 0.00002
n = 7
r_star = (k*n) ** (1/(n+1))

def g(r):
    if (r >= r_star):
        return k/(r ** n)
    return -r + r_star * (1 + 1 / n)

def S(r_quote, r):
    return (g(r_quote) - g(r)) / (r_quote - r)

Ai = float(input("Asset of token i: "))
Li = float(input("Liability of token i: "))

Aj = float(input("Asset of token j: "))
Lj = float(input("Liability of token j: "))

# token j = (oracle_price) * token i
oracle_price = float(input("price of token j in term of token i: "))

delta_i = float(input("Swap how many token i to get token j: "))
delta_j = delta_i * oracle_price 

ri = Ai/Li
rj = Aj/Lj

ri_new = (Ai + delta_i) / Li
rj_new = (Aj - delta_j) / Lj

S_i_j = S(ri_new, ri) - S(rj_new, rj)
userReceive = delta_j * (1-S_i_j)

print("How many token j you get: ", userReceive)

print("Updated asset of token i: ", Ai + delta_i)
print("Updated asset of token j: ", Aj - userReceive)