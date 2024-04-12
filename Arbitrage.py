def swap_algo(i_token, o_token, amount):
    k = i_token * o_token
    new_amount = amount * 0.997
    new_o_token = k / (i_token + new_amount)
    token_balance  = o_token - new_o_token
    return token_balance 

liquidity = {
    ("tokenA", "tokenB"): (17, 10), 
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
# initial
path = []
path.append("B")

# B -> A
out_1st = swap_algo(10, 17, 5)
print("swap, tokenB->tokenA,", "AmountIn = ", 5, "AmountOut =", out_1st)
path.append("A")
# A -> C
out_2nd = swap_algo(11, 7, out_1st)
print("swap, tokenA->tokenC,", "AmountIn = ", out_1st, "AmountOut =", out_2nd)
path.append("C")
# C -> E
out_3rd = swap_algo(10, 8, out_2nd)
print("swap, tokenC->tokenE,", "AmountIn = ", out_2nd, "AmountOut =", out_3rd)
path.append("E")
# E -> D
out_4th = swap_algo(25, 60, out_3rd)
print("swap, tokenE->tokenD,", "AmountIn = ", out_3rd, "AmountOut =", out_4th)
path.append("D")
# D -> C
out_5th = swap_algo(12, 30, out_4th)
print("swap, tokenD->tokenC,", "AmountIn = ", out_4th, "AmountOut =", out_5th)
path.append("C")
# C -> B
out_6th = swap_algo(4, 36, out_5th)
print("swap, tokenC->tokenB,", "AmountIn = ", out_5th, "AmountOut =", out_6th)
path.append("B")


print("path: ", end="")
for i in range(len(path)):
  if (i != len(path) - 1):
    print(f'token{path[i]}->', end = "")
print(f'token{path[-1]}, ', end = "")
print("tokenB balance =", out_6th)
