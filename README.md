# PBHSim
Proposed hypothetical primordial black hole around 400-800 astronomical units (AU) out which helps to dictate movements within the Kuiper Belt. 

PBH Orbital Perturbation Simulator
A full 3D N-body simulation exploring the long-term gravitational influence of a Primordial Black Hole (PBH) or Planet-Nine–like object on the outer Solar System.
This script models the Sun, a PBH (~5 Earth masses), and a swarm of Kuiper Belt Objects (KBOs), integrating their trajectories over 1 million years using the REBOUND N-body integrator.
🌌 Overview
This project simulates how a distant, massive, inclined object (PBH / Planet Nine candidate) alters the orbital structure of the Kuiper Belt over long timescales.
The script performs:
N-body integration with the Sun, PBH, and 200 massless KBOs
Randomized initial orbital elements for realistic Kuiper Belt distributions
Top-down (XY plane) plots comparing the system at
t = 0
t = 1,000,000 years
2D animated evolution using matplotlib
3D visualization + animation using Mayavi
Full storage of positions for all bodies across the integration time
🧪 Physics & Initial Conditions
Units:
Distance: AU
Time: years
Mass: Solar masses
Bodies Included
Body	Mass	Description
Sun	1.0 Msun	Central star
PBH	1.5×10⁻⁵ Msun (~5 Earth masses)	Highly inclined, mildly eccentric hypothetical Planet-Nine-like perturber
200 KBOs	0	Massless test particles with low eccentricity & inclination
PBH orbital elements
a = 500 AU
e = 0.2
inclination = 20°
Ω = 150°
ω = 100°
true anomaly = 0°
📦 Dependencies
Install via:
pip install rebound numpy matplotlib mayavi
Required libraries
REBOUND — N-body gravitational simulation
NumPy — numerical arrays
matplotlib — 2D visualization + animation
Mayavi — 3D visualization + animated orbital evolution
▶️ How to Run
From the project root:
python3 src/pbh_simulation.py
The script will:
Print integration progress for each timestep
Produce initial + final static orbital plots
Generate a 2D animated evolution (FuncAnimation)
Open an interactive 3D Mayavi visualization
Optionally animate the 3D system over the full time span
To save a GIF, uncomment:
# ani.save('pbh_perturb.gif')
📊 Outputs
1. Static Plots
Initial configuration
Final configuration after 1 million years
Displays:
Sun (yellow)
PBH (black)
KBO swarm (blue)
2. 2D Animation
A top-down XY-plane animation of the orbital evolution across all 1000 timesteps.
3. 3D Visualization
Mayavi windows rendering:
Sun (yellow)
PBH (black)
KBO cloud (blue)
Includes a frame-by-frame 3D animation loop.
🧠 What This Simulation Demonstrates
How a massive, distant planet/PBH reshapes the Kuiper Belt
Orbital clustering and excitation
Precession and long-term evolution
Potential signatures consistent with Planet Nine hypotheses
Dynamical stability over Myr-scale integration
🗂 Project Structure
pbh-dynamics-simulator/
│
├── src/
│   └── pbh_simulation.py    # Main simulation script
│
├── README.md
├── requirements.txt
└── .gitignore
📘 Notes
Mayavi requires Qt or VTK support; installation may vary by platform.
The integration step count (1000 steps over 1 Myr) is optimized for animation;
increase resolution for scientific accuracy.
✨ Future Extensions
Add giant planets (Jupiter → Neptune)
Add KBO size/family distributions
Implement orbital clustering detection
Explore PBH mass range (0.1–10 Earth masses)
Compute Tisserand parameters, inclinations, perihelion angles
Include long-term stability metrics
