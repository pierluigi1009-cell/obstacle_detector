# 🛰️ Obstacle Detector – ROS2 Package

This ROS2 package extends the [sllidar_ros2](https://github.com/Slamtec/sllidar_ros2) project by adding two custom nodes for **obstacle detection and clustering**.  
It was developed and tested in a ROS2 workspace under Ubuntu (VirtualBox environment).

---

## 📦 Project Overview

The `obstacle_detector` package contains:
- `obstacle_detector_node.py` — simple node just to check if there is object near the Lidar  
- `obstacle_clusters_node.py` — node that detect different objects near the Lidar
You can easily modify parameters of detection in each nodes
---

## 🧩 Prerequisites

Make sure you have:
- **ROS2 Humble** or newer  
- A working **ROS2 workspace** (`ros2_ws`)  
- The base **sllidar_ros2** package cloned and built  

---

## ⚙️ Installation

Clone this repository inside your ROS2 workspace:

```bash
cd ~/ros2_ws/src
```bash
git clone https://github.com/pierluigi1009-cell/obstacle_detector.git
```bash
cd ~/ros2_ws
```bash
colcon build --packages-select obstacle_detector
```bash
source install/setup.bash
