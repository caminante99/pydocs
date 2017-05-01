import win32api
import win32con
import time

def click(rel=True):# con rel = False se queda pulsado
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    if rel == True:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_der(rel=True):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    if rel == True:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def get_pos():
    x, y = win32api.GetCursorPos()
    print '(' + str(x) + ', ' + str(y) + ')'

def move(x, y):
    win32api.SetCursorPos((x, y))
