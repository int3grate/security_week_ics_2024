## Introduction

This repository contains resources and exercises for a talk titled "*Fortifying Industrial Control Systems: A Deep Dive into Evaluating Cryptographic Implementations*" given at the Security Week ICS Conference in 2024.

## Exercises

The following folders contain exercises with incomplete code you need to finish in order to obtain the solution.  Solutions will be posted a week after the conference, along with details on how to setup a Docker container to host them yourself.

- **cpa_attack** : contains traces and text-in data collected from a real device performing AES encryption.  Finish the script to recover the key.

- **compression_oracle** / **padding_oracle** : contains the code for an example of a vulnerable function and the start of an attack script you can complete to try the attack yourself.

## Resources

- **length_extension_attack** : contains example code used to exploit length extension attack.

- **WinDBG_Cheat_Sheet.pdf** : my own cheat sheet for WinDBG.

- **aes_visualization** : encrypt pixel data using AES ECB mode.  Demonstrates the issues with using ECB mode.

 - **ics_presentation_2024.pdf** : copy of presentation given at event.
