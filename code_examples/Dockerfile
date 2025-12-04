# Use a base image with ROS 2 Humble already installed
FROM ros:humble-ros-base

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-rosdep \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init || true && rosdep update

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install any additional Python packages required by your code examples
# For example, if you use numpy, uncomment the line below:
# RUN pip install numpy

# Copy the code examples directory into the container
COPY . /app/code_examples

# Source the ROS 2 environment
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
ENV PYTHONPATH=/app/code_examples:$PYTHONPATH

# Make the test script executable
RUN chmod +x /app/code_examples/run_tests.py

# Set the default command to run the test script
CMD ["/app/code_examples/run_tests.py"]
