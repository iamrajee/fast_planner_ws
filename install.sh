# if facing issue of  'PCL requires C++14 or above', then change c++11 to c++14 in below files
uav_simulator/map_generator/CMakeLists.txt
uav_simulator/local_sensing/CMakeLists.txt
fast_planner/plan_env/CMakeLists.txt
fast_planner/path_searching/CMakeLists.txt
fast_planner/bspline_opt/CMakeLists.txt
fast_planner/traj_utils/CMakeLists.txt
fast_planner/plan_manage/CMakeLists.txt

sudo apt install libarmadillo-dev
sudo apt install ros-melodic-nlopt
or
sudo apt install ros-noetic-nlopt
