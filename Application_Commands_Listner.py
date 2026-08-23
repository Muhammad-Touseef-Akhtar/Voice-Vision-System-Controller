import os
import cv2
import sys
import json
import socket
import pyaudio
import Shared_State as ss
from vosk import Model, KaldiRecognizer


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class OfflineSysController:
    
    def __init__(self, model_path="vosk-model-small-en-us-0.15"):
        
        self.net_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.c_plus_address = ('127.0.0.1', 5005)
        
        print(f"Loading local offline speech model from '{model_path}'...")
        
        if not os.path.exists(model_path):
            print(f"[CRITICAL ERROR] Download the model and place it in the '{model_path}' folder!")
            sys.exit(1)
            
        self.model = Model(model_path)
        
        self.recognizer = KaldiRecognizer(self.model, 16000)
        
        self.audio_hardware = pyaudio.PyAudio()
        self.stream = self.audio_hardware.open(
            format=pyaudio.paInt16, 
            channels=1, 
            rate=16000, 
            input=True, 
            frames_per_buffer=2048
        )
        
        self.stream.start_stream()
        self.Mouse_Switch = True 
        print("[SUCCESS] Offline hardware pipeline is locked and loaded.")

        self.SETTINGS       = ["settings", "set up",  "pc set up", "start configuration", "configuration", "start settings"]
        self.NOTEPAD        = [ "start editor", "editor", "notes","open notes"]
        self.EXIT_WINDOW    = ["close", "close application", "remove", "remove application"]
        self.BROWSER        = ["google", "open google", "start google", "edge", "open edge"]
        self.MS_WORD        = ["open word", "microsoft word", "start word", "start microsoft word", "open microsoft word", "right documents", "documents"]
        self.WHATSAPP       = ["open what's up", "what's up", "open messages", "messages", "start messages", "start what's up"]
        self.CALCULATOR     = ["open calculator", "calculator", "start calculator"]
        self.V_STUDIO       = ["open vs", "visual studio", "open visual studio", "vs", "start vs", "start visual studio", "studio"]
        self.FOLDERS        = ["open folders", "folders", "storage", "this pc", "pc", "my pc" ]
        self.CAMERA         = ["open camera", "camera", "picture", "image", "start camera", "web cam"]
        self.TASK_MANAGER   = ["open task manager", "task manager", "manager", "start manager"]
        self.SHUTDOWN       = ["shut down", "shutdown server", "close server", "close pc", "close computer", "shut down pc", "shut down computer", "computer down"]
        self.EXIT_PROGRAM   = ["exit", "exit program", "and program", "stop program"]
        self.LOCK_COMPUTER  = ["lock computer", "protect windows", "security", "go security", "close windows", "protect system"]
        self.CLOCK          = ["open cloak", "cloak", "start cloak", "time", "showtime", "open time", "view time"]
        self.YOUTUBE        = ["entertainment", "movies", "fun"]
        self.CODE_BLOCK     = ["code block", "cp", "cb", "open code block", "start code blocks", "cpp", "c plus plus"]
        self.PAINT          = ["sketch", "draw"]
        self.VIDEOS         = ["videos", "open videos"]
        self.MUSIC          = ["music", "songs"]
        self.DOWNLOADS      = ["downloads"]
        self.REFRESH        = ["update", "five"]
        self.RESTART        = ["restart", "reboot"]
        self.SNIPING_TOOL   = ["screenshot", "screen capture", "take screenshot"]
        self.MOUSE_SWITCING = ["switch", "activate", "vision"]
        
           
                  
    def process_intents(self, text):
            
            """Maps varying text phrases into explicit operating system shell operations."""
            
                 
            if any(phrase in text for phrase in self.SETTINGS):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_SETTINGS", self.c_plus_address)
                            
                            
            elif any(phrase in text for phrase in self.CAMERA):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_CAMERA", self.c_plus_address)
               
               
            elif any(phrase in text for phrase in self.V_STUDIO):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_VS_STUDIO", self.c_plus_address) 
                    
                    
            elif any(phrase in text for phrase in self.FOLDERS):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_FOLDERS", self.c_plus_address)
                    
                    
            elif any(phrase in text for phrase in self.TASK_MANAGER):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_TASK_MANAGER", self.c_plus_address) 
                    
                      
            elif any(phrase in text for phrase in self.NOTEPAD):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_NOTEPAD", self.c_plus_address)
                    
                    
            elif any(phrase in text for phrase in self.MS_WORD):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_MS_WORD", self.c_plus_address)
                
                
            elif any(phrase in text for phrase in self.WHATSAPP):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_WHATSAPP", self.c_plus_address)  
                    
                    
            elif any(phrase in text for phrase in self.CALCULATOR):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_CALCULATOR", self.c_plus_address)
                    
                    
            elif any(phrase in text for phrase in self.BROWSER):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_BROWSER", self.c_plus_address) 
                    
                    
            elif any(phrase in text for phrase in self.CLOCK):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_CLOCK", self.c_plus_address)
              
              
            elif any(phrase in text for phrase in self.YOUTUBE):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_YOUTUBE", self.c_plus_address) 
                    
                
            elif any(phrase in text for phrase in self.PAINT):
                     print("Vocabulary Match Found! Sending execution token to C++...")
                     self.net_socket.sendto(b"LAUNCH_PAINT", self.c_plus_address)
                     
                     
            elif any(phrase in text for phrase in self.SNIPING_TOOL):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_SNIPING_TOOL", self.c_plus_address)  
                     
                     
            elif any(phrase in text for phrase in self.CODE_BLOCK):
                     print("Vocabulary Match Found! Sending execution token to C++...")
                     self.net_socket.sendto(b"LAUNCH_CODE_BLOCK", self.c_plus_address)    
                             
                             
            elif any(phrase in text for phrase in self.VIDEOS):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_VIDEOS", self.c_plus_address)
                    
                    
            elif any(phrase in text for phrase in self.MUSIC):
                     print("Vocabulary Match Found! Sending execution token to C++...")
                     self.net_socket.sendto(b"LAUNCH_MUSIC", self.c_plus_address)
                     
                     
            elif any(phrase in text for phrase in self.DOWNLOADS):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LAUNCH_DOWNLOADS", self.c_plus_address)             
                
                
            elif any(phrase in text for phrase in self.EXIT_WINDOW):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"CLOSE_ACTIVE_WINDOW", self.c_plus_address)
                    
                    
            elif any(phrase in text for phrase in self.REFRESH):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"REFRESH_WINDOW", self.c_plus_address) 
                    
                    
            elif any(phrase in text for phrase in self.MOUSE_SWITCING):
                    ss.Mouse_active = not ss.Mouse_active
                    
                    if ss.Mouse_active:
                     print("Voice Engine: Signal received! Turning ON Mouse.")
                    else:
                     print("Voice Engine: Signal received! Turning OFF Mouse.")
                      
                                           
            elif any(phrase in text for phrase in self.RESTART):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"RESTART_PC", self.c_plus_address)        
                    
                    
            elif any(phrase in text for phrase in self.SHUTDOWN):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"", self.c_plus_address)
                
                
            elif any(phrase in text for phrase in self.LOCK_COMPUTER):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"LOCK_COMPUTER", self.c_plus_address)
                    
                    
            elif any(phrase in text for phrase in self.EXIT_PROGRAM):
                    print("Vocabulary Match Found! Sending execution token to C++...")
                    self.net_socket.sendto(b"EXIT", self.c_plus_address)
                    self.stream.stop_stream()
                    self.stream.close()
                    self.audio_hardware.terminate()
                    print("Voice Control System shut down safely.")
                    sys.exit(0)
                    exit_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    print("Sending shutdown command to C++ on Port 5005...")
                    exit_socket.close()
                        
                     
            
    def run_voice_loop(self):
        print("\n[LISTENING] Speak naturally to command your PC...")
        
        while True:
            #Capturing a raw binary chunk of sound waves from the hardware buffer
            audio_data = self.stream.read(2048, exception_on_overflow=False)
            
            #Feeding the sound bytes directly into the local AI to check if a phrase finished
            if self.recognizer.AcceptWaveform(audio_data):
                #Converting the raw phonetic text output from JSON into a Python Dictionary
                result_json = json.loads(self.recognizer.Result())
                spoken_text = result_json.get("text", "").lower()
                
                #Filtering out empty breaths or static pass real words to the intent mapper
                if spoken_text:
                    print(f"Heard : '{spoken_text}'")
                    self.process_intents(spoken_text)
            