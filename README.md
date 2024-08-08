
# Motion-Planning Robot in Gazebo

## Overview

This project involves a motion-planning robot simulated in the Gazebo environment. The robot is equipped with a camera that uses template matching to identify and locate specific objects within the environment. Once an object is identified, the robot navigates towards it.

### Key Features
- **Template Matching:** The robot's camera uses template matching to identify objects in the environment. 
- **Motion Planning:** Once an object is recognized, the robot plans and executes a path to approach the object.
- **Command Interface:** Users can interact with the robot via a simple text prompt interface. For example, typing "rubik" will command the robot to locate and move towards a Rubik's cube.
- **MoveIt Integration:** The project leverages the MoveIt Assistant for motion planning and control, ensuring smooth and efficient movements.

## Setup

### Prerequisites
- [ROS (Robot Operating System)](http://www.ros.org/) installed.
- [Gazebo](http://gazebosim.org/) simulator.
- [MoveIt](https://moveit.ros.org/) installed and configured.
- Python 3.6+ or equivalent for running the command interface.

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo-name/motion-planning-robot.git
    cd motion-planning-robot
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Build the ROS workspace:
    ```bash
    catkin_make
    source devel/setup.bash
    ```

## Usage

1. **Launch the Gazebo simulation:**
    ```bash
    roslaunch motion_planning_robot simulation.launch
    ```
2. **Run the command interface:**
    ```bash
    python3 command_interface.py
    ```
3. **Send a command:**
   - Type the name of the object you want the robot to locate, e.g., `rubik`, and press Enter.
   - The robot will identify the object using template matching, plan a path, and move towards it.

## Customization

- **Template Matching:** Modify the template images in the `templates/` directory to add or update the objects the robot can recognize.
- **Motion Planning:** Adjust the motion planning parameters in the MoveIt configuration files to tweak the robot's movement behavior.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
