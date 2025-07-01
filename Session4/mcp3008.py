from gpiozero import LED,MCP3008
pot1 = MCP3008(0)
led = LED(17)
while True:
    print(pot1.value)
    led.blink(on_time= pot1.value, off_time= 1-pot1.value,n=1,background = False)
# n : so lan nhay led , xoa while True di de nhay 1 lan
# background: che do chay nen
