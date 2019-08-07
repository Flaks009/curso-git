def repeatedString(s, n):
    a = 0
    aa = 0
    mod = n % len(s)

    for i in s:
        if i == 'a':
            a += 1

    for j in (s[:mod]):
        if j == 'a':
            aa += 1

    return  (a * (n // len(s)) + aa)



# def repeatedString2(s, n):
#     soma = 0
#     i = 0
#     j = 0
#     size = len(s)
#     while j < n:
#         if i == size:
#             i = 0
#         i += 1
#         j += 1
#     return soma

print(repeatedString('aab', 882787))
print(repeatedString('aba', 10))
print(repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570))