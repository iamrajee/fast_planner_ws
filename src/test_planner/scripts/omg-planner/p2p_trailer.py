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

assert_ma57()

# create vehicle
vehicle = Dubins(shapes=Circle(0.2), bounds={'vmax': 0.8, 'wmax': np.pi/3., 'wmin': -np.pi/3.})
vehicle.define_knots(knot_intervals=9)  # adapt amount of knot intervals
vehicle.set_initial_conditions([0., 0., 0.])  # input orientation in rad
vehicle.set_terminal_conditions([3.4, 3., 0.])

# create trailer
trailer = Trailer(lead_veh=vehicle,  shapes=Rectangle(0.2, 0.2), l_hitch = 0.6,
                  bounds={'tmax': np.pi/4., 'tmin': -np.pi/4.})  # limit angle between vehicle and trailer
# Note: the knot intervals of lead_veh and trailer should be the same
trailer.define_knots(knot_intervals=9)  # adapt amount of knot intervals
trailer.set_initial_conditions(0.)  # input orientation in rad
trailer.set_terminal_conditions(0.)  # this depends on the application e.g. driving vs parking

# create environment
environment = Environment(room={'shape': Square(5.), 'position': [1.5, 1.5]})

# create a point-to-point problem
problem = Point2point(trailer, environment, freeT=True)  # pass trailer to problem
# todo: isn't there are a cleaner way?
problem.father.add(vehicle)  # add vehicle to optifather, such that it knows the trailer variables
problem.vehicles.append(vehicle)
# todo: isn't there are a cleaner way?
vehicle.to_simulate = False
# extra solver settings which may improve performance
problem.set_options({'solver_options':
    {'ipopt': {'ipopt.hessian_approximation': 'limited-memory',
               'ipopt.linear_solver': 'ma57'}}})
problem.init()

# problem.set_options({'hard_term_con': True, 'horizon_time': 12})
# vehicle.problem = problem  # to plot error

# create simulator
simulator = Simulator(problem)
problem.plot('scene')
trailer.plot('input', knots=True, prediction=True, labels=['v (m/s)', 'ddelta (rad/s)'])
trailer.plot('state', knots=True, labels=['x_tr (m)', 'y_tr (m)', 'theta_tr (rad)', 'x_veh (m)', 'y_veh (m)', 'theta_veh (rad)'])

# run it!
simulator.run()
