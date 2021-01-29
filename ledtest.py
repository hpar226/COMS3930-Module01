# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import wget
import linecache

 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
 
# The number of NeoPixels
num_pixels = 8
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


try:
    time.sleep(4)
    #call API as specified
    url = 'http://worldtimeapi.org/api/ip/173.54.252.151.txt'

    wget.download(url, '/home/pi/pythonprojs/time_out.txt')
    
    #read in the current time as a string
    s = linecache.getline('/home/pi/pythonprojs/time_out.txt', 3)
    #find and store the decimals for seconds
    s2 = s[30:36]
    print("\ns2 = ", s2)
    #starting LED display as blue LED if even, and red LED if odd
    color = int(s2)%2
    
    print("color = ", color)
    
    if color == 0:
        while True:
            #show Blue, then cycle with Red
            pixels.fill((0, 0, 255))
            pixels.show()
            time.sleep(6)
            
            pixels.fill((0,255,0))
            pixels.show()
            time.sleep(3)
            '''
            rainbow_cycle(0.005)  # rainbow cycle with 1ms delay per step
            time.sleep(3)
	    '''
    if color == 1:
        while True:
            #show Red, then cycle with Blue
            pixels.fill((0, 255, 0))
            pixels.show()
            time.sleep(3)
            
            pixels.fill((0,0,255))
            pixels.show()
            time.sleep(6)
            '''
            rainbow_cycle(0.005)  # rainbow cycle with 1ms delay per step
            time.sleep(3)
	    '''
#turn off lights when exited w cntl-c
except KeyboardInterrupt:
    pixels.fill((0,0,0))
    pixels.show()
