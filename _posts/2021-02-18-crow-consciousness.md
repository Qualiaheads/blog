---
title: "A neural correlate of sensory consciousness in a corvid bird"
date: 2021-02-18T19:00:00+01:00
tags:
  - access consciousness
  - experimental
---

Paper review of: [A neural correlate of sensory consciousness in a corvid bird](https://science.sciencemag.org/content/369/6511/1626) (doi currently broken). Do crows have sensory / access consciousness?

## Observations

Boils down a test for access consciousness to testing the memory representation of a stimulus in the bird - makes access consciousness seem quite weak

* Memory of stimulus intensity - not access consciousness
* Memory of whether or not the stimulus was seen - access consciousness

Test protocol makes sense to decouple crow's response from input stimulus

* Correct response depends on secondary cue presented after a delay from the stimulus
* Crow can't just associate action with seeing the stimulus and vice versa
  * Needs to "access" its memory of whether it saw the stimulus, when it receives the secondary cue after the delay period

Figure 4 b) wasn't entirely convincing. We did some modelling [here](https://nbviewer.jupyter.org/github/consciousness-discussions/blog/blob/master/notebooks/Noisy%20neuron%20access%20consciousness.ipynb).

* Wouldn't a similar result be expected from a single, noisy neuron encoding the stimulus intensity?
  * Noise would cause the neuron to become more predictive of the outcome closer to the decision time
  * Noise would also cause the neuron to become less predictive of the stimulus intensity over time - the representation would get corrupted
* While this could seemingly work for a single neuron, unclear if it would for a whole population
* Would need to perform more modelling to definitively rule out a simpler explanation than a binary encoding of whether the stimulus was seen i.e. access consciousness

## Conclusions

* The findings seemed a bit less "grandiose" than we expected overall
  * Could be simplified to: crows form and access an abstract binary representation of whether a stimulus was seen or not, rather than a representation of stimulus intensity
* Access consciousness seems quite "weak" - need to investigate more, particularly with regards to global workspace theory
* It would have been super interesting (but maybe not possible) to as the crow to make two different choices based on the stimulus visibility.
  * If the two decisions were consistent, the crow's memory is of whether it saw the stimulus. If not, the memory is of the stimulus intensity.
  * Making the first choice might anchor the crow's second choice, then there wouldn't be any interesting results.
