# imports
# import snntorch as snn
# from snntorch import spikeplot as splt
# from snntorch import spikegen

import torch
# import torch.nn as nn

import numpy as np
import matplotlib.pyplot as plt
def leaky_integrate_neuron(U, time_step=1e-3,I=0,R=5e7,C=1e-10):
    tau = R*C
    U = U + (time_step / tau) * (-U + I*R) 
    return U 

# Add spike 
def leaky_integrate_and_fire(mem, cur=0,threshold=1, time_step=1e-3,R=5.1, C=5e-3):
    tau_mem = R*C
    spk = (mem > threshold) 
    mem = mem + (time_step/tau_mem)*(-mem + cur*R) 
    return mem, spk 

# Add reset mechanism 
def leaky_integrate_and_fire(mem, cur=0,threshold=1, time_step=1e-3,R=5.1,C=5e-3):
    tau_mem = R*C
    spk = (mem > threshold) 
    mem = mem + (time_step/tau_mem)*(-mem + cur*R) - spk*threshold
    return mem, spk 

def plot_cur_mem_spk(cur, mem, spk, thr_line=False, vline=False, title=False, ylim_max2=1.25):
  # Generate Plots
  fig, ax = plt.subplots(3, figsize=(8,6), sharex=True, 
                        gridspec_kw = {'height_ratios': [1, 1, 0.4]})

  # Plot input current
  ax[0].plot(cur, c="tab:orange")
  ax[0].set_ylim([0, 0.4])
  ax[0].set_xlim([0, 200])
  ax[0].set_ylabel("Input Current ($I_{in}$)")
  if title:
    ax[0].set_title(title)

  # Plot membrane potential
  ax[1].plot(mem)
  ax[1].set_ylim([0, ylim_max2]) 
  ax[1].set_ylabel("Membrane Potential ($U_{mem}$)")
  if thr_line:
    ax[1].axhline(y=thr_line, alpha=0.25, linestyle="dashed", c="black", linewidth=2)
  plt.xlabel("Time step")

  # Plot output spike using spikeplot
  splt.raster(spk, ax[2], s=400, c="black", marker="|")
  if vline:
    ax[2].axvline(x=vline, ymin=0, ymax=6.75, alpha = 0.15, linestyle="dashed", c="black", linewidth=2, zorder=0, clip_on=False)
  plt.ylabel("Output spikes")
  plt.yticks([]) 

  plt.show()

if __name__ == "__main__":
    num_steps = 200 
    cur_in = torch.cat((torch.zeros(10), torch.ones(190)*0.2),0)
    mem = torch.zeros(1)
    mem_rec = [] 
    spk_rec = [] 

    # neuron simulation 
    for step in range(num_steps): 
        mem, spk = leaky_integrate_and_fire(mem, cur_in[step]) 
        mem_rec.append(mem) 
        spk_rec.append(spk) 
    # convert lists to tensor 
    mem_rec = torch.stack(mem_rec)
    spk_rec = torch.stack(spk_rec) 
    plot_cur_mem_spk(cur_in, mem_rec, spk_rec, thr_line=1, vline=109, ylim_max2=1.3,
                 title="LIF Neuron Model With Uncontrolled Spiking")
