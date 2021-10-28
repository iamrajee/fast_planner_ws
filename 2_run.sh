#!/bin/bash
#Terminal2

#roslaunch darknet_ros my_yolov3.launch config_file:=yolov3 image:=/stereo_camera/left/image_raw
#roslaunch darknet_ros my_yolov3.launch config_file:=yolov3-tiny image:=/stereo_camera/left/image_raw

#roslaunch darknet_ros my_yolov3.launch config_file:=yolo-drone image:=/stereo_camera/left/image_raw


#roslaunch darknet_ros my_yolov3.launch config_file:=yolov4-p6 image:=/stereo_camera/left/image_raw
#roslaunch darknet_ros my_yolov3.launch config_file:=yolov4-csp image:=/stereo_camera/left/image_raw
roslaunch darknet_ros my_yolov3.launch config_file:=yolov4 image:=/stereo_camera/left/image_raw

#roslaunch darknet_ros yolo_v4.launch image:=/stereo_camera/left/image_raw
#roslaunch darknet_ros yolo_v4.launch image:=/usb_cam/image_raw

roslaunch darknet_ros my_yolov3.launch config_file:=yolov3-spp image:=/stereo_camera/left/image_raw
# roslaunch darknet_ros my_yolov3.launch config_file:=yolov3-spp image:=/image_raw_top_left
# roslaunch darknet_ros my_yolov3.launch config_file:=yolov3-spp image:=/usb_cam/image_raw
# roslaunch darknet_ros my_yolov3.launch config_file:=yolov3-tiny image:=/usb_cam/image_raw
# roslaunch darknet_ros yolo_v3.launch image:=/usb_cam/image_raw

# ROS_NAMESPACE=/stereo/camera rosrun stereo_image_proc stereo_image_proc _approximate_sync:=True
# rosrun image_view stereo_view stereo:=/stereo/camera image:=image_raw _approximate_sync:=True
