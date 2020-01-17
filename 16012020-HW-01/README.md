### Question
Design a circuit (Boolean Expression) w/ logic gate that can convert a decimal number to binary

### Visual Representation of the question

Let's assume there is a numpad of the following sort

![numpad](numpad.png "Numpad")

when you press one of those numbers, you should get the binary represantation of that number as output. For that we need to figure out how to ouput the represantation.


The binary represantation of the numbers 0-9 follow:

![Decimal to Binary Represantation of 0-9](dectobin.png "Dec to Bin")

The table shows that we need at least a 4-bit space to write 0 through 9

So, we can put 4 LEDs side-by-side representing each bit

![](4led.png "LED Representation")

Let's assume the LED is yellow when turned off and red when it is turned on

When 6 is pressed the state of the LEDs will be:

![](6rep.png "6")

So the LED turns on when we send a **1** and turns off when given a signal **0**

### Inputs and Outputs
Each of the number is represented by a switch that has two states - on(1)/off(0) marked A-J

![](switches.png "Switch")
The output is a set of 4 LEDs representing each bit of the binary number where a turned on LED means 1 and a turned off LED means 0.

![](output.png "Output")
Inititally, all of them are turned off.

### Table
We can generate a truth table consisting each case where one(and only one) switch is pressed.

![](truthtable.png "Truth Table")

### Equations
To represent the state (0/1) of each LED, we can use a boolean equation

Using SOP Method:

$W(A,B,...,J)$ = $\sum{_m}(8,9)$
$X(A,B,...,J)$ = $\sum{_m}(4,5,6,7)$
$Y(A,B,...,J)$ = $\sum{_m}(2,3,6,7)$
$Z(A,B,...,J)$ = $\sum{_m}(1,3,5,7,9)$

After simplifying,

$W(A,B,...,J)$ = $\bar A\bar B\bar C\bar D\bar E\bar F\bar G\bar H.(I \oplus J)$
$X(A,B,...,J)$ = $\bar A\bar B\bar C\bar D\bar I\bar J .[ \bar G\bar H(E \oplus F) + \bar E\bar F(G \oplus H) ]$
$Y(A,B,...,J)$ = $\bar A\bar B\bar E\bar F\bar I\bar J .[ \bar G\bar H(C \oplus D) + \bar C\bar D(G \oplus H) ]$
$Z(A,B,...,J)$ = $\bar A\bar C\bar E\bar G\bar I .[ \bar F\bar H\bar J(B \oplus D) + \bar B\bar D\bar J(F \oplus H) + \bar B\bar D\bar F\bar H J ]$

### The circuit
We get the following circuit after implementing the equations

![Circuit](16012020-01-final.png "Final Circuit")

which works as following

![Circuit GIF](circuit.gif "Circuit GIF")

If we interpret a turned on LED as **1** and a turned off LED as **0**, the set of LEDs give the correct binary representation of the pressed switch/number