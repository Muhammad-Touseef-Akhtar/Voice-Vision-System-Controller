import cv2
import time
import Hands_Tracking as ht
import Mouse_Events as me
import Shared_State as ss


# ----------------------------------------------------------------------------------------------------

def Mouse_Running():

      cap = None
      Previous_Time = 0
      Current_Time = 0
    
      H_detector = ht.Hand_Detection() 
      MF_detector = me.Mouse_Fingers_Detection()

      while True:
          
        if ss.Mouse_active:
            if cap is None:
                print("Camera Thread: Opening Web Camera Feed...")
                cap = cv2.VideoCapture(0)
          
          
            success, img = cap.read()

            if not success:
             print("Failed to grab camera frame. Exiting.....")
             time.sleep(0.1)
             continue

            img = cv2.flip(img, 1)

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = H_detector.hands.process(imgRGB)

            img = H_detector.Find_Hands(img, results)
            land_marks_list = H_detector.Find_Hand_Coordinates(results)
        
          
            if len(land_marks_list) > 0 :
              MF_detector.cursor_movement(land_marks_list)
              MF_detector.double_click(land_marks_list)
              MF_detector.left_click(land_marks_list)
              MF_detector.right_click(land_marks_list)

            Current_Time = time.time()
            Frame_per_sec = 1/(Current_Time-Previous_Time)
            Previous_Time = Current_Time
        
            cv2.imshow("Image", img)
            cv2.waitKey(1)
          
        else:
             if cap is not None:
                print("Camera Thread: Closing Camera Feed safely...")
                cap.release()
                cv2.destroyAllWindows()
                cap = None  
                
             time.sleep(0.2)    
   
        
        
        
        
  
        