﻿# Random Statue Generator

Content generation is an expensive process which usually requires hiring several professionals and coordinating them to converge to a cohesive game. Instead of manually writing different levels, it is possible to design an algorithm capable of generating the same. The challenge is in designing an algorithm capable of creative generation of the various game components. This project attempts to automatically designing novel 3D art structures. Aesthetic measures are used as fitness parameters to quantify the novelty of the generated worlds.

Content generation is a critical & expensive process in game development.Procedural Content Generation (PCG) is a technique for creating content algorithmically.No Man's sky has implemented PCG mathematical equations defining the game entities. Drawback of this system is the generated content is too random.Procedural Content Generation(PCG) problems require both quality and diversity of the generated content.Evolutionary Algorithms have the capability to generate diverse structures. If we look at the large body of research in computational creativity, we can see that value and novelty are vital criteria to evaluate an artifact as creative. The use of EA’s in simulation engines would be able to dynamically create a variety of environments for simulators.

Proposed Solution :

EA Respresentation of our solution is an array with values of vertices[], faces[], RGB, alpha, roughness.
![image](https://user-images.githubusercontent.com/68246158/210088579-d1f7813c-9c56-401b-860f-5c164b43a3ea.png)


A random population is generated and it is being mutated and out of which using tournament selection, two random parents are chosen to which single point crossover is done and a new genaration is created. This is done for n no of generations until we get a well defined figure.

To check if the figure formed is better than others, we came up with a fitness function, the compression factor. So after compressing the figure, the value should be the greatest and that is when we actually know there is an evolution.

