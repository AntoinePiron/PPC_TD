import sysv_ipc

key = 128

mq = sysv_ipc.MessageQueue(key)

while True:
    print("Time request send 1")
    print("Termination request send 2")
    try:
        type = int(input("Request ID :"))
        if type != 1 and type != 2:
            print("Wrong values")
            exit(1)
    except:
        print("An error occured")
        exit(1)
    mq.send(0,type)
    if type == 1:
        message, t = mq.receive()
        time = message.decode()
        print("Time : ", time)
    elif type == 2:
        exit(0)
    