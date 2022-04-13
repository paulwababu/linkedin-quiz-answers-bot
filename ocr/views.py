import base64
import linecache
from django.contrib import messages
from django.shortcuts import render
import requests

def homepage(request):
    if request.method == "POST":
        #get also the question category for linked in assessment quizes
        text = request.POST["question"]
        #find matching question
        string1 =  text
        particular_line = ''
        lines = ''
        # opening a text file
        ################################################################################
        file1 = open("/home/tinka/Desktop/linkedin/OCR-django-app/ocr/adobe.md", "r")
        #####################################################################################
        # setting flag and index to 0
        flag = 0
        index = 0
        # Loop through the file line by line
        for line in file1:
            index += 1
            # checking string is present in line or not

            if string1 in line:
                flag = 1
                break
        # checking condition for string found or not
        if flag == 0:
            print('String', string1, 'Not Found')
        else:
            # print('String', string1, 'Found In Line', index)
            particular_line = linecache.getline('/home/tinka/Desktop/linkedin/OCR-django-app/ocr/adobe.md', index)
            print(particular_line)
            print('#################################################################')
            with open("/home/tinka/Desktop/linkedin/OCR-django-app/ocr/adobe.md", 'r') as fp:
                # lines to read
                line_numbers = [index, index + 1, index + 2, index + 3, index + 4, index + 5]
                # To store lines
                lines = []
                for i, line in enumerate(fp):
                    # read line 4 and 7
                    if i in line_numbers:
                        lines.append(line.strip())
                    elif i > index + 5:
                        # don't read after line 7 to save time
                        break
        print(lines)
        # closing text file    
        file1.close()                                 
        # return text to html
        return render(request, "home.html", {'question':particular_line, 'lines':lines})

    return render(request, "home.html")
