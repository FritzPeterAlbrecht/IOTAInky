import inkyphat
from PIL import Image
from PIL import ImageFont
import InkyData as Ida
from time import sleep as s


# run the data fetch
s(10)
Ida.coininfo()

inkyphat.set_colour("red")

inkyphat.set_border(inkyphat.BLACK)
inkyphat.set_rotation(180)


img = Image.open("/home/pi/PythonScripts/IOTAInky/IotaInkyWhiteSBR.png")
inkyphat.set_image(img)

# Add the price text

font = ImageFont.truetype('/home/pi/PythonScripts/IOTAInky/Orbitron-Regular.ttf', 36)
price = Ida.price
pricestr = str(price)
inkyphat.text((4, 5), pricestr[0:5], inkyphat.RED, font)

# Add the change text

font = ImageFont.truetype('/home/pi/PythonScripts/IOTAInky/Orbitron-Regular.ttf', 22)
changed = Ida.changed
changedstr = str(changed)
if changed >= 0.0:
    inkyphat.text((7, 42), changedstr[0:5], inkyphat.BLACK, font)
if changed <= 0.0:
    inkyphat.text((7, 42), changedstr[0:5], inkyphat.RED, font)

# Add the ROI text

font = ImageFont.truetype('/home/pi/PythonScripts/IOTAInky/Orbitron-Regular.ttf', 34)
roi = Ida.roi
roistr = str(roi)

inkyphat.text((4, 75), roistr[0:7], inkyphat.WHITE, font)

inkyphat.show()