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
