import ctypes
import logging
import threading
from plot_inference_results import DynamicUpdate
from mouse_controller import MouseControler
import pyautogui
import logging
import numpy as np

from dll_loading import DLLLoader


# GLOBAL parameters, should be added.
MIN_TRESHOLD = 15
BUFFER_SIZE = 3 
MVT_DURATION = 0.1 # should not be changed
SPEED = 200 # speed must be given in pixel per seconds
ROW = 640
COLS = 480
show_inference_results = True

x = ctypes.c_float()
y = ctypes.c_float()
z = ctypes.c_float()

def load_and_start(c_lib):
    mainLoop = c_lib.mainLoop
    mainLoop.argtypes = [ctypes.POINTER(ctypes.c_float),ctypes.POINTER(ctypes.c_float)]
    #(rows, cols) = (img.shape[0], img.shape[1])
    # ,data.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))

    mainLoop(ctypes.byref(x),ctypes.byref(y),ctypes.byref(z))

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
    
    logging.info("Loading DLL...")

    dll_loader = DLLLoader()
    mouse_controler = MouseControler(SPEED,MVT_DURATION,[ROW,COLS], MIN_TRESHOLD,BUFFER_SIZE)

    logging.info("Application is starting")
    c_lib = dll_loader.load_lib()
    main_algo = threading.Thread(target=load_and_start, args=[c_lib])
    main_algo.daemon = True
    main_algo.start()
    logging.info("Press Ctrl-C for stopping application")
    try:
        while(True):

            mouse_controler.moveMouse(x.value,y.value)
            
    except KeyboardInterrupt:
        logging.info("Application was stopped")