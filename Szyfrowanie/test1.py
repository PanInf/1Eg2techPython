# # sha md5
# from hashlib import md5
# # print(md5(b"Eru5zk@-321").hexdigest())
# # print(md5(b"Gruszka2-345").hexdigest())
# # print(md5(b"K@m11@").hexdigest())
# # print(md5(b"G").hexdigest())

# passw = "Lubiepilke"
# print(md5(passw.encode("iso-8859-1")).hexdigest())

A = int(input())
B = int(input())

if (A + B) != 100: 
    print("SKANDAL")
elif A > B:
    print("Bitek")
elif B > A:
    print("Bajtek")
else:
    print("Remis")