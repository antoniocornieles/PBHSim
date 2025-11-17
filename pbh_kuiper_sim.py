import rebound
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mayavi import mlab

# Setup simulation
sim = rebound.Simulation()
sim.units = ('AU', 'yr', 'Msun')  # Units: AU, years, solar masses

# Add Sun
sim.add(m=1.0)  # Index 0: Sun

# Add PBH (Planet Nine-like: ~5 Earth masses = 1.5e-5 solar, at 500 AU, e=0.2 for perturbation)
sim.add(m=1.5e-5, a=500, e=0.2, inc=20*np.pi/180, omega=100*np.pi/180, Omega=150*np.pi/180, f=0)  # Index 1: PBH

# Add ~50 Kuiper Belt test particles (mass=0, random orbits ~30-50 AU, low ecc/inc for stability)
N_kbo = 200
for i in range(N_kbo):
    a = np.random.uniform(30, 50)  # Semi-major axis
    e = np.random.uniform(0, 0.1)  # Low ecc
    inc = np.random.uniform(0, 10) * np.pi/180  # Degrees to rad
    sim.add(m=0, a=a, e=e, inc=inc, omega=np.random.uniform(0, 360)*np.pi/180,
            Omega=np.random.uniform(0, 360)*np.pi/180, f=np.random.uniform(0, 360)*np.pi/180)

# Integrate over time (1e6 years, 1000 steps for animation)
times = np.linspace(0, 1e6, 1000)
positions = np.zeros((len(times), sim.N, 3))  # Store x,y,z for all particles

for i, t in enumerate(times):
    print(f"Step {i}/{len(times)}")
    sim.integrate(t)
    for j, p in enumerate(sim.particles):
        positions[i, j] = [p.x, p.y, p.z]

# Static plots: Initial and final top-down (xy plane)
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
for ax, idx, title in zip(axs, [0, -1], ['Initial', 'Final (1e6 yrs)']):
    ax.scatter(positions[idx, 0, 0], positions[idx, 0, 1], c='yellow', s=100, label='Sun')  # Sun
    ax.scatter(positions[idx, 1, 0], positions[idx, 1, 1], c='black', s=50, label='PBH')  # PBH
    ax.scatter(positions[idx, 2:, 0], positions[idx, 2:, 1], c='blue', s=5, label='KBOs')  # KBOs
    ax.set_xlim(-600, 600)
    ax.set_ylim(-600, 600)
    ax.set_title(title)
    ax.set_xlabel('AU')
    ax.set_ylabel('AU')
    ax.legend()
plt.show()

# Animation: Top-down view evolution
fig, ax = plt.subplots()
ax.set_xlim(-600, 600)
ax.set_ylim(-600, 600)
sun = ax.scatter([], [], c='yellow', s=100)
pbh = ax.scatter([], [], c='black', s=50)
kbos = ax.scatter([], [], c='blue', s=5)

def animate(i):
    sun.set_offsets([positions[i, 0, :2]])
    pbh.set_offsets([positions[i, 1, :2]])
    kbos.set_offsets(positions[i, 2:, :2])
    return sun, pbh, kbos

ani = FuncAnimation(fig, animate, frames=len(times), interval=50, blit=True)
#plt.show()  # Or ani.save('pbh_perturb.gif') for GIF
#ani.save('pbh_perturb.gif')

# 3D scatter plot
fig = mlab.figure(size=(800, 600))
mlab.points3d(positions[0, 0, 0], positions[0, 0, 1], positions[0, 0, 2], color=(1, 1, 0), scale_factor=50, label='Sun')  # Sun
mlab.points3d(positions[0, 1, 0], positions[0, 1, 1], positions[0, 1, 2], color=(0, 0, 0), scale_factor=50, label='PBH')  # PBH
mlab.points3d(positions[0, 2:, 0], positions[0, 2:, 1], positions[0, 2:, 2], color=(0, 0, 1), scale_factor=10, label='KBOs')  # KBOs

# Animate (simplified, one frame for now)
@mlab.animate(delay=50)
def anim():
    for i in range(len(times)):
        mlab.clf()  # Clear previous frame
        mlab.points3d(positions[i, 0, 0], positions[i, 0, 1], positions[i, 0, 2], color=(1, 1, 0), scale_factor=50, label='Sun')
        mlab.points3d(positions[i, 1, 0], positions[i, 1, 1], positions[i, 1, 2], color=(0, 0, 0), scale_factor=50, label='PBH')
        mlab.points3d(positions[i, 2:, 0], positions[i, 2:, 1], positions[i, 2:, 2], color=(0, 0, 1), scale_factor=10, label='KBOs')
        yield

anim = anim()
mlab.show()
