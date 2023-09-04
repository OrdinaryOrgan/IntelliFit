import multiprocessing
import os

def worker(file):
    os.system("python3 " + file)
    return

print("Program running... Press CTRL+C to exit")
files = ["EnvPublish.py","PosPublish.py"]
try:
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start() # 开启进程
except KeyboardInterrupt:
    print("Program terminated!")
    for i in files:
        p.terminate() # 结束进程
