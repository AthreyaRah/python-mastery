import time
f1 = open("somefile.txt")
f2 = open("somefile.txt")

print(f1.read())    # reads the ENTIRE file: ABCDEFGH
print(f2.read(3))   # reads first 3 characters


f = open("output.txt", "w")
f.write("Hello World")
# no f.close() here — program ends right after this line


f = open("output2.txt", "w")
for i in range(5):
    f.write(f"line {i}\n")
    print(f"wrote line {i}")
    time.sleep(2)
# still no close() — script is still running, hasn't exited yet


with open("output3.txt", "w") as f:
    for i in range(5):
        f.write(f"line {i}\n")
        print(f"wrote line {i}")
        time.sleep(1)
        if i == 2:
            raise ZeroDivisionError("simulated crash")
