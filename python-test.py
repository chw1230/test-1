from random import *

cnt = 0
for i in range(50):
    time = randint(5,50)
    if(5<=time<=15):
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i+1,time))
        cnt = cnt + 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i+1,time))
print("총 탑승객 : {}명".format(cnt))