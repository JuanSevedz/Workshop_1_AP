# Workshop 3
This is a program to define a catalog of vehicles, with the next requeriments:

Each vehicle has at least engine, chasis (A or B), model, gas consumption, and year.
Depending on the vehicle type, you should define additional propeties.

There are different vehicle vehicle types: car, truck, yacht, motorcycle.

Each engine has type, potency, weight.

To calculate the vehicle gas consumption you could créate a method based on:
1.1	* engine.potency + 0.2 * engine.weight – (0.3 if chassis == A or 0.5 if chasssis == B).
