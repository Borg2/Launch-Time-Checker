import time
import timeit
import pyautogui
import psutil

def is_process_running(process_name):

    for process in psutil.process_iter():
        try:
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


#running time of zoom
pyautogui.hotkey('winleft', 's')
pyautogui.typewrite('powerpnt')
pyautogui.press('enter')
start_time = timeit.default_timer()

while True:
    if is_process_running("powerpnt"):
        break
end_time = timeit.default_timer()

print("Time taken to open power point application: ", end_time - start_time)
time.sleep(1)

#running time of whatsapp
pyautogui.hotkey('winleft', 's')
pyautogui.typewrite('whatsapp')
pyautogui.press('enter')
start_time = timeit.default_timer()

while True:
    if is_process_running("whatsapp"):
        break
end_time = timeit.default_timer()

print("Time taken to open whatsapp application: ", end_time - start_time)
time.sleep(1)

#running time of codeblocks
pyautogui.hotkey('winleft', 's')
pyautogui.typewrite('codeblocks')
pyautogui.press('enter')
start_time = timeit.default_timer()

while True:
    if is_process_running("codeblocks"):
        break
end_time = timeit.default_timer()

print("Time taken to open codeblocks application: ", end_time - start_time)
time.sleep(1)


#running time of google chrome
pyautogui.hotkey('winleft', 's')
pyautogui.typewrite('google chrome')
pyautogui.press('enter')
start_time = timeit.default_timer()

while True:
    if is_process_running("Chrome"):
        break
end_time = timeit.default_timer()

print("Time taken to open google chrome application: ", end_time - start_time)
time.sleep(1)

#running time of microsoft 365(office)
pyautogui.hotkey('winleft', 's')
pyautogui.typewrite('microsoft 365')
pyautogui.press('enter')
start_time = timeit.default_timer()

while True:
    if is_process_running("office"):
        break
end_time = timeit.default_timer()

print("Time taken to open microsoft365 application: ", end_time - start_time)




