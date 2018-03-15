import random
rand1 = random.randint(1, 999999999)
print("Using " + str(rand1) + " as a random number")
user1_rand2 = random.randint(1, 999999999)
user2_rand2 = random.randint(1, 999999999)
private_user1 = user1_rand2 + rand1
private_user2 = user2_rand2 + rand1
print("Using " + str(private_user1) + " as a user1 private key")
print("Using " + str(private_user2) + " as a user2 private key")
public_user1 = private_user1 % 256
public_user2 = private_user2 % 256
print("Using " + str(public_user1) + " as a user1 public key")
print("Using " + str(public_user2) + " as a user2 public key")
pre_user1 = public_user2 + user1_rand2
pre_user2 = public_user1 + user2_rand2
print("Using " + str(pre_user1) + " for generating shared key user1")
print("Using " + str(pre_user2) + " for generating shared key user2")
shared_user1 = pre_user1 % 256
shared_user2 = pre_user2 % 256
print("Using " + str(shared_user1) + " that's the result of user1 key gen")
print("Using " + str(shared_user1) + " that's the result of user2 key gen")
print("Checking equality...")
if shared_user1 == shared_user2:
    print("Correct! Key exchange completed!")
else:
    print("Looks like math gone wrong...")
