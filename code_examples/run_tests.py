import os
import subprocess
import sys

def run_python_code_examples():
    print("Running Python code examples...")
    code_examples_dir = os.path.join(os.path.dirname(__file__))
    python_files = [f for f in os.listdir(code_examples_dir) if f.endswith('.py') and f != os.path.basename(__file__)]

    all_passed = True
    if not python_files:
        print("No Python code examples found to run.")
        return True

    for py_file in python_files:
        file_path = os.path.join(code_examples_dir, py_file)
        print(f"--- Running {py_file} ---")
        try:
            # Execute Python script with a timeout
            result = subprocess.run([sys.executable, file_path], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"SUCCESS: {py_file} ran without errors.")
                print("Output:")
                print(result.stdout)
            else:
                print(f"FAILED: {py_file} exited with error code {result.returncode}.")
                print("Stdout:")
                print(result.stdout)
                print("Stderr:")
                print(result.stderr)
                all_passed = False
        except subprocess.TimeoutExpired:
            print(f"FAILED: {py_file} timed out after 10 seconds.")
            all_passed = False
        except Exception as e:
            print(f"ERROR: Could not run {py_file}: {e}")
            all_passed = False
    return all_passed

def check_ros2_environment():
    print("Checking ROS 2 environment...")
    # Check if ROS_DISTRO is set, indicating ROS 2 is sourced
    if "ROS_DISTRO" in os.environ and os.environ["ROS_DISTRO"]:
        print(f"ROS_DISTRO is set to {os.environ['ROS_DISTRO']}.")
        # Further check if colcon is available
        try:
            subprocess.run(["colcon", "--version"], capture_output=True, check=True)
            print("colcon build tool found. ROS 2 environment appears to be set up.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("colcon build tool not found, or ROS 2 environment is incomplete.")
            return False
    else:
        print("ROS_DISTRO not set. ROS 2 environment is not sourced.")
        return False

def main():
    python_tests_passed = run_python_code_examples()
    ros2_env_ok = check_ros2_environment()

    if python_tests_passed and ros2_env_ok:
        print("\nAll foundational code example tests and ROS 2 environment checks passed!")
        sys.exit(0)
    else:
        print("\nSome foundational code example tests or ROS 2 environment checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
