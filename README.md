# Word Counter
This program relizes a simple word counter using Python. The program counts predefined words and returns a graph containing the mean and absolute number the word was found in one or multiple PDF files. It was implemented for application in a seminar paper by Nico Schurig from the [TU Bergakademie Freiberg](https://tu-freiberg.de). The seminar paper focuses on robotic applications for surgery.
Although this program was made for a very specific usecase it also can be used for other scenarios.
## How To Use
- At first generate a new .txt file (this will contain the words you want to search for).
- After that, write the words into the .txt file. <br>
  Here you can see an example .txt file. This contains the names of different systems used for robot-assisted surgery:
  ![example txt file](/example_txt_file.png)
  
- Create a new directory for your .pdf files and add them.
- Change the following two lines of code, to work with your data:
  ```python
    #Path to .txt file with predefined words
    wordlist_file = 'words.txt'
  ```
  ```python
    #Directory path, containing the PDF files
    pdf_folder = 'PDF_Files/example'
  ```
- **That´s It! You can now run the code to count your words.**
