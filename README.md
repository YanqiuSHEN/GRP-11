The GRP-11's Challenges
===
**The challenges for the UV of LARM**  

**Group Member:** Xuechu WANG & Yanqiu SHEN & Fan FEI  

 Preparation
 ---
 1.Create a ROS-Kinetic ROSjet on The construct RDS.  
 
 2.Clone and build this project in place of the initial `simulation_ws` directory. So, in RDS the terminal :  
 
 ```bash
 rm -fr simulation_ws
 git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git simulation_ws
 cd simulation_ws
 catkin_make
 source devel/setup.bash
 ```
 
 3.Test the installation by the command: `roslaunch larm test.launch`. And open the Gazebo to see if there is the environment.  

 4.Make the distant repositorie as your `catkin_ws` directory. So, in RDS the terminal:  
 
 ```bash
 rm -fr catkin_ws
 git clone https://github.com/YanqiuSHEN/GRP-11.git catkin_ws
 cd ~/catkin_ws/
 mkdir src
 catkin_make
 source devel/setup.bash
 ```
 
 Challenge-1
 ---
 1.Open 3 WebShell, Gazebo and the Graphical Tools.  
 
 2.Run the environment --> WebShell #1: `roslaunch larm challenge-1.launch`.  
 
 3.Navigate the robot:  
  * with the map --> WebShell #2: `roslaunch challenge_1 navigation.launch`;  
  * without the map --> WebShell #2: `roslaunch challenge_1 navigation_nomap.launch`.  
  
 4.Run the Rviz --> WebShell #3: `rosrun rviz rviz`.  
 
 5.In the Rviz, open the configuration: Open Files --> Open config --> /home/user/catkin_ws/src/student_pkg/challenge_1/document_rviz/challenge_1.rviz 
