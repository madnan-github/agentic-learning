---
title: ROS 2 Core Concepts - The Robotic Nervous System
description: An introduction to the fundamental concepts of ROS 2, including nodes, topics, services, actions, and the ROS 2 graph.
slug: /module1/chapter1/lesson1-ros2-basics
sidebar_label: ROS 2 Basics
---

# ROS 2 Core Concepts: The Robotic Nervous System

Welcome to the world of the Robotic Operating System 2 (ROS 2)! ROS 2 is a flexible framework for writing robot software. It's not an operating system in the traditional sense, but rather a set of software libraries and tools that help you build robot applications across a wide range of robot platforms.

In this lesson, you will learn about the fundamental building blocks of ROS 2 that enable robots to perceive, process, and act upon their environment.

## 1. What is ROS 2?

ROS 2 is designed for the modern robotics landscape, addressing challenges such as multi-robot systems, real-time control, and embedded platforms. It provides a standardized communication infrastructure and a rich ecosystem of tools and libraries.

### Why ROS 2?

-   **Distributed System**: Easily communicate between different processes, which can be on the same machine or across a network.
-   **Modularity**: Build complex robot systems by combining smaller, independent components.
-   **Hardware Abstraction**: Interact with various robot hardware through a consistent API.
-   **Tooling**: A powerful set of tools for debugging, visualization, and data logging.

## 2. The ROS 2 Graph

The ROS 2 graph is a network of interconnected **nodes** that communicate with each other. Understanding this graph is key to comprehending how ROS 2 applications work.

### 2.1. Nodes

-   **Definition**: A node is an executable process that performs a specific computation. In a robotic system, you might have nodes for camera drivers, motor controllers, localization algorithms, or path planning.
-   **Characteristics**: Nodes are designed to be modular and reusable. They encapsulate functionality and interact with other nodes through various communication mechanisms.

### 2.2. Topics (Publisher/Subscriber)

-   **Definition**: Topics are the primary means of asynchronous, many-to-many data streaming in ROS 2.
-   **How it works**: A node can **publish** data (messages) to a topic, and any number of other nodes can **subscribe** to that topic to receive the data.
-   **Analogy**: Think of a radio station (publisher) broadcasting music (messages) on a specific frequency (topic). Anyone with a radio (subscriber) tuned to that frequency can listen.
-   **Example**: A camera driver node publishes image data on `/camera/image_raw` topic. A vision processing node subscribes to this topic to receive and analyze the images.

### 2.3. Services (Client/Server)

-   **Definition**: Services provide synchronous, request-response communication between nodes. They are used for operations that involve a clear request and a single, definite response.
-   **How it works**: A node acts as a **service server**, providing a specific functionality. Another node acts as a **service client**, sending a request to the server and waiting for a response.
-   **Analogy**: Like making a phone call to request a specific piece of information and waiting for the answer.
-   **Example**: A robot arm control node might offer a service to `move_to_position`. A planning node acts as a client to request the arm to move to a target position and waits for confirmation.

### 2.4. Actions (Client/Server with Feedback)

-   **Definition**: Actions are similar to services but are designed for long-running tasks that provide periodic feedback and can be preempted.
-   **How it works**: An **action client** sends a **goal** to an **action server**. The server executes the goal, sending **feedback** periodically, and eventually returns a **result**. The client can also send a **cancel** request.
-   **Analogy**: Like ordering a pizza delivery (goal), getting updates on its status (feedback), and eventually receiving the pizza (result).
-   **Example**: A navigation node might offer an action to `navigate_to_pose`. A client sends a goal to reach a specific location, receives continuous updates on the robot's progress (feedback), and eventually gets a success/failure result.

## 3. Communication Middleware

ROS 2 uses a **Data Distribution Service (DDS)** as its communication middleware. DDS is a decentralized, data-centric, and real-time publish-subscribe framework. It handles message serialization, transport, and discovery, allowing nodes to communicate reliably and efficiently.

## 4. Message Types

Messages are the data structures used for communication in ROS 2. They are defined using `.msg` files, which specify the data fields and their types (e.g., `std_msgs/String`, `geometry_msgs/Twist`, `sensor_msgs/Image`). ROS 2 automatically generates code for these message types in various programming languages.

## 5. Next Steps

In the next lesson, you will learn how to build your first ROS 2 packages using Python and create simple nodes that communicate via topics.
