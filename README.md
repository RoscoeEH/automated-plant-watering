# automated-plant-watering
This contains python code to be run on a raspberry pi that checks the moisture content of my house plants and sends an email tell which ones need to be watered. 

It works with some moisture sensors connected to ADCs that communicate with the raspberry pi.

The sensors output a 10-bit int to represent moisture with a higher number meaning less moisture and a lower number meaning more. The values when a plant needs to be watered will be determined experimentally for each plant.

If this works reasonably well I may also connect a water pump and have the watering be automated as well.