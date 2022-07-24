# ColorFinderHexcode
This programe tells the top 10 color present with their hex code in given image with a preview of that picture.

# Files 
It contain three files and one folder 
- main.py - main file to run application 
- v2.py - implementation of gui with functionality 
- pngToBase64.py - contain code to convert image to base64 code and also contain base64 code for two images used in application 
- assests - folder contain all the images used (for logo icon2.png is used)

# Librabry used 
1. tkinter
2. PIL aka pillow
3. colorthief
4. os
5. base64
6. io


# How to use application 
- To convert .py to exe 
  - Step 1: put all three .py files in same directory 
  - Step 2: Make sure you have python installed with all librabry mentioned above 
  - Step 3: Use following command to get a exe verion of programm 
            ```
            pyinstaller --onefile -w main.py 
            ```
  - Step 4: You will find exe in same direcotry in folder named dist 
- exe file not inculded here due to its big size 25mb+

