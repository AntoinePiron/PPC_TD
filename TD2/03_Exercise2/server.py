import sysv_ipc
import time

key = 128

mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

while True:
    message, t = mq.receive()
    value = message.decode()
    if t == 1:
        currTim = time.asctime()
        sendValue = currTim.encode()
        mq.send(sendValue, 3)
        pass
    elif t == 2:
        mq.remove()
        break
    else:
        print("Unknown message type")
    