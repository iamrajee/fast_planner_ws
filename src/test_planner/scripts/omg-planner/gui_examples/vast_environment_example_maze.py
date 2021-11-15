# This file is part of OMG-tools.
#
# OMG-tools -- Optimal Motion Generation-tools
# Copyright (C) 2016 Ruben Van Parys & Tim Mercy, KU Leuven.
# All rights reserved.
#
# OMG-tools is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA


# This example is very similar to p2p_multiframeproblem.py, and uses the same principles
# The difference is that in the current example, a GUI is used to assist the user in building up
# the desired environment. For an explanation about how to use the GUI, see below.

from omgtools import *

# create vehicle
vehicle = Holonomic(shapes = Circle(radius=0.75), options={'syslimit': 'norm_2'},
                    bounds={'vmax': 1.2, 'vmin':-1.2, 'amax':8, 'amin':-8})
veh_size = vehicle.shapes[0].radius

# create environment with the help of a GUI

# Note: to run this example just click Load in the GUI and select vast_environment_example2.pickle

try:
  import tkinter as tk
except ImportError:
  import Tkinter as tk
root = tk.Tk()
# the number of desired cells in horizontal and vertical direction are passed as an option
# together with the width and height of the environment, this determines the cell size
gui = EnvironmentGUI(parent=root, width=16, height=16, position=[0,0], options={'n_cells': [20,20]})
root.mainloop()  # run the GUI
environment = gui.get_environment()  # get the environment from the GUI

# get start and goal from GUI
# include vehicle size to shift clicks that were too close to the border
clicked = gui.get_clicked_positions(margin=veh_size)
vehicle.set_initial_conditions(clicked[0])
vehicle.set_terminal_conditions(clicked[1])
start, goal = clicked[0], clicked[1]

# make global planner
# the amount of cells are extracted from the GUI and were either passed by the user to the GUI, or kept at default values
# include vehicle size to take this into account when computing the global path
globalplanner = AStarPlanner(environment, gui.n_cells, start, goal, options={'veh_size': veh_size})

# make schedulerproblem
# 'n_frames': number of frames to combine when searching for a trajectory
# 'check_moving_obs_ts': check in steps of ts seconds if a moving obstacle is inside the frame
# 'frame_type': 'corridor': creates corridors
	# 'scale_up_fine': tries to scale up the frame in small steps, leading to the largest possible corridor
	# 'l_shape': cuts off corridors, to obtain L-shapes, and minimize the influence of moving obstacles
# 'frame_type': 'shift': creates frames of fixed size, around the vehicle
	# 'frame_size': size of the shifted frame
options={'freeT': True, 'horizon_time': 10, 'no_term_con_der': False,
         'n_frames': 2, 'frame_type': 'corridor', 'scale_up_fine': True, 'l_shape':True, 'check_moving_obs_ts': 0.1}
# options = {'n_frames': 2, 'frame_type': 'shift', 'frame_size': 9, 'check_moving_obs_ts': 0.1}

# Note: When 'corridor' is selected and your vehicle size is larger than the cell size,
# shifting frames sometimes causes problems
schedulerproblem=SchedulerProblem(vehicle, environment, globalplanner, options=options)

# Note: using linear solver ma57 is optional, normally it reduces the solving time
schedulerproblem.set_options({'solver_options':
    {'ipopt': {'ipopt.linear_solver': 'ma57',
			   'ipopt.tol': 1e-5,
               'ipopt.warm_start_bound_push': 1e-6,
               'ipopt.warm_start_mult_bound_push': 1e-6,
               'ipopt.warm_start_mult_bound_push': 1e-6,
               'ipopt.mu_init': 1e-5,
               # 'ipopt.hessian_approximation': 'limited-memory',
               'ipopt.max_iter': 20000}}})#,}}})

simulator = Simulator(schedulerproblem)
schedulerproblem.plot('scene')
vehicle.plot('input', knots=True, prediction=True, labels=['v_x (m/s)', 'v_y (m/s)'])
vehicle.plot('dinput', knots=True, prediction=True, labels=['a_x (m/s^2)', 'a_y (m/s^2)'])

# run it!
simulator.run()
schedulerproblem.plot_movie('scene', number_of_frames=100, repeat=False)
schedulerproblem.save_movie('scene', format='gif', name='example2_corridor', number_of_frames=300, movie_time=30, axis=False)
# schedulerproblem.save_movie('scene', format='tikz', name='example2_corridor', number_of_frames=100, movie_time=10, axis=False)
