#   import
import time
#   chosse
A = (int(input("chosse time : ")))
#   time going
while A > 0:
    print(str(A) + "sec" )
    time.sleep(1)
    A = A - 1
#   time stop
if A <= 0:
    print("stop stop stop!")
