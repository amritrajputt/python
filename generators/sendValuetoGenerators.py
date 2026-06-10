def chai_customer():
    print("welcome what chai would you like?")
    order = yield  # if i dont give stall.send then i program wait because of yield but when i give enter the while true loop and print it then
    # again wait because there is another yield in while true loop
    while True:
        print(f"preparing: {order}")
        order =  yield

stall = chai_customer()
next(stall)       
stall.send("masala chai")
stall.send("ginger chai")