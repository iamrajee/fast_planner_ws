#roslaunch sort_track sort.launch

rosrun flocking sort_custom.py _/display:=True _/img_topic:=/stereo_camera/left/image_raw _/min_hits:=1 _/max_age:=500 _/iou_threshold:=0.05 _/bbox_topic:=darknet_ros/bounding_boxes_nms/
#rosrun flocking sort_custom.py _/display:=True _/img_topic:=/stereo_camera/left/image_raw _/min_hits:=1 _/max_age:=500 _/iou_threshold:=0.05
#rosrun flocking sort_custom.py _/display:=True _/img_topic:=/stereo_camera/left/image_raw _/min_hits:=1 _/max_age:=200 _/iou_threshold:=0.2
#rosrun flocking ros-sort.py _/display:=True _/img_topic:=/stereo_camera/left/image_raw _/min_hits:=1 _/max_age:=200 _/iou_threshold:=0.2
#rosrun flocking ros-sort.py _/display:=True _/img_topic:=/usb_cam/image_raw _/min_hits:=1 _/max_age:=200 _/iou_threshold:=0.2
