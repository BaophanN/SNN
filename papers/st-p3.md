#ST-P3
And end to end AD pipe line that uses camera only. 
The SAD is built upon this code base. Use ResNet-18 at all feature extraction stage. Dual pathway modeling. LSS view transformation and the same cost function. Even the experiments are all the same. 
SAD just replaces all the module from ST-P3 with spiking components. 
Hmm, energy consumption is computed theoretically based on MAC and AC.
There is a github repo to measure the number of MAC and AC. 
