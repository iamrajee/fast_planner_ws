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
vehicle = Quadrotor()
vehicle.set_options({'safety_distance': 0.1})
vehicle.set_initial_conditions([-4., -4., 0., 0., 0.])
vehicle.set_terminal_conditions([4., 4.])

# create environment
environment = Environment(room={'shape': Square(10.)})
environment.add_obstacle(Obstacle({'position': [-0.6, -5.4]},
                                  shape=Rectangle(width=0.2, height=12.)))

# create a point-to-point problem
problem = Point2point(vehicle, environment, {'horizon_time': 5})
problem.init()

# create simulator
simulator = Simulator(problem)
problem.plot('scene')
vehicle.plot('input', knots=True, label=['Thrust force (N/kg)',
                                         'Pitch rate (rad/s)'])

# run it!
simulator.run()
