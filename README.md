# ElectroShower-Detection

## Inspiration
As engineers, it is pretty apparent that we are busy a lot. Sometimes, this comes at the expense of not showering. Thus, we felt it would be a good idea to create an image processing and detection system that could, theoretically, detect if a person has showered or not.

## What it does
Our project essentially detects irregularities in patterns of a person's showering habits. It does this through the the backend process of python where the functions of colors and shades and the ability to change it on a camera is established. Then Arduino comes in where it combines the hardware portion of the breadboard to the software and either lights up green if you have entered a shower or red if you haven't that day. 

## How we built it
Our project utilizes a Python program that incorporates OpenCV and HSV to perform image processing and facial detection. Furthermore, there is a use of Arduino and two LEDs. First, the two LEDs, one green and one red, were wired to the breadboard and served as the digital output of the system. Next, an Arduino program was built and incorporated into a separate Python program. Once the necessary libraries were imported, they were integrated into the system to automatically detect a face. Then, many HSV values were gathered and ultimately were used to match HSV values of a typical clean face or a color of a grease stain. As for the output, in the first phase, the webcam detects the face and turns on the green LED. However, if a face is not detected, the red LED is turned on. Then, in the second phase, the system remains green until a person who hasn't showered has been detected and it should involve the HSV values. Overall, the project's goal is to determine whether an individual has showered or not by analyzing physical characteristics on their face.

## Challenges we ran into
We had two major challenges during the creation of the project. First, the camera was slightly flawed because it was only able to detect RGB values. In order to fix this, we would need a multispectral camera such as a hyperspectral camera that can detect multiple of different colors at different wavelengths. However, this would cost a lot of money and we had to work with the limited resources that we had. The other challenge was that we can't realistically rely on only image processing. Deep learning would be better but without much deep learning experience in a limited time setting, working on that from scratch would have been impossible. Lastly, odors cannot be detected so we had to rely solely on physical characteristics.

## Accomplishments that we're proud of
As a whole, our team is proud of accomplishing a project of this caliber as it accommodates the content from ENGR 102, ECEN 248, and ECEN 214 as we used python, Arduino, and a breadboard. We are extremely proud of the coding portion of our project as this was a hardware project that incorporated object-oriented programming, which wasn't our strong point. Finally, through trial and error, we are proud of the perseverance and will power our team showed to keep going even if we had an impossible hurdle to go over.

## What we learned
Our team learned a lot about the different applications of computer vision and its impact in the real world. We've found out more about the potential it has. Furthermore, this was the first time that two of us learned about HSV so it was a great experience.

## What's next for ElectroShower Detection
In the future, we would like to expand our project to use deep learning to detect grease, oily skin, and other factors on a person's face that could be indicative of whether an individual has showered or not. This would be a lot bigger project but it would make us more familiar with how machine learning, specifically deep learning, works. Furthermore, the incorporation of a multispectral camera would be able to extract various values and contain multiple layers. In addition, military personnel tend to need hyperspectral cameras for autonomous vehicles and an RGB camera with deep learning would be dangerous if used. Thus, to apply our project to a bigger scale, using a multispectral camera would help in the grander scheme of things.
