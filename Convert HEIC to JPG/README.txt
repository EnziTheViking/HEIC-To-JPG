--------------------------------------------------------------
Git Hub:
https://github.com/carsales/pyheif

Script from:
https://www.py4u.net/discuss/183992

More info:
https://pypi.org/project/pyheif-pillow-opener/

Run Linux in window WSL
https://docs.microsoft.com/en-us/windows/wsl/install-win10

--------------------------------------------------------------


You have to use Linux or Mac, there is a workaround using WSL on a windows computer allowing
you to use a Linux environment in windows. I don't know why pyheif won't work on windows but this is the best way for Window users at this time, without installing other programs. 


---------
STEP ONE
---------
Do this guide --> https://docs.microsoft.com/en-us/windows/wsl/install-win10

	Or follow here 

		1. Open PowerShell in Admin Mode
		
		2. Enable the Windows Subsystem for Linux
		_________________________________________
		dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
		

		3. Enable Virtual Machine feature
		__________________________________
		dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
		

		4. Download the Linux kernel update package
		https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

		---------------
		Reboot Computer
		---------------

		5. Install your Linux distribution of choice
		Windows store, I'm using Ubuntu(20.04LTS)
		

--------------------------------------------------------------	

---------
STEP TWO
---------

	1. Make sure you have a The script.py in the folder that contains all the HEIC files
	
	2. Once you have your login info for your linux enviroment 
	
	3. We will need to install the nessisary libraries
		- 1. Check what python package we have installed (in linux) Needs to be 3.6.x to 3.8.x
			python3 --version
			
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