---
title: Quickstart Guide for Physical AI & Humanoid Robotics Book
description: A quickstart guide for setting up the development environment, running Docusaurus, and executing code examples.
slug: /specs/physical-ai-book-layout/quickstart
---

# Quickstart Guide

This guide provides a quick overview of how to get started with the "Physical AI & Humanoid Robotics" book project. It covers setting up your development environment, running the Docusaurus documentation site locally, and executing the provided code examples.

## 1. Prerequisites

Before you begin, ensure you have the following installed on your system:

-   **Git**: For cloning the repository.
-   **Node.js** (v18 or higher) and **npm**: For Docusaurus development.
-   **Python 3.8+** and **pip**: For running Python code examples.
-   **Docker**: (Optional, but recommended) For running code examples in a consistent, isolated environment (especially for ROS 2).

## 2. Setting Up the Project

1.  **Clone the Repository**:

    ```bash
    git clone https://github.com/agentic-learning-org/agentic-learning.git
    cd agentic-learning
    ```

2.  **Install Docusaurus Dependencies**:

    ```bash
    npm install
    ```

## 3. Running the Documentation Site Locally

To start the Docusaurus development server and view the book locally:

```bash
npm start
```

This will open your browser to `http://localhost:3000` (or another available port). The site will hot-reload as you make changes to Markdown files or React components.

## 4. Running Code Examples

### 4.1. Running Python Code Examples

Individual Python examples can be run directly:

```bash
python3 code_examples/module1/ros2_publisher_subscriber.py # (Example path, will vary)
```

To run the automated test script for all Python examples:

```bash
python3 code_examples/run_tests.py
```

### 4.2. Running Code Examples with Docker (Recommended for ROS 2)

For a consistent environment, especially for ROS 2 examples, you can use Docker:

1.  **Build the Docker Image** (from the project root):

    ```bash
    docker build -t physical-ai-book-env -f code_examples/Dockerfile .
    ```

2.  **Run the Docker Container** (and execute the test script):

    ```bash
    docker run physical-ai-book-env
    ```

    Alternatively, to get a shell inside the container:

    ```bash
    docker run -it physical-ai-book-env bash
    ```
    Once inside the container, you can manually run ROS 2 commands or Python scripts. Ensure the ROS 2 environment is sourced:
    ```bash
    source /opt/ros/$ROS_DISTRO/setup.bash
    # Then run your ROS 2 commands, e.g.,
    # ros2 run my_ros2_package my_node
    ```

## 5. Building the Static Site

To build the static HTML, CSS, and JavaScript files for deployment:

```bash
npm run build
```

The built files will be located in the `build/` directory.
