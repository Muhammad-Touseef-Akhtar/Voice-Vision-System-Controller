import threading
import time
import Application_Commands_Listner as acl
import Mouse_Commands_Executioner as mce



# -------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    
    controller = acl.OfflineSysController("vosk-model-small-en-us-0.15")
    
    t1 = threading.Thread(target = controller.run_voice_loop, daemon = True)
    t2 = threading.Thread(target = mce.Mouse_Running, daemon = True)
    
    t1.start()
    t2.start()
    
    while True:
        time.sleep(1)