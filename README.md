# Alter-Image-Dimensions

1. **Prerequisite to run this python program (also contain GUI):**<br />
   **a.** OS Mac, Windows or Linux (The demonstration shown below is on MacOS BigSur version 11.3). <br />
   **b.** Python version 3 and to run this program demonstration I am using **PyCharm**, you can use any IDE or run it through your OS **command_line_tool**.<br />
   **c.** **Pillow:** The Python Imaging Library adds image processing capabilities to your Python interpreter. <br />
   **d.** **tkinter:** Python offers multiple options for developing GUI and tkinter is the most commonly used method (importing modules, creating main window and add widgets to it).

   **Note:** The directory or file structure is used acrroding to the MacOS, you can change it according to your system within the source code.
   
2. This is how you can check you python version:<br />
   a. For python version 2 you can type *"python --version"* in your terminal.<br />
   b. For python version 3 you can type *"python3 --version"* in your terminal.<br />

   ![Screenshot 2021-05-06 at 5 45 28 PM](https://user-images.githubusercontent.com/46700867/117296582-d9f36f80-ae92-11eb-90e0-63bc30cc47f9.png)


3. Now go to the directory where you have saved the **Alter_Image.py** python file and the type this command *"python3 Alter_Image.py"* in your terminal and hit enter.<br />

   ![Screenshot 2021-05-06 at 5 57 22 PM](https://user-images.githubusercontent.com/46700867/117298015-83873080-ae94-11eb-9dc2-9d561d192420.png)
   

4. Now, you can see that a window (Graphical User Interface) is open with window title **Altering Image Dimension (Devashish Choudhary)** having two buttons **Open File** and **Alter Image** as shown below:

   ![Screenshot 2021-05-06 at 7 51 45 PM](https://user-images.githubusercontent.com/46700867/117314540-7e31e200-aea4-11eb-88db-a9431719c05a.png)


5. Then click on the **Open File** button, you will observe that the dialog box will appear to select the input image which we have to alter as shown in the below:

   ![Screenshot 2021-05-06 at 8 41 50 PM](https://user-images.githubusercontent.com/46700867/117322298-82153280-aeab-11eb-8dca-43396289f1f6.png)
   
   **Note:** The initial directory of the dialog box which is being used to select the input image is set to *"/Users/isshu/Desktop"*


6. **The smaple input image is shown below:**
   
   ![Input_Image](https://user-images.githubusercontent.com/46700867/117328593-6745bc80-aeb1-11eb-9629-06671a6b7e64.jpg)
   

7. After that you can observe the image path which you have choose will appear on the window in as shown below in **red highlighted** field:

   ![Screenshot 2021-05-06 at 11 00 02 PM](https://user-images.githubusercontent.com/46700867/117341408-b09d0880-aebf-11eb-8667-0829649d2343.png)


8. Then click on the **Alter Image** button to alter the image according to the scenario and all the required alterations of input image are stroed with in the same directory in which the input image is stored, as mentioned in the following steps:

   a. After you click on the **Alter Image** button you will observe the path final altered image on the window in as shown below in **red highlighted** field:
   
   ![Screenshot 2021-05-06 at 11 17 28 PM](https://user-images.githubusercontent.com/46700867/117343263-bdbaf700-aec1-11eb-8b23-a94a882a63e4.png)

   b. Then open the directory in which your final altered image as mentioned on the window and you will observed the all 5 alteration (4 intermediate alteration + final altered image) are present in that directory, as shown belown:
   
   ![Screenshot 2021-05-06 at 11 24 49 PM](https://user-images.githubusercontent.com/46700867/117343784-446fd400-aec2-11eb-9ace-7207ec221110.png)

   Here, <br />
   (I)   Input image (original image) named as *"Input_Image.jpg"*. <br />
   (II)  Intermediate image alterations are named as *"cropped_image_1.jpg"*, *"cropped_image_2.jpg"*, *"cropped_image_3.jpg"*, and *"cropped_image_4.jpg"* and in each alteration the demension of the image is equally reduce by 50% (become half) from every sides.<br />
   (III) Final image (result image) is named as *"Final_Image-Result"* and it is getting by resizing the *"cropped_image_4.jpg"* in the same size as the original image.
   

9. Comparing the **Original Image** and the **Final Image** as shown below:

   **Original Image**
   
   ![Screenshot 2021-05-06 at 11 48 08 PM](https://user-images.githubusercontent.com/46700867/117347054-3328c680-aec6-11eb-90c1-02267431c07b.png)
   
   **Final Image** (Observed that the **Red Highlighted** field in **Original Image** is shown here):
   
   ![Screenshot 2021-05-06 at 11 57 00 PM](https://user-images.githubusercontent.com/46700867/117347452-c4983880-aec6-11eb-9d57-53b4aa0d9467.png)

10. Console Output, provides the dimension of each image in every alteration as well as the newly calculated dimension for next alteration:
   
    ![Screenshot 2021-05-07 at 12 02 28 AM](https://user-images.githubusercontent.com/46700867/117348171-86e7df80-aec7-11eb-8f25-afd86290d0e8.png)
