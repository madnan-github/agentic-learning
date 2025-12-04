---
title: Deployment to Jetson Orin
description: Guide on deploying AI-powered robotics applications to NVIDIA Jetson Orin developer kits, including environment setup, cross-compilation, and optimizing for edge deployment.
slug: /module3/chapter3/lesson2-deploy-jetson-orin
sidebar_label: Deploy Jetson Orin
---

# Deployment to Jetson Orin

NVIDIA Jetson Orin developer kits provide powerful, energy-efficient computing at the edge, making them ideal platforms for deploying AI-powered robotics applications. This lesson guides you through the process of setting up a Jetson Orin and deploying your robot control and AI inference pipelines.

## 1. Introduction to Jetson Orin

The Jetson Orin series (e.g., Nano, NX, AGX) offers a significant leap in AI performance compared to previous generations, featuring NVIDIA Ampere architecture GPUs with Tensor Cores, a deep learning accelerator (DLA), and a vision processing accelerator (PVA). This makes it capable of running complex AI models in real-time directly on the robot.

Key features for robotics deployment:
-   **High AI Inference Throughput**: For perception, navigation, and control tasks.
-   **Integrated ISP**: For high-quality camera input.
-   **Rich I/O**: GPIO, I2C, SPI, UART, USB, PCIe, and MIPI CSI/DSI for connecting various sensors and actuators.
-   **NVIDIA JetPack SDK**: A comprehensive software stack that includes CUDA-X libraries, cuDNN, TensorRT, and vision primitives.

## 2. Setting Up Your Jetson Orin

1.  **Flash JetPack SDK**: Use the NVIDIA SDK Manager on a host PC to flash the latest JetPack OS onto your Jetson Orin. This installs Ubuntu, CUDA, cuDNN, TensorRT, and other necessary drivers and libraries.
2.  **Initial Configuration**: Complete the Ubuntu setup, including creating a user, setting up Wi-Fi, and updating packages.
3.  **Install ROS 2**: Follow the standard ROS 2 Humble (or relevant distribution) installation guide for Ubuntu on ARM64. Ensure you install the `ros-humble-desktop` or `ros-humble-ros-base` variants.
4.  **Install Isaac ROS**: Install the necessary Isaac ROS packages for your application. These are typically distributed as Debian packages or can be built from source.
    ```bash
    # Example: Install Isaac ROS packages for Humble
    sudo apt install ros-humble-isaac-ros-common ros-humble-isaac-ros-image-pipeline ...
    ```

## 3. Optimizing AI Models for Edge Deployment

For optimal performance on Jetson Orin, AI models should be optimized:

-   **TensorRT Conversion**: Convert your trained deep learning models (e.g., from PyTorch/TensorFlow to ONNX) into TensorRT engines. TensorRT performs graph optimizations, kernel auto-tuning, and precision calibration (e.g., to FP16 or INT8) to maximize inference speed.
-   **Quantization**: Reduce the precision of model weights and activations (e.g., from FP32 to FP16 or INT8) to further accelerate inference and reduce memory footprint. TensorRT supports various quantization schemes.
-   **Model Pruning and Distillation**: Reduce model complexity by removing redundant connections or training a smaller model to mimic a larger one.

Isaac ROS packages are already optimized to leverage TensorRT, so when you use components like `isaac_ros_detectnet`, they will automatically use TensorRT if available.

## 4. Cross-Compilation and Workspace Setup

When developing on a powerful host PC and deploying to Jetson, you might need to cross-compile your ROS 2 packages. This involves building your code on the host for the ARM64 architecture of the Jetson.

However, often it's simpler to directly build on the Jetson if your development environment (e.g., a Docker container) is consistent.

**On Jetson Workspace Setup:**

1.  **Create a ROS 2 Workspace**: `mkdir -p ~/ros2_ws/src`
2.  **Clone Your Repository**: `cd ~/ros2_ws/src && git clone <your_repo_url>`
3.  **Install Dependencies**: Use `rosdep install --from-paths src --ignore-src -r -y`
4.  **Build Workspace**: `cd ~/ros2_ws && colcon build --symlink-install`
5.  **Source Setup Files**: `source install/setup.bash`

## 5. Running Your Application

Once built, your ROS 2 nodes and AI pipelines can be launched on the Jetson:

-   **Individual Nodes**: `ros2 run <package_name> <executable_name>`
-   **Launch Files**: `ros2 launch <package_name> <launch_file.py>`

### Example: Launching an Isaac ROS Perception Pipeline

Assuming you have an `isaac_ros_object_detection.py` node and an `isaac_ros_detectnet` launch file similar to what was discussed in previous lessons, you would run it:

```bash
# From your ROS 2 workspace root on Jetson
source install/setup.bash
ros2 launch my_robot_perception detectnet_pipeline.launch.py
```

Monitor performance using tools like `tegrastats` (a Jetson-specific utility to monitor GPU, CPU, and memory usage) or `htop`.

## 6. Remote Access and Debugging

-   **SSH**: Access your Jetson remotely via SSH for command-line operations.
-   **VS Code Remote Development**: Use Visual Studio Code\'s Remote Development extension to develop and debug directly on the Jetson from your host PC.
-   **ROS 2 Logging**: Use `ros2 log` and `rqt_console` to inspect logs from your running nodes.
-   **RViz (Remote)**: If your Jetson has a desktop environment, you can run RViz directly. Alternatively, forward X over SSH or use `rqt_image_view` for image streams.

Effective deployment to Jetson Orin combines careful environment setup, model optimization, and robust debugging strategies to unlock the full potential of AI-powered robotics at the edge.
