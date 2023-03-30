# Engineering_4_Notebook

&nbsp;

## Table of Contents
### Launchpad Assignments

* [Onshape_Assignment_Template](#Onshape_Assignment_Template)
* [LaunchPad_Countdown](#LaunchPad_Countdown)
* [LaunchPad_Lights](#LaunchPad_Lights)
* [LaunchPad_Button](#LaunchPad_Button)
* [LaunchPad_Servo](#LaunchPad_Servo)
### Crash Avoidance Asssignments
* [Crash_Avoidance1](#Crash_Avoidance1)
* [Crash_Avoidance2](#Crash_Avoidance2)
* [Crash_Avoidance3](#Crash_Avoidance3)
### Landing Area Assignments
* [Landing_Area1](#Landing_Area1)
* [Landing_Area2](#Landing_Area2)
### Morse Code Assignments
* [Morse_Code1](#Morse_Code1)
* [Morse_Code2](#Morse_Code2)
### FEA Team Assignments
* [FEA_Parts](#FEA_Parts)
### Onshape Assignments
* [Ring_and_Spinner](#Ring_and_Spinner)
* [Key_and_Prop](#Key_and_Prop)
* [Assembling_The_Launcher](#Assembling_The_Launcher)
### Pi In the Sky
* [Pi In the Sky Repo](https://github.com/rareval48/Eng4_Pi_in_the_Sky/blob/main/README.md)




&nbsp;

## Onshape_Assignment_Template
Pay no mind to this, im using this as a reference to future onshape assignements
### Assignment Description

### Part Link 

### Part Image

### Reflection

&nbsp;

## LaunchPad_Countdown

### Assignment Description
This assignment is the beginning of learning how to launch a rocket and launching a rocket

### Evidence
<img src="https://user-images.githubusercontent.com/71342195/191979857-57f11e35-6524-4090-b4b2-fb05f40575c9.gif">

### Code
[Countdown code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad(Countdown%201))

### Reflection
This one was really easy as I have done countdowns before and have had experience with. But for new people doing this this would be pretty easy as there is plenty of documentation on how to do for statements.

&nbsp;

## LaunchPad_Lights

### Assignment Description
This assignment is the second assignment where we learn how to launch a rocket.

### Evidence
<img src="https://user-images.githubusercontent.com/71342195/191979306-15a34399-91f9-4f12-94d7-251b8c83952a.gif">

### Wiring
<img src= "https://user-images.githubusercontent.com/71342195/191981469-f6e085e8-9483-4ed4-9cf3-448078246d36.png" width="400px">

### Code
[Lights code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad%20(Countdown%202))

### Reflection
This one was also really easy as I have worked with LEDs and resistors before. For the code I just used the for loop for printing the countdown and the while loop for keeping the green led on. This was pretty easy as I have done this before.

&nbsp;

## LaunchPad_Button

### Assignment Description
This assignment is the third part of the project where we code a button to start the countdown.

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/191984808-e3822249-5278-432b-bba5-dfd23dafd961.gif" width="300px">

### Wiring
<img src="https://user-images.githubusercontent.com/71342195/191770569-94029a39-bfe3-435f-b6ec-cf40fbe1a4ba.png" width="400px">

### Code
[Button code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad%20(Countdown%203))

### Reflection
There was a difficult problem with the code, where even though the button wasnt pressed, the code would run. So I looked at some other code and saw that I had part of my code outside of the indent, so it would start and finish without thinking about the whether or not it got a signal from the button or not. So once I fixed that and the code started working I was able to start on the fourth part of the project.


&nbsp;

## LaunchPad_Servo

### Assignment Description
This assignment is the third part of the project where we code a servo to act like an arm to hold 

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/192791995-8391e24e-0b88-4f2c-b284-f53554bd18bb.gif" width="300px">

### Wiring
<img src="https://user-images.githubusercontent.com/71342195/192788160-dab59f27-1de2-4d1c-9c97-5825dac8361a.png" width="400px">

### Code
[Servo Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad%20(Countdown%204))

### Reflection
This part of the project was really easy as all i needed to do was add code from a previous project to fit the requirements for this project. The only thing wiring wise that I needed to add was a servo with a ground, 3v, and signal.

&nbsp;

## Crash_Avoidance1

### Assignment Description
This assignment is where we code a XYZ coordinate calculator that tells us our altitude.

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/192802773-dcf936b9-adac-4e3b-a669-3b84389d0a41.gif" width="300px">

### Wiring
<img src="https://user-images.githubusercontent.com/71342195/192805739-1c262c40-3af5-43ac-bc5f-15ca95d6db83.png" width="400px">

### Code
[Crash Avoidance Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance%20(1))

### Reflection
This assignment was pretty easy as I got most of the important imformation from Mr. Miller. Make sure the SDA and SDL pins are conected on the same I2C port.


&nbsp;

## Crash_Avoidance2

### Assignment Description
This assignment is where we add a LED to the previous code to show us when the Z coord goes below or equal to one.

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/193294584-e68d327f-a342-4fcc-b3d2-945ed185c573.gif" width="300px">

### Wiring
<img src="https://user-images.githubusercontent.com/71342195/192788160-dab59f27-1de2-4d1c-9c97-5825dac8361a.png" width="400px">

### Code
[Crash Avoidance 2 Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance%20(2))

### Reflection
This part of the project was really easy as all i needed to do was add code from a previous project to fit the requirements for this project. The only thing wiring wise that I needed to add was a servo with a ground, 3v, and signal.

&nbsp;

## Crash_Avoidance3

### Assignment Description
This assignment is where we add a LCD screen to display the XYZ coords of the gyro.

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/194888688-aa3dc980-5807-497f-90ff-92c69761ee77.gif" width="300px">

### Wiring
<img src="https://user-images.githubusercontent.com/71342195/194892308-a924fb89-952d-477f-9e77-214bca31d0b7.png" width="400px">

### Code
[Crash Avoidance 3 Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance%20(3))

### Reflection
Getting the LCD screen to work was problably the hardest theing to do, as the code didnt like the device address foir some reason so I had to go back multiple times to make sure that I actually got the right address. Once I fixed that another slew of problems arrived, including code and wiring problems. But, after I fixed them all the code finally worked.

&nbsp;

## Landing_Area1

### Assignment Description
This assignment is calcualting the area of theree points in a triangle.

### Evidence
There isnt any evidence, you just have to trust me.

### Wiring
No wiring needed

### Code
[Landing Area 1 Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Landing%20Area%20Pt1)

### Reflection
This part of the project was pretty easy as there wasnt much to do except code. I already had the resources to find the code and use it all I had to do was copy and paste code.

&nbsp;

## Landing_Area2

### Assignment Description
This assignment is using a LCD to plot points onto a graph.

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/196706419-cd115f15-ca49-4b58-a1c8-de96ff639ab6.gif" width="300px">

### Wiring
<img src= "https://user-images.githubusercontent.com/71342195/196712731-00a554df-b1c7-4bba-882c-373d0dce3b2d.png" width="400px">

### Code
[Landing Area 2 Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Landing%20Area%20Pt%202)

### Reflection
This part was relativley easy as I just needed to add code for previous projects such as Landing Area 1 and Crash Avoidance 3. I added code from those previous projects and some code that Mr. Miller gave me in the assinment. I also borrowed code from Paul as help for the first part of the project. [Paul's Github](https://github.com/pschake34/Engineering_4_Notebook)

&nbsp;

## Morse_Code1

### Assignment Description
This assignment is about creating and using code to translate letters and numbers to Morse Code.

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/197546952-d9d41208-e9e0-4e00-9585-681d24cdaa32.gif" width="300px">

### Wiring
No Wiring Needed

### Code
[Morse Code 1 Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Morse%20Code%201)

### Reflection
This assignemnt was pretty easy as there wasnt much do besides making sure that the code actually worked. As the resources and the dictionary for the assignment was given to me.

&nbsp;

## Morse_Code2

### Assignment Description
This assignment was about blinking an LED using morse code.

### Evidence
<img src= "https://user-images.githubusercontent.com/71342195/198037631-00e58cbb-3d59-4363-955c-0af9b408f87c.gif" width="300px">

### Wiring
<img src= "https://user-images.githubusercontent.com/71342195/198040996-7da49e87-df45-469c-9ab4-6b2536fea4d6.png" width="400px">

### Code
[Morse Code 2 Code](https://github.com/rareval48/Engineering_4_Notebook/blob/main/raspberry-pi/Morse%20Code%202)

### Reflection
This assignment was reletivaly easy as I just had to use an if/elif statement to tell the led when to blink and when to sleep. Depending on the different dots and dashes it would sleep for longer or blink for longer. There were also different sleep times for spaces and inbetween letters shown as "/". 

&nbsp;

## FEA_Parts

## Github Link
We made a seperate github link for this assignment

https://github.com/rareval48/FEA-Team-Beam-Design

&nbsp;

## Ring_and_Spinner

### Assignment Description

### Part Link
https://cvilleschools.onshape.com/documents/c10a64adb05a97594b5f00ac/w/d896d0d5707f299028cb3778/e/33b134c2eb2db36c090f1224
### Part Image

<img src="https://user-images.githubusercontent.com/71342195/225023152-8a7734e0-3247-4c6e-a747-7bad1439223a.png" width="400px">

### Reflection
This one was the easiest part as there wasnt much to do besides use the given dimensions
&nbsp;

## Key_and_Prop

### Assignent Description

### Part Link
https://cvilleschools.onshape.com/documents/c10a64adb05a97594b5f00ac/w/d896d0d5707f299028cb3778/e/33b134c2eb2db36c090f1224

### Part Image
I do not have a image for the key and prop

### Reflection
I wasnt the one who completed this assignment I just did part A

&nbsp;

## Assembling_the_Launcher

### Assignment Description

### Part Link
https://cvilleschools.onshape.com/documents/c10a64adb05a97594b5f00ac/w/d896d0d5707f299028cb3778/e/33b134c2eb2db36c090f1224###

### Part Image
I do not have an image for the key and prop

### Reflection
I wasnt able to fully assemble this assignment

&nbsp;








