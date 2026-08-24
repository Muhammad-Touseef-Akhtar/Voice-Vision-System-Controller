# Voice and Vision System Controller

An **offline desktop automation system** built as an **Object-Oriented Programming (OOP) project**. The system allows users 
to control Windows applications and basic system functions using **voice commands and right-hand gestures**, without 
depending on a physical mouse or keyboard.

## 1. Project Overview

The system combines:

* **Offline Voice Recognition** using Vosk
* **Computer Vision** using OpenCV and MediaPipe
* **Gesture-Based Mouse Control**
* **Native Windows Automation** using C++ Win32 APIs
* **UDP Communication** between Python and C++
* **Multithreading and Shared State** for parallel voice and vision processing
* **Completely Offline Operation** after the required dependencies and Vosk model are installed

The Python side handles voice processing, camera input, hand tracking, and gesture detection. The C++ backend receives 
commands through **UDP Port 5005** and executes Windows-level operations.

---

# 2. Main Features

### Voice Control

Users can launch applications, navigate folders, control windows, and perform system operations using predefined voice 
commands.

### Vision Mouse Control

The webcam tracks the user's right hand and converts specific finger positions into mouse movement and click events.

### Offline Speech Recognition

The project uses the locally stored **Vosk English model**, so voice commands do not require an internet connection.

### Hybrid Python + C++ Architecture

Python manages computer vision and speech processing, while C++ performs native Windows automation through Win32 APIs.

### Multithreaded Processing

Voice and vision systems operate in parallel using separate threads and communicate through a shared state.

---

# 3. Voice Commands

The system recognizes multiple phrases for common operations.

### System

* **Settings:** `settings`, `set up`, `configuration`
* **Task Manager:** `task manager`, `manager`, `start manager`
* **This PC:** `folders`, `storage`, `this pc`, `my pc`
* **Calculator:** `calculator`, `open calculator`
* **Camera:** `camera`, `open camera`, `web cam`
* **Clock:** `clock`, `time`, `showtime`
* **Lock PC:** `lock computer`, `security`, `protect system`
* **Shutdown:** `shut down`, `close pc`, `shut down computer`
* **Restart:** `restart`, `reboot`

### Applications

* **Notepad:** `start editor`, `editor`, `notes`, `open notes`
* **Microsoft Word:** `open word`, `microsoft word`, `start word`, `documents`
* **Visual Studio:** `visual studio`, `open vs`, `vs`, `studio`
* **Code::Blocks:** `code block`, `cb`, `cpp`, `c plus plus`
* **Paint:** `sketch`, `draw`
* **WhatsApp:** `what's up`, `messages`, `start messages`
* **Browser:** `google`, `open google`, `edge`, `open edge`

### Files & Media

* **Videos:** `videos`, `open videos`
* **Music:** `music`, `songs`
* **Downloads:** `downloads`
* **YouTube:** `entertainment`, `movies`, `fun`

### Window Controls

* **Close:** `close`, `close application`, `remove`
* **Refresh:** `update`, `five`
* **Screenshot:** `screenshot`, `screen capture`, `take screenshot`
* **Exit Program:** `exit`, `exit program`, `stop program`

### Vision Control

* **Activate Mouse/Vision:** `switch`, `activate`, `vision`

---

# 4. Right-Hand Gesture Controls

Use your **right hand** in front of the webcam.

### Move Mouse

**Gesture:** Raise your **index and middle fingers** while keeping your **thumb straight**.

**Action:** Move your hand in the desired direction to control the mouse cursor.

**Image:**
<img  alt="Cursor Motion" src="https://github.com/user-attachments/assets/fa662a1b-3625-44cb-a36b-cf0ef476c5cb" />


### Stop Mouse Movement

**Gesture:** Keep your **index and middle fingers up** and **close your thumb**.

**Action:** Stops the cursor from following your hand.


### Left Click

**Gesture:** Keep your **middle finger up**, bend your **index finger**, and close your **thumb**. Keep the remaining fingers down.

**Action:** Performs a left mouse click.

**Image:**
<img alt="Left Click" src="https://github.com/user-attachments/assets/b007b0e1-712a-46c1-92d1-d9762ab3ef64" />


### Right Click

**Gesture:** Keep your **index finger up** and put your **middle finger down**, and close your **thumb**. Keep the remaining fingers down.

**Action:** Performs a right mouse click.

**Image:**
<img  alt="Right Click" src="https://github.com/user-attachments/assets/323d7c96-3a2b-445e-8c8f-a3c9ae250935" />


### Double Click

**Gesture:** Keep both your **index and middle fingers down**, and close your **thumb**. Keep the remaining fingers down.

**Action:** Performs a double left click.

---

# 5. Requirements

### Software

* Windows OS
* C++ compiler with `g++`
* Python 3.x
* Webcam
* Microphone
* Internet connection **only for initial dependency installation**

### Python Libraries

pip install opencv-python mediapipe pyaudio numpy pyautogui vosk

The Vosk model must remain inside the project directory:

vosk-model-small-en-us-0.15/


---

# 6. How to Run

Because the project uses a **Python + C++ hybrid architecture**, both components must run simultaneously.

## Terminal 1 — C++ Backend

Open a terminal in the project directory and run cpp code file  **Application_Commands_Executioner**. The C++ server will 
start listening on UDP Port: 5005.

---

## Terminal 2 — Python Engine

Open another terminal in the same project directory and run py file **Code_Running _Body**. The Python engine will 
initialize the voice and vision processing threads.

### Install dependencies

pip install opencv-python mediapipe pyaudio numpy pyautogui vosk

---

# 7. Windows Firewall

During the first execution of `.exe file`, Windows may display a **Windows Security Alert**.

If prompted:

1. Allow access for the application.
2. Enable **Private networks**.
3. Click **Allow access**.

The application uses UDP communication on **Port 5005** to communicate between the Python and C++ components.

---

# 8. Important Notes

* Keep the **C++ backend running before starting the Python engine**.
* Keep the Vosk model in the correct project directory.
* Make sure the webcam and microphone are available.
* Use the gestures clearly and within the camera's field of view.
* The system is designed for **Windows** because the C++ backend uses Win32 functionality.
* The system is designed to operate **offline** during normal use; no cloud speech-recognition service is required.
  
