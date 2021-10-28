##================================ yolact ================================##
# git clone https://github.com/Eruvae/yolact_ros_msgs.git
# git clone --recurse-submodules https://github.com/Eruvae/yolact_ros.git
# pip install torchvision
# pip install pycocotools
# =========================================================================##
roslaunch yolact_ros yolact_ros.launch image_topic:=/stereo_camera/left/image_raw display_visualization:=true model_path:=/home/rajendra/swarm_ws/src/yolact_ros/scripts/yolact/weights/yolact_resnet50_54_800000.pth
