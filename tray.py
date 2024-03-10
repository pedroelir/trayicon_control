# from pywinauto import taskbar

# # taskbar.RightClickHiddenSystemTrayIcon("NVIDIA")
# taskbar.ShowHiddenIconsButton.click_input()
# niow_dlg = taskbar.explorer_app.window(class_name='NotifyIconOverflowWindow')
# niow_dlg.OverflowNotificationAreaToolbar.wait('ready', timeout=30)
# niow_dlg.SysLink.click_input()


from pywinauto import Application, findwindows
import time

app = Application(backend="uia").connect(path="explorer.exe")
st = app.window(class_name="Shell_TrayWnd")
t = st.child_window(title="Notification Chevron").wrapper_object()
t.click()

time.sleep(0.25)

list_box = Application(backend="uia").connect(class_name="NotifyIconOverflowWindow")
list_box_win = list_box.window(class_name="NotifyIconOverflowWindow")
list_box_win.wait('visible', timeout=30, retry_interval=3)
# list_box_win.dump_tree()
# # child = list_box_win.children_texts()
list_box_win.child_window(title_re="New quick").right_click_input()

time.sleep(0.25)

nvidia = Application(backend="uia").connect(path="ONENOTEM.EXE")
wins = nvidia.windows()
# wins2 = findwindows.find_windows(process="ONENOTEM.EXE")

context = nvidia.Context
menus = nvidia.Context["OneNote icon defaults"]
# child_window(title="OneNote icon defaults", control_type="MenuItem")
menus.wait(wait_for="visible ")
# context.dump_tree()
menu_obj = menus.wrapper_object()
menu_obj.click_input()
context.dump_tree()
print (nvidia.windows())
print(dir(menu_obj))


time.sleep(0.25)

# The new submenu could apear as a new window of the proces
# nvidia = Application(backend="uia").connect(path="ONENOTEM.EXE")
context = nvidia["OneNote icon defaults"]
context.dump_tree()


# from pywinauto import Desktop

# dsk = Desktop(backend='uia')
# # explorer = Application(backend="uia").connect(path="explorer.exe")
# # sys_tray = explorer.window(class_name="Shell_TrayWnd")

# # app_window = sys_tray.child_window(title="insert the name of application").click_input(button='right')

# # app_window = sys_tray.child_window(title="CCleaner").click_input(button='right')

# # dsk.Context.*insertthenameofoption*.click_input()

# ctx = dsk.Context
# ctx.dump_tree()