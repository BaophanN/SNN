# Autonomous Driving with Spiking Neural Networks 


1. Spiking Neuron Layer

$$
U[t] = H[t - 1] + X[t],
$$

$$
S[t] = \Theta (U[t] - u_{th}),
$$

$$
H[t] = U_{\text{reset}} S[t] + (\beta U[t]) (1 - S[t]),
$$

where
$$
X[t]: \text{ Input to the neuron at timestep } t
$$

$$
U[t]: \text{ Membrane potential of the neuron}
$$

$$
\Theta(x): \text{ Heaviside step function } = 
\begin{cases} 
1, & \text{if } x \geq 0 \\ 
0, & \text{otherwise} 
\end{cases}
$$

$$
S[t]: \text{ Tensor of emitted spikes}
$$

$$
H[t]: \text{ Temporal output}
$$
Right here, the temporal nature of SNN should be fully utilized so as to get the true potential of it. If single frame, NO USE. 

2. Encoder: Spking Token Mixer with Sequence Repetition: 12 layers of spiking CNN pretrained on imagenet 
![image](https://github.com/user-attachments/assets/f3b35922-af16-4c95-bb99-b9eb0fdaf487)
T: number of frames repeated due to squential repetition, L: number of frames in a continous camera recording. 

**Sequential Alignment for decoder**: sequential input data is passed step by step to SNN
**Sequential Repetition for encoder**: the same frame is repeated. 

3. Decoder: Sequential Alignment with Streaming Feature Maps: first 3 layers of MS-ResNet18 + upsample layers (factor of 2) + skip connection 
![image](https://github.com/user-attachments/assets/8452138d-d877-44bc-808a-1294b2dcf327)

4. Prediction: Fusing parallel spike streams: Use two LIF neuron layers.
to predict the future features 
Layer 1 takes the present and prior output BEV feature maps from the encoder of the perception model as inputs.
![image](https://github.com/user-attachments/assets/741c4edd-7116-48d3-8d0f-700626f5ee85)
Layer 2 accounts for the uncertainty distribution of future BEV predictions (4x Spiking MS-Resnet)


Dual pathway

![image](https://github.com/user-attachments/assets/d0fb7a7a-5f90-4afb-a87e-dea0691b3161)

5. Planning: Spiking Temporal for Trajectory Refinement 
Use bicycle model to generate a diverse set of potential trajectories.
Choose the trajectory that minimize the cost function:
![image](https://github.com/user-attachments/assets/8f9289bc-11e5-48c1-9628-62d90f1cfd8e)
Then optimized with Spiking Gated Recurrent Unit.
![image](https://github.com/user-attachments/assets/7712c525-c230-4fd6-8a06-c6633cef5b2f)


