# Spike Driven Transformer 
Benchmark on ImageNet, task image classification. Not really special apart from using the spiking neuron LIF. 
Spike Driven Self Attention (SDSA) is a form of linear attention, contains only mask and sparse additions. 
Key changes compare to Vanilla Self Attention: 
1. Hadamard product replace matrix multiplication
2. Matrix column-wise summation replace softmax and scale

![image](https://github.com/user-attachments/assets/cb709731-f7d1-4ae0-8333-f1c90132956b)
The form of SDSA: 
![image](https://github.com/user-attachments/assets/3497c298-2042-4d6a-a416-c591b68cd7c8)
For more details on each vector of the Q, K, V tensor: 
![image](https://github.com/user-attachments/assets/c30b5a49-5e63-4b26-bb4a-dc13a0362e95)

In comparison, the complexity of VSA vs SDSA - $2N^2D$ vs $0.02ND$ multiply-and-accumulate
![image](https://github.com/user-attachments/assets/1230f3af-e2b8-4059-823f-0259ab594bda)

So, what matters here is the ability to encode signal of SNN, which makes matrix multiplication becomes addition. Dense signal from tensor needed by traditional ANNs replaced by sparse signal from spiking neuron.



