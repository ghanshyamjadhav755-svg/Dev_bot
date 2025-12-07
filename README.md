## to launch gazebo with custom world
ros2 launch my_bot launch_sim.launch.py world:=/home/jd/dev_ws/src/my_bot/worlds/maze.world 

##localization
ros2 launch nav2_bringup localization_launch.py map:=/home/jd/dev_ws/turtlebot_world.yaml use_sim_time:=true

##Navigation
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true






## launch rviz2
ros2 run rviz2 -d src/my_bot/config/view_bot.rviz

## robot state publisher
ros2 launch my_bot rs.launch.py

## mapping with slam_toolbox
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_bot/config/mapper_params_online_async.yaml use_sim_time:=true



