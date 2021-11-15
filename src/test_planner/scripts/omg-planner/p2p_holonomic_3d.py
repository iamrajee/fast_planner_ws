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

from omgtools import *

# create vehicle
vehicle = Holonomic3D(Plate(Rectangle(0.5, 1.), height=0.1))

vehicle.set_initial_conditions([-2., -2., -2])
vehicle.set_terminal_conditions([2., 2., -2])

# create environment
environment = Environment(room={'shape': Cube(5.)})
environment.add_obstacle(Obstacle(
    {'position': [0., 0., -1.5]}, shape=Cuboid(width=0.5, depth=4., height=2.)))
trajectories = {'velocity': {'time': [4.], 'values': [[0.0, 0.0, 1.]]}}
environment.add_obstacle(Obstacle(
    {'position': [1., 1., -2.25]}, shape=RegularPrisma(0.25, 0.25, 6),
    simulation={'trajectories': trajectories}))

# create a point-to-point problem
problem = Point2point(vehicle, environment, freeT=False)
problem.set_options({'hard_term_con': True, 'horizon_time': 12})
problem.init()

# create simulator
simulator = Simulator(problem)
problem.plot('scene', view=[45, -45])  # elevation and azimuth of cam
vehicle.plot('state', knots=True, labels=['x (m)', 'y (m)', 'z (m)'])
vehicle.plot('input', knots=True, labels=['v_x (m/s)', 'v_y (m/s)', 'v_z (m/s)'])

# run it!
simulator.run()
