import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from SaveSettings import *
import pickle
import inspect
FILE= pickle.load( open( "save.p", "rb" ) )
print (inspect.getmembers(FILE))
