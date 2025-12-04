---
title: Building ROS 2 Python Packages
description: Learn how to create and structure ROS 2 packages using Python, including `setup.py` and `package.xml` configurations.
slug: /module1/chapter1/lesson2-ros2-packages
sidebar_label: Python Packages
---

# Building ROS 2 Python Packages

In the previous lesson, you learned about the core concepts of ROS 2. Now, it's time to put that knowledge into practice by creating your own ROS 2 packages using Python. A ROS 2 package is the fundamental unit for organizing software in ROS 2. It contains nodes, launch files, configuration files, and other resources.

## 1. ROS 2 Package Structure

A typical ROS 2 Python package has the following basic structure:

```text
my_robot_package/
├── package.xml
├── setup.py
├── resource/
│   └── my_robot_package
└── my_robot_package/
    ├── __init__.py
    └── my_node.py
```

-   `package.xml`: Provides metadata about the package, such as its name, version, description, maintainers, license, and dependencies.
-   `setup.py`: A Python setuptools script that defines how your Python code is built and installed.
-   `resource/my_robot_package`: An empty file used by `ament_python` to locate your package's Python modules.
-   `my_robot_package/`: This is your Python module directory, containing your actual Python source code (`.py` files).

## 2. Creating a New ROS 2 Python Package

You can create a new ROS 2 package using the `ros2 pkg create` command. For a Python package, you would specify the build type as `ament_python`:

```bash
ros2 pkg create --build-type ament_python my_robot_package
```

This command will create the `my_robot_package` directory with a basic `package.xml` and `setup.py`.

## 3. `package.xml` Explained

The `package.xml` file is crucial for ROS 2. Here's a breakdown of key tags:

```xml
<package format="3">
  <name>my_robot_package</name>
  <version>0.0.0</version>
  <description>TODO: Package description</description>
  <maintainer email="user@todo.todo">user</maintainer>
  <license>TODO: License declaration</license>

  <depend>rclpy</depend>
  <depend>std_msgs</depend>

  <test_depend>python3-pytest</test_depend>
  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
```

-   `<name>`, `<version>`, `<description>`, `<maintainer>`, `<license>`: Standard package metadata.
-   `<depend>rclpy</depend>`: Specifies a build and run dependency on `rclpy`, the Python client library for ROS 2.
-   `<depend>std_msgs</depend>`: Dependency on standard ROS 2 message types.
-   `<test_depend>python3-pytest</test_depend>`: A dependency for running tests with pytest.
-   `<export><build_type>ament_python</build_type></export>`: Declares that this is an `ament_python` package.

## 4. `setup.py` Explained

The `setup.py` file uses Python's `setuptools` to define how your package is built, installed, and what executables it provides. A typical `setup.py` for a ROS 2 Python package looks like this:

```python
from setuptools import find_packages, setup

package_name = 'my_robot_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_robot_package.my_node:main',
        ],
    },
)
```

-   `packages=find_packages(exclude=['test'])`: Automatically discovers Python packages in your source tree.
-   `data_files`: Specifies non-Python files (like `package.xml` and the `resource` marker file) that need to be installed.
-   `install_requires`: Lists Python package dependencies.
-   `entry_points`: This is where you define executable scripts (nodes) from your Python modules. Here, `my_node` will be an executable command that runs the `main` function in `my_node.py` located within the `my_robot_package` Python module.

## 5. Writing a Simple ROS 2 Python Node

Inside your `my_robot_package/my_node.py` (or similar) file, you would write your node's logic. Here's a basic structure for a node:

```python
import rclpy
from rclpy.node import Node

class MyMinimalNode(Node):
    def __init__(self):
        super().__init__('my_minimal_node')
        self.get_logger().info('My minimal node has been started!')

def main(args=None):
    rclpy.init(args=args)
    minimal_node = MyMinimalNode()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## 6. Building and Running Your Package

1.  **Build the package** (from your workspace root, where `my_robot_package` is a subdirectory):

    ```bash
    colcon build --packages-select my_robot_package
    ```

2.  **Source your workspace**:

    ```bash
    source install/setup.bash
    ```

3.  **Run your node**:

    ```bash
    ros2 run my_robot_package my_node
    ```

## Next Steps

In the next lesson, we will create a concrete example of a ROS 2 Python publisher and subscriber node to demonstrate inter-node communication.
