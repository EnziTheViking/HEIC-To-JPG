
# Links


>### Git Hub:
>https://github.com/carsales/pyheif

>### Update: (Original Link to get the script does not work, including the script bellow)
>Script "WAS" from: "py4u.net/discuss/183992"
```python
import whatimage
import pyheif
from PIL import Image
import os

def decodeImage(bytesIo, index):
    with open(bytesIo, 'rb') as f:
        data = f.read()
        fmt = whatimage.identify_image(data)
    if fmt in ['heic', 'avif']:
        i = pyheif.read_heif(data)
        pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
        pi.save("new" + str(index) + ".jpg", format="jpeg")

# For my use I had my python file inside the same folder as the heic files
source = "./"

for index,file in enumerate(os.listdir(source)):
    decodeImage(file, index)

```
>### More info:
>https://pypi.org/project/pyheif-pillow-opener/


>### Run Linux in window WSL
>https://docs.microsoft.com/en-us/windows/wsl/install-win10
>


# Description
> You have to use Linux or Mac, there is a workaround using WSL on a windows computer allowing
you to use a Linux environment in windows. I don't know why pyheif won't work on windows but this is the best way for Windows users at this time, without installing other programs. 


# STEP ONE

Follow this guide --> https://docs.microsoft.com/en-us/windows/wsl/install-win10
>
    Or follow here
    
		1. Open PowerShell as Administrator
		
		2. Enable the Windows Subsystem for Linux 
		
       		dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
		
		3. Enable Virtual Machine feature
		
       		dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
		
		4. Download the Linux kernel update package
       		https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
          
            5. Reboot Computer

		6. Install a Linux distribution of your choice in the Windows Store, I'm using Ubuntu(20.04LTS)
    
# STEP TWO

>
	1. Make sure you have a The script.py in the folder that contains all the HEIC files
	
	2. Once you have your login info for your Linux environment 
	
	3. We will need to install the necessary libraries
		- 1. Check what python package we have installed (in Linux) Needs to be 3.6.x to 3.8.x
			python3 --version
		- If step 2 doesn't work, try A & B
			A. "sudo apt-get update"
			B. "sudo apt-get install python3.6"
		- 2. apt install python3-pip
		
		- 3. pip install whatimage
		
		- 4. pip install Image
		
		- 5. pip install pyheif-pillow-opener
		
	4. Go ahead and go to the folder dir that contains the script and photos. 
	
		- 1. cd /mnt/c/filename
				
		- 2. List files
			ls
			
		- 3. Run script 
			python3 script.py


#NOTE
> This is just an all in one place tutorial, I am not the original writer of the python script.

