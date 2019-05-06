# marine-sci
Documents from my Marine Science Internship with Harvard Biorobotics Lab working with autonomous vehicles.

### Initial Meeting (1/28/19)

In this meeting, Professor Howe and I discussed potential goals for the semester.

- Platform
  - Underwater Vehicle/Submarine
  - Robotic Sailboat
- Onboard Processor (for vision and other sensors)
  - Raspberry Pi (ARM)
  - Arduino, or other microprocessor
  - Q: What can provide the processing power/speed needed?
- Language
  - Needs to be fast (C, C++, Rust, etc)
  - Needs to have relevant open source libraries
- Sensors (largely platform/task dependent)
  - Vision
  - Sonar
  - GPS
  - Radar
  - Wind Speed
  - Water Speed
  - IMU
- Methods
  - Vision-based targeting (follow-the-leader)
  - SLAM
  - Sonar beacons
  - GPS
- Tasks
  - Follow the leader
  - Search pattern - beacon or SLAM
  - Sailboat race (or underwater race)
  - Fish tracking
  - Mapping


### Notes

#### Run rviz on hector slam (no odom)
`roscore`
`rviz -d src/RPLidar_Hector_SLAM/hector_slam/hector_slam_launch/rviz_cfg/mapping_demo.rviz`
`rosbag play 2019-05-06-14-45-20.bag`
