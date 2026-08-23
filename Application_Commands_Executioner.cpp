#include <iostream> 
#include <winsock2.h> 
#include <windows.h> 
#include <shellapi.h>
using namespace std; 

#pragma comment(lib, "ws2_32.lib") 


// -----------------------------------------------------------------------------------------------------------------------------------


int main() { 
    // Allocating the Windows Sockets Data structure configuration layout
    WSADATA win_network_drivers; 
    
    // Booting up the Winsock DLL drivers (Requesting Version 2.2 profiles)
    WSAStartup(MAKEWORD(2, 2), &win_network_drivers); 
    
    SOCKET communication_antenna = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP); 
    
    // Configure the network address, protocol family, and target application Port
    sockaddr_in portConfig; 
    portConfig.sin_family = AF_INET; 
    portConfig.sin_port = htons(5005);          // Locks listener onto Port 5005
    portConfig.sin_addr.S_un.S_addr = ADDR_ANY; // Listen to incoming signals from any local engine
    
    // Binding the socket antenna directly to laptop's internal network ports
    bind(communication_antenna, (sockaddr*)&portConfig, sizeof(portConfig)); 
    
    cout << "C++ Active. Listening for System Commands on Port 5005..." << endl; 
    
    char networkBuffer[1024]; 
    sockaddr_in senderDetails; 
    int senderSize = sizeof(senderDetails); 
    
    while(true) { 
        
        memset(networkBuffer, 0, 1024); 
        
        int bytesCaught = recvfrom(communication_antenna, networkBuffer, 1024, 0, (sockaddr*)&senderDetails, &senderSize); 
        
        if (bytesCaught > 0) { 
            string command_word(networkBuffer); 
            
            if (command_word == "EXIT") { 
                cout << endl << "Exit signal received from Python. Closing server cleanly..." << endl; 
                break; 
            }
            else if (command_word == "LAUNCH_SETTINGS") {
                cout << "Executing: Opening Settings..." << endl;
                ShellExecuteA(NULL, "open", "ms-settings:", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_NOTEPAD") {
                cout << "Executing: Opening Notepad Editor..." << endl;
                ShellExecuteA(NULL, "open", "notepad.exe", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_MS_WORD") {
                cout << "Executing: Opening MS_word..." << endl;
                ShellExecuteA(NULL, "open", "winword.exe", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_CALCULATOR") {
                cout << "Executing: Opening Calculator..." << endl;
                ShellExecuteA(NULL, "open", "calc.exe", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_WHATSAPP") {
                cout << "Executing: Opening Whatsapp..." << endl;
                ShellExecuteA(NULL, "open", "whatsapp:", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_BROWSER") {
                cout << "Executing: Navigating to Web Search Engine..." << endl;
                ShellExecuteA(NULL, "open", "https://google.com", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_VS_STUDIO") {
                cout << "Executing: Launching VS Studio..." << endl;
                ShellExecuteA(NULL, "open", "devenv.exe", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_FOLDERS") {
                cout << "Executing: Opening Folders..." << endl;
                ShellExecuteA(NULL, "open", "explorer.exe", "D:\\", NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_CAMERA") {
                cout << "Executing: Opening Camera..." << endl;
                ShellExecuteA(NULL, "open", "microsoft.windows.camera:", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_CLOCK") {
                cout << "Executing: Launching Clock..." << endl;
                ShellExecuteA(NULL, "open", "ms-clock:", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_PAINT") {
                cout << "Executing: Opening Paint..." << endl;
                ShellExecuteA(NULL, "open", "mspaint.exe", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_SNIPING_TOOL") {
                cout << "Executing: Launching Snipping Tool..." << endl;
                ShellExecuteA(NULL, "open", "SnippingTool.exe", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_YOUTUBE") {
                cout << "Executing: Navigating to Youtube..." << endl;
                ShellExecuteA(NULL, "open", "https://www.youtube.com", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_CODE_BLOCK") {
                cout << "Executing: Launching Code Blocks..." << endl;
                ShellExecuteA(NULL, "open", "C:\\Program Files\\CodeBlocks\\codeblocks.exe", NULL,  NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_VIDEOS") {
                cout << "Executing: Launching Videos..." << endl;
                ShellExecuteA(NULL, "open", "explorer.exe", "C:\\Users\\DELL\\Videos",  NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_MUSIC") {
                cout << "Executing: Launching Music..." << endl;
                ShellExecuteA(NULL, "open", "explorer.exe", "C:\\Users\\DELL\\Music", NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LAUNCH_DOWNLOADS") {
                cout << "Executing: Opening Downloads..." << endl;
                ShellExecuteA(NULL, "open", "explorer.exe", "C:\\Users\\DELL\\Downloads", NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "REFRESH_WINDOW") {
                cout << "Executing: Refreshing the Current Window..." << endl;
                keybd_event(VK_F5, 0,0,0);
                keybd_event(VK_F5, 0, KEYEVENTF_KEYUP, 0);
            }
            else if (command_word == "LAUNCH_TASK_MANAGER") {
                cout << "Executing: Launching Windows Task Manager..." << endl;
                ShellExecuteA(NULL, "open", "taskmgr.exe", NULL, NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "LOCK_COMPUTER") {
                cout << "Executing: Securing Windows Workstation instantly..." << endl;
                LockWorkStation();
            }
            else if (command_word == "CLOSE_ACTIVE_WINDOW") {
                cout << "Executing: Injecting Close command to active foreground window..." << endl;
                HWND active_window = GetForegroundWindow();
                PostMessage(active_window, WM_CLOSE, 0, 0);
            } 
            else if (command_word == "RESTART_PC") {
                cout << "Executing: Injecting Shutdown command to closing the PC..." << endl;
                ShellExecuteA(NULL, "open", "shutdown.exe", "/r /t 0", NULL, SW_SHOWNORMAL);
            }
            else if (command_word == "SHUTDOWN_PC") {
                cout << "Executing: Injecting Shutdown command to closing the PC..." << endl;
                ShellExecuteA(NULL, "open", "shutdown.exe", "/s /t 0", NULL, SW_SHOWNORMAL);
            }
        } 
    } 
    
    cout << "Cleaning up network sockets..." << endl; 
    closesocket(communication_antenna); 
    WSACleanup(); 
    
    cout << "C++ Program Terminated Successfully." << endl; 
    return 0; 
}