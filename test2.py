import bcrypt;

print(bcrypt.hashpw('password'. encode('utf-8'), bcrypt.gensalt()))