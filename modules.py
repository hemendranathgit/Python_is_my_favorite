# import threading
# import time
# # print(time.ctime(0))
# # time_object=time.localtime()
# # time.strftime()
# # thread = a fllow of execution. Like a seperate order of instructions.
#
# def eat_breakfast():
#     time.sleep(3)
#     print("I am done with the breakfast")
#
# def drink_coffee():
#     time.sleep(4)
#     print("i drank coffee")
#
# def study():
#     time.sleep(5)
#     print("you finish studying")
#
# x=threading.Thread(target=eat_breakfast(),args=())
# x.start()
# y=threading.Thread(target=drink_coffee(),args=())
# y.start()
# z=threading.Thread(target=study(),args=())
# z.start()
#
# # eat_breakfast()
# # drink_coffee()
# # study()

#tkinter = which is used to create a GUI using the python
#widgets = gui elements: buttons, textboxes, lables, images.
#windows = serves as a container to hold or contain these widgets.

from tkinter import *

window = Tk() # instantiate an instance of a window

window.geometry("573x573")

window.mainloop()#To place the window on the main loop
