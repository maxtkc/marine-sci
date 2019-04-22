# Annotated Bibliography
> This is a simple/rough working list of resources & captions -- nothing fancy


### [Creating A Low-Cost Autonomous Vehicle](http://isl.ecst.csuchico.edu/DOCS/Logs/Michael/Files/web_link_files/low_cost.pdf)

- Used GPS
- 2002, so not too useful


### [Autonomous Ship Hull Inspection by Omnidirectional Path and View](http://srv.uib.es/public/AUV2016/pdf/SP7.pdf)

- Very cool application
- Rough grammar...
- Coordination between the robots movement and the camera's view is very important. It must steer to keep the camera moving in a straight path.
- Doppler Velocity Logger (Teledyne) used for navigation
  - Found [SeaPILOT](http://rowetechinc.com/seapilot/) (made for underwater navigation)
    - Uses Sonar? (refers to pings to the water surface and to the sea bottom)
    - Probably expensive (quote)
    - Seems fairly accurate
  - **Doppler Velocity Logger (DVL)** may be worth looking into
  - \$500 -- very pricey...
- Also uses 10 DOF IMU
- Tritech Micron Sonar
  - Found [Micron - Mechanical Scanning Sonar (Small ROV)](https://www.tritech.co.uk/product/small-rov-mechanical-sector-scanning-sonar-tritech-micron)
    - `smallest digital CHIRP sonar in the world`
  - **Tritech** has high performance underwater technologies
  - Uses this sensor with SLAM
  - \$14k -- out of question
- Diagonal thruster placement
- Panda Board ES with dual-core Cortex-A9 MPCore with symmetric multiprocessing (SMP) at up to 1.2 GHz and 1 GB DDR2 RAM.
- 22.2V with LiPo batteries
  - Power distribution board
- [Robot Operating System (ROS)](http://www.ros.org/)
  - Linux based
  - **ROS may be worth using if OS is needed**
- Sensors are very expensive


### [2016 IEEE/OES Autonomous Underwater Vehicles Conference list of papers](http://toc.proceedings.com/32600webtoc.pdf)


### [Surveillance of Coral Reef Development Using an Autonomous Underwater Vehicle](http://srv.uib.es/public/AUV2016/pdf/SP3.pdf)

- High budget (but they still use an Adafruit 10 DOF IMU!)
- Very relatable to Marine Biology/Science
- Submarine-like shape due to a long tube for a frame
- BlueRobotics thrusters
- Uses OpenCV and python to do image processing
  - Is python too slow?
- NUC Single Board computer with 6th Gen Intel Processor
- Kodak PIXPRO SP360 for camera -- very wide-angle lens


### [Behavior-Based Control for Autonomous Underwater Exploration](https://pdfs.semanticscholar.org/c263/0628c0aa66cb0cdd21ad5e554e43c27f588b.pdf)

- Interesting overview of a logic system used to determine commands for the robot based on data
- Behaviors
  - Maintain Altitude
  - Avoid Collisions
  - Follow Rope (survey line)
  - Follow Targets
- DAMN fuzzy logic arbiter
    - each behavior casts a weighted vote for what the bot should do
    - `defuzzification` -- new favorite word?


### [TeraRanger Evo Inexpensive LiDAR](http://www.teraranger.com/product/teraranger-evo/)

- Less than \$200


### [SparkFun TFMini Micro LiDAR Module](https://www.sparkfun.com/products/14588)

- \$40
- Communicates over 3.3V UART at 115200 baud
- `This product does not use laser light for ranging. Instead it contains an LED and optics. Many such systems are being marketed under the name "LiDAR," although it may be more appropriate to think of this device as a "Time-of-Flight Infrared Rangefinder". It differs significantly from traditional IR rangefinders in that it uses ToF to determine range and not triangulation — as is performed by the Sharp GP-series devices.`


### [SparkFun LiDAR-Lite v3](https://www.sparkfun.com/products/14032)

- \$130 sensor from Garmin™
- Interfaced via I2C or PWM
- 5V <100mA
- 40 meter


### [Optical Sensors and Methods for Underwater 3D Reconstruction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4721784/)

- Describes the refraction of light passing from air to glass to water
- Three major classes of measuring (definitely overlap)
  - Triangulation
    - structured light
    - laser stripe
    - photometric stereo
    - structure from motion
    - stereo vision
  - Time of Flight
    - Sonar
    - LiDAR
    - Pulse generated laser line scanning
  - Modulation
    - Amplitude modulation of blue-green laser
  - Sensors and Technologies
    - Sonar
    - LiDAR
    - Laser Line Scanning
    - Structured Light
    - Photometric Stereo
    - Structure from Motion
    - Stereo Vision
    - Underwater Photogrammetry
- [Table](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4721784/table/sensors-15-29864-t009/?report=objectonly) overviewing strengths and weaknesses of sensors and techniques for 3D reconstruction
- **TODO: Read more of these sensors**


### [BreezySLAM LiDAR SLAM Open Source Library for Python (and c/cpp/java/matlab)](https://github.com/simondlevy/BreezySLAM)

- 


### [SLAM Lectures](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm)

- Lectures go over SLAM from the ground up, working towards a robot that uses SLAM completely
- Worth watching if doing SLAM project


### [RI Seminar: Matthew Johnson-Roberson : Underwater mapping: new robotic approaches to an old problem](https://www.youtube.com/watch?v=jbiPFUxP8h8)

- Very few high resolution (<5cm per pixel) underwater maps are available
- Old methods
  - Leadline (drop lead on a line)
  - Single Beam Sonar
  - Multibeam Sonar (similar to lidar)
- Modern Methods
  - stereo cameras: can work, but only very close up
  - lidar: can work, not as easy as above water
  - satellite: cannot penetrate water
- Large scale ROV's are very expensive in many ways
  - Tether is huge
  - Million dollar ROV's
  - Pay for driver
  - Brought out with a boat and crane
- Bundle adjustment helps
- Talks about mapping hull bottoms
- Uses camera image data to texture 3d maps
  - Makes them more visually appealing for humans
- TODO: Rewatch and take notes

### [DF Robot TF Mini LiDAR(ToF) Laser Range Sensor](https://www.dfrobot.com/product-1702.html)

- \$40
- Static laser LiDAR

### [DF Robot RPLIDAR A1M8 - 360 Degree Laser Scanner Development Kit](https://www.dfrobot.com/product-1125.html)

- \$99
- `scanning frequency reached 5.5 hz when sampling 1450 points each round`
- Rotating! That would make the electricals/mechanicals a lot easier


### [Jaffe Laboratory for Underwater Imaging](http://jaffeweb.ucsd.edu/)

- 9 projects relating to underwater imaging


### [OpenSLAM](https://openslam-org.github.io/)

- A couple dozen projects working with SLAM algorithms
- Fantastic set of resources!!
  - Papers, libraries, datasets, people
- Some are a bit old
- A variety of 2d/3d, sensors, strategies

### [SSS-SLAM: An Object Oriented Matlab Framework for Underwater SLAM using Side Scan Sonar](http://www.ja2014.upv.es/wp-content/uploads/papers/paper_48.pdf)

- `Side Scan Sonars (SSS) are frequently used by Autonomous Underwater Vehicles (AUV) to observe the sea floor.`
- A bit old, but could be very useful resource for using SSS
- Created impressive trajectories improving upon the dead reckoning techniques as well as mosaics to visualize the acoustic images
- Everything is open source (including dataset)


### [Underwater 3-D Scene Reconstruction Using Kinect v2 Based on Physical Models for Refraction and Time of Flight Correction](https://www.researchgate.net/publication/318869088_Underwater_3D_Scene_Reconstruction_Using_Kinect_v2_Based_on_Physical_Models_for_Refraction_and_Time_of_Flight_Correction)

- 2017 (recent)
- Point cloud data up to 650 mm
- Created a waterproof housing for the Kinect (publicly available)
- `Applications such as coral reef mapping and underwater SLAM in shallow waters for ROV’s can be a viable application area that can beneﬁt from results achieved`
- They have to correct for the refraction of the air -> perspex (container) -> water


### [Underwater Distance Measurement/Sensing (Build your own, StackExchange)](https://electronics.stackexchange.com/questions/55804/underwater-distance-measurement-sensing)

- Explains how to build your own lidar sensor, and what the constraints are
- `Why this works with a laser but not necessarily with UV LEDs: 
The light from an LED is not collimated, hence does not get significantly intensified in the return direction, whereas a combination of reflection and diffraction causes significant pulsed intensification of such returned signal for a collimated laser beam, by speckle pattern formation.`
- 


### [Hector SLAM without odometry data on ROS with the RPLidar A1](https://github.com/NickL77/RPLidar_Hector_SLAM)

- Requires ROS Kinetic
