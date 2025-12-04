---
title: Gazebo Simulation Setup
description: Learn how to set up and use Gazebo for robot simulation, including world creation, robot spawning, and basic interaction.
slug: /module2/chapter1/lesson1-gazebo-basics
sidebar_label: Gazebo Basics
---

# Gazebo Simulation Setup

Gazebo is a powerful 3D robot simulator often used with ROS 2. It allows you to accurately simulate complex robot systems in various environments, crucial for development and testing without physical hardware.

## 1. Introduction to Gazebo

Gazebo provides:
-   **Physics Engine**: Accurate simulation of rigid body dynamics.
-   **High-Quality Graphics**: Renders realistic environments and robot models.
-   **Sensor Simulation**: Simulates various sensors like cameras, lidar, and IMUs.
-   **Plugin Interface**: Extend functionality with custom plugins, often used for ROS 2 integration.

## 2. Gazebo Concepts

-   **Worlds**: Describe the environment (terrain, buildings, objects, lighting). Defined in `.sdf` (Simulation Description Format) files.
-   **Models**: Represent robots or objects within the world. Can be simple shapes or complex articulated robots defined using URDF (Universal Robot Description Format) or SDF.
-   **Sensors**: Simulated sensors attached to models (e.g., cameras, IMUs, lidars).
-   **Plugins**: Extend Gazebo's functionality, often used to connect Gazebo simulations with ROS 2.

## 3. Launching Gazebo

Gazebo can be launched using the `gazebo` command or integrated with ROS 2 launch files.

To launch an empty Gazebo world:
```bash
gazebo
```

To launch a specific world file (e.g., `empty.world`):
```bash
gazebo worlds/empty.world
```

## 4. Spawning Robots in Gazebo

Robots are typically spawned into a Gazebo world using ROS 2 launch files or command-line tools. This involves:
1.  Loading the robot's URDF/SDF model.
2.  Spawning the model into the Gazebo environment.
3.  Launching controllers for the robot's joints.
4.  Launching `robot_state_publisher` to publish the robot's TF tree.

### Example: Spawning a URDF Robot

A common way to spawn a URDF robot model in Gazebo is using the `spawn_entity.py` script from the `ros_gz_sim` package.

First, ensure you have `ros_gz_sim` installed:
```bash
sudo apt install ros-humble-ros-gz-sim
```

Then, you can use a ROS 2 launch file similar to this (example `launch/spawn_humanoid.launch.py`):

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_name = 'my_robot_description' # Replace with your package name
    pkg_share_dir = get_package_share_directory(pkg_name)
    urdf_file = os.path.join(pkg_share_dir, 'urdf', 'humanoid_robot.urdf') # Your URDF file

    # Start Gazebo sim
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': '-r empty.sdf'}.items()
    )

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(urdf_file).read()}],
    )

    # Spawn robot
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=['-topic', '/robot_description',
                   '-name', 'humanoid_robot',
                   '-x', '0',
                   '-y', '0',
                   '-z', '0.5'],
    )

    return LaunchDescription([
        gazebo_launch,
        robot_state_publisher_node,
        spawn_entity,
    ])
```

This launch file first starts Gazebo, then launches the `robot_state_publisher` to parse your URDF and publish the robot's joint states and transforms, and finally uses `ros_gz_sim/create` to spawn your robot model into the simulation.

## 5. Basic Interaction

Once your robot is in Gazebo, you can:
-   **Move the camera**: Use mouse and keyboard controls to navigate the 3D view.
-   **Apply forces/torques**: Interact with the robot through Gazebo's GUI or via ROS 2 topics (e.g., `/model/humanoid_robot/cmd_vel` for velocity commands).
-   **Inspect data**: Use `rqt_plot` or `ros2 topic echo` to visualize sensor data or joint states published by the simulated robot.
