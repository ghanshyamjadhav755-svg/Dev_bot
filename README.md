## to launch gazebo with custom world
ros2 launch my_bot launch_sim.launch.py world:=/home/jd/dev_ws/src/my_bot/worlds/maze.world 

## launch rviz2
ros2 run rviz2 -d src/my_bot/config/view_bot.rviz

## robot state publisher
ros2 launch my_bot rs.launch.py

## mapping with slam_toolbox
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_bot/config/mapper_params_online_async.yaml use_sim_time:=true

