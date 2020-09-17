import win32gui
import win32process
import win32api
import ctypes

window_handle = win32gui.FindWindow(None, 'Postman')
print(window_handle)

process_ids = win32process.GetWindowThreadProcessId(window_handle)
print(process_ids)
process_handle = win32api.OpenProcess(0x1f0fff,False, process_ids[1])
print(process_handle)
kernel32 = ctypes.windll.LoadLibrary(r'C:\Windows\System32\kernel32.dll')
data = ctypes.c_long()
kernel32.ReadProcessMemory(int(process_handle), 0x55555,ctypes.byref(data), 4, None)
print(data.value)