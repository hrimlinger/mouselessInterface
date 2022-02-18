import ctypes
import logging
import os
import logging


class DLLLoader():
    def __init__(self) -> None:
        pass
    def load_lib(self) -> ctypes.CDLL:
    
        # Load the shared library into ctypes
        os.add_dll_directory("C:\\Users\\pepito\\Documents\\AI\\python_eye_interface\\touchlessInterfaceIHM\\dependencies")

        ctypes.cdll.LoadLibrary("onnx_importer.dll")
        ctypes.cdll.LoadLibrary("inference_engine_legacy.dll")
        ctypes.cdll.LoadLibrary("inference_engine_lp_transformations.dll")
        ctypes.cdll.LoadLibrary("inference_engine.dll")
        ctypes.cdll.LoadLibrary("opencv_imgproc440.dll")
        ctypes.cdll.LoadLibrary("opencv_imgcodecs440.dll")
        ctypes.cdll.LoadLibrary("opencv_highgui440.dll")
        ctypes.cdll.LoadLibrary("KERNEL32.DLL")
        ctypes.cdll.LoadLibrary("MSVCP140.DLL")
        ctypes.cdll.LoadLibrary("LIBMMD.DLL")
        ctypes.cdll.LoadLibrary("ngraph.dll")

        c_lib = ctypes.CDLL("userFaceAnalysisDLL.dll")

        logging.info("DLL and other required librairies were successfully loaded")

        return c_lib

        
