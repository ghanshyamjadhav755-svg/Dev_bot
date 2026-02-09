## to launch gazebo with custom world
ros2 launch my_bot launch_sim.launch.py world:=/home/jd/dev_ws/src/my_bot/worlds/new.world 

##localization
ros2 launch my_bot localization_launch.py map:=/home/jd/dev_ws/new_map.yaml use_sim_time:=true

##Navigation
ros2 launch my_bot navigation_launch.py use_sim_time:=true



## mapping with slam_toolbox
ros2 launch my_bot online_async_launch.py



## launch rviz2
ros2 run rviz2 -d src/my_bot/config/view_bot.rviz

## robot state publisher
ros2 launch my_bot rs.launch.py




