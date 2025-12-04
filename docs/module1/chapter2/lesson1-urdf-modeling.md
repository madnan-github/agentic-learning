---
title: Humanoid URDF Modeling
description: Learn how to model humanoid robots using the Unified Robot Description Format (URDF) in ROS 2.
slug: /module1/chapter2/lesson1-urdf-modeling
sidebar_label: URDF Modeling
---

# Humanoid URDF Modeling

The Unified Robot Description Format (URDF) is an XML format used in ROS 2 to describe all elements of a robot. It allows you to specify the robot's kinematics (links and joints), visual properties, collision properties, and inertial properties. For humanoid robots, URDF is essential for defining the complex articulated structure of the robot.

In this lesson, you will learn the basics of URDF, how to define links and joints, and how to assemble them to create a simple humanoid robot model.

## 1. URDF Basics: Links and Joints

At its core, URDF describes a robot as a tree-like structure of `links` connected by `joints`.

-   **Links**: Represent the rigid bodies of the robot (e.g., torso, upper arm, forearm, hand). They have associated geometric, visual, collision, and inertial properties.
-   **Joints**: Represent the connections between links. They define the type of motion allowed between two links (e.g., revolute, prismatic, fixed) and their limits.

### 1.1. The `<link>` Element

A `<link>` element defines a rigid body. Key properties include:

-   **Visual**: Describes how the link should look (e.g., geometry, material, color).
-   **Collision**: Defines the geometry used for collision detection.
-   **Inertial**: Specifies mass, center of mass, and inertia tensor, crucial for physics simulations.

**Example Link Definition (Simplified):**

```xml
<link name="base_link">
  <visual>
    <geometry>
      <box size="0.2 0.4 0.1"/>
    </geometry>
    <material name="white"/>
  </visual>
</link>
```

### 1.2. The `<joint>` Element

A `<joint>` element connects two links: a `parent` link and a `child` link. Key properties include:

-   **Name**: Unique identifier for the joint.
-   **Type**: Defines the joint's degree of freedom (e.g., `revolute`, `continuous`, `prismatic`, `fixed`).
-   **Origin**: Specifies the transform from the parent link's origin to the joint's origin.
-   **Axis**: For revolute and prismatic joints, defines the axis of rotation or translation.
-   **Limit**: For revolute and prismatic joints, defines the lower and upper bounds of motion.

**Example Joint Definition (Simplified):**

```xml
<joint name="base_to_torso" type="fixed">
  <parent link="base_link"/>
  <child link="torso_link"/>
  <origin xyz="0 0 0.2" rpy="0 0 0"/>
</joint>
```

## 2. Assembling a Simple Humanoid Model

Building a humanoid robot in URDF involves connecting many links and joints in a hierarchical structure. A typical humanoid might have:

-   A `base_link` or `pelvis_link` as the root.
-   A `torso_link` connected to the base.
-   Arms, each with `shoulder`, `upper_arm`, `forearm`, and `hand` links, connected by various revolute joints.
-   Legs, each with `hip`, `upper_leg`, `lower_leg`, and `foot` links, also connected by revolute joints.
-   A `head_link` connected to the torso via a neck joint.

**Considerations for Humanoid Models:**

-   **Degrees of Freedom (DoF)**: Humanoids have many DoF, requiring careful joint placement and type selection.
-   **Symmetry**: Many humanoid robots are designed with bilateral symmetry, which can simplify the URDF by allowing reuse of link and joint structures with appropriate transformations.
-   **Coordinate Frames**: Consistent use of coordinate frames is critical. ROS typically uses a Z-up, X-forward, Y-left convention.
-   **Mass Properties**: Accurate inertial properties are essential for realistic simulation and control.

## 3. Visualizing URDF Models

Once you have created a URDF file, you can visualize it in ROS 2 using tools like `RViz`.

To view a URDF in RViz:

1.  **Launch a `robot_state_publisher`**: This node reads your URDF and publishes the robot's transformations to the TF tree.

    ```bash
    ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(cat your_robot.urdf)"
    ```

2.  **Launch `RViz`**:

    ```bash
    rviz2
    ```

3.  In RViz, add a `RobotModel` display and ensure the `robot_description` parameter is set correctly (e.g., to the content of your URDF).

## 4. Next Steps

In the next lesson, we will create a complete URDF model for a simple humanoid robot, which you can then visualize and use in simulations.
