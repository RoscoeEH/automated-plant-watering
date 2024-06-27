import spidev
from datetime import datetime


# This dictionary uses the moisture sensor number as the key and the watering threshold as the value
# Currently don't know what the threshold should be so I will just have it send values and will update them experimentally
PLANT_GLOSSARY = {0:256, 1:256, 2:256, 3:256, 4:256, 5:256, 6:256}
CHANNEL_NUM = 7

# Initializes spi
def spiOpen():

    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 1350000

    return spi

# Closes spi connection
def spiClose(spi):
    spi.close()

# Retrieves the water level from a specific channel
def getWaterLvl(spi, channel):

    if channel < 0 or channel > 7:
        return -1

    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]

    return data

# checks the value at each sensor and writes it to a separate file
def compareResults(spi):
    moistureLvls = []
    for channel in range(CHANNEL_NUM):
        moistureLvls.append(getWaterLvl(spi, channel))

    with open("moisture.txt", "w") as file:
        # adds date to the reading
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Current Time: {currentTime}\n")

        # Adds data to file
        for i, value in enumerate(moistureLvls):
            file.write(f"{i} -> {value}\n")

        # Adds line breaks for next entry to be read clearly
        file.write("\n---\n")

if __name__ == "__main__":
    spi = spiOpen()
    compareResults(spi)
    spiClose(spi)