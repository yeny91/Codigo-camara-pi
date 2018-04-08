
# Este codigo sirve para tomar una foto con la camara pi, en la raspberry pi 3
# Este codigo es adaptado de http://pitando.australiando.es/2015/11/26/modulo-de-camara-para-la-raspberry-pi/

import picamera
camara = picamera.PiCamera()
camara.capture("test_python.jpeg")
camara.close()
