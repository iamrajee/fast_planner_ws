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
import numpy as np

# create fleet
N = 3
vehicles = [Quadrotor(0.2) for l in range(N)]
fleet = Fleet(vehicles)
for quad in fleet.vehicles:
    quad.set_options({'safety_distance': 0.1, 'safety_weight': 1.})
configuration = RegularPolyhedron(0.4, N, orientation=np.pi/2).vertices.T
init_positions = [-4., -4.] + configuration
terminal_positions = [4., 4.] + configuration

fleet.set_configuration(configuration.tolist())
fleet.set_initial_conditions([np.r_[pos, np.zeros(3)] for pos in init_positions.tolist()])
fleet.set_terminal_conditions(terminal_positions.tolist())

# create environment
environment = Environment(room={'shape': Square(9.3)})
environment.add_obstacle(Obstacle({'position': [0., 3.7]},
                                  shape=Rectangle(width=0.2, height=3.)))
environment.add_obstacle(Obstacle({'position': [0., -5.4]},
                                  shape=Rectangle(width=0.2, height=10.)))
trajectory = {'velocity': {'time': [0.8], 'values': [[-5., 0.]]}}
environment.add_obstacle(
    Obstacle({'position': [6., 0.8]}, UFO(1.5, 0.6), {'trajectories': trajectory}))

# create a formation point-to-point problem
options = {'horizon_time': 5., 'rho': 0.04}
problem = FormationPoint2point(fleet, environment, options=options)
problem.init()

# create simulator
simulator = Simulator(problem)
problem.plot('scene')
problem.plot('residuals')
fleet.plot('input', knots=True, labels=['Thrust force (N/kg)',
                                        'Pitch rate (rad/s)'])

# run it!
simulator.run()
