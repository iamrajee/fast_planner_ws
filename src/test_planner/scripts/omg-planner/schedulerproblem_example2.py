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


# This code shows an expansion of a normal multiframeproblem (schedulerproblem_example1.py),
# in which a large environment is split over several frames.
# In a multiframeproblem we only consider one room/frame at a time.
# Using a schedulerproblem, you can combine frames, i.e. a trajectory is computed through multiple frames at a
# time. The advantage is that e.g. moving obstacles around the corner can immediately be taken into account.
# Note that when putting n_frames=1 you get exactly the same idea/behaviour as in the
# p2p_multiframeproblem.py example.

from omgtools import *

# create vehicle
vehicle = Holonomic(shapes = Circle(radius=0.5), options={'syslimit': 'norm_2', 'stop_tol': 1.e-2},
                    bounds={'vmax': 2, 'vmin':-2, 'amax':4, 'amin':-4})
veh_size = vehicle.shapes[0].radius

# create environment
start = [5,0]
goal = [40,20]
vehicle.set_initial_conditions(start)
vehicle.set_terminal_conditions(goal)

room1 = {'shape': Rectangle(width=60, height=30), 'position': [30, 10], 'draw':True}

environment = Environment(room=room1)

# create stationary obstacles

rectangle = Rectangle(width=2., height=2)
rectangle1 = Rectangle(width=0.2, height=0.2)

obstacle1 = Obstacle({'position': [10,0]}, shape=rectangle)
trajectories = {'velocity': {'time': [0.], 'values': [[0, -0.]]}}
obstacle2 = Obstacle({'position': [22.5,12.5]}, shape=rectangle, simulation={'trajectories': trajectories})

# Warning: if you use fill room, then also fill the empty rooms with []
environment.fill_room(room1, [obstacle1, obstacle2])

# make global planner
# [25,25] = number of cells in vertical and horizonal direction
globalplanner = AStarPlanner(environment, [25,25], start, goal, options={'veh_size': veh_size})

# make problem
# 'n_frames': number of frames to combine when searching for a trajectory
# 'check_moving_obs_ts': check in steps of ts seconds if a moving obstacle is inside the frame
# 'frame_type': 'corridor': creates corridors
	# 'scale_up_fine': tries to scale up the frame in small steps, leading to the largest possible corridor
	# 'l_shape': cuts off corridors, to obtain L-shapes, and minimize the influence of moving obstacles
# 'frame_type': 'shift': creates frames of fixed size, around the vehicle
	# 'frame_size': size of the shifted frame
options = {'frame_type': 'corridor', 'scale_up_fine': True, 'n_frames': 2, 'l_shape':True}
schedulerproblem = SchedulerProblem(vehicle, environment, globalplanner, options=options)

# simulate the problem
simulator = Simulator(schedulerproblem)

# define what you want to plot
schedulerproblem.plot('scene')
vehicle.plot('input', knots=True, prediction=True, labels=['v_x (m/s)', 'v_y (m/s)'])
vehicle.plot('dinput', knots=True, prediction=True, labels=['a_x (m/s^2)', 'a_y (m/s^2)'])

# run it!
simulator.run()

schedulerproblem.plot_movie('scene', number_of_frames=100, repeat=False)
schedulerproblem.save_movie('scene', format='gif', name='schedulergif', number_of_frames=100, movie_time=10, axis=False)
# schedulerproblem.save_movie('scene', number_of_frames=50, name='scheduler', axis=False)
