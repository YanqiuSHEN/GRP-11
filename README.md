The GRP-11's Challenges
===
**The challenges for the UV of LARM**  

**Group Member:** Xuechu WANG & Yanqiu SHEN & Fan FEI  

 Preparation
 ---
 * Create a ROS-Kinetic ROSjet on The construct RDS.  
 
 * Clone and build this project in place of the initial `simulation_ws` directory. So, in RDS the terminal :  
 
 ```bash
 rm -fr simulation_ws
 git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git simulation_ws
 cd simulation_ws
 catkin_make
 source devel/setup.bash
 ```
 
 * Test the installation by the command: `roslaunch larm test.launch`. And open the Gazebo to see if there is the environment.  

 * Make the distant repositorie as your `catkin_ws` directory. So, in RDS the terminal:  
 
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
 * Open 3 WebShell, Gazebo and the Graphical Tools.  
 
 * Run the environment --> WebShell #1: `roslaunch larm challenge-1.launch`.  
 
 * Navigate the robot:  
   * with the map --> WebShell #2: `roslaunch challenge_1 navigation.launch`;  
   * without the map --> WebShell #2: `roslaunch challenge_1 navigation_nomap.launch`.  
  
 * Run the Rviz --> WebShell #3: `rosrun rviz rviz -d /home/user/catkin_ws/src/student_pkg/challenge_1/document_rviz/challenge_1.rviz`.
 
 * Using the 2D Navi Goal tool in the rviz to set the navigation for the robot.
 
 Challenge-2
 ---
 * Open 3 WebShell, Gazebo and the Graphical Tools.  
 
 * Run the environment and navigate the robot -->  WebShell #1: `roslaunch challenge_2 mapping_challenge_2.launch`.  
 
 * For dectecting the position of the bottle --> WebShell #2: `roslaunch challenge_2 bottle.launch`.  
 
 * Open the Graphical tools and you will see the images. 
 
 * To move the robot:  
   * Using the keyboard --> WebShell #3: `roslaunch turtlebot_teleop keyboard_teleop.launch`;  
   * Using 2D Navi Goal --> WebShell #3:  
    `rosrun rviz rviz -d /home/user/catkin_ws/src/student_pkg/challenge_2/document_rviz/challenge_2.rviz`.  
    (We recommend the first method, because in this environment, use 2D Navi Goal to move may be very slow)  
 
 * When the robot see the bottle of Nuka-Cola, the position of the robot will show in the WebShell #2. 
 
 Challenge-3
 ---
 * Open 4 WebShell, Gazebo and the Graphical Tools.
 
 * Run the environment --> WebShell #1: `roslaunch larm challenge-3.launch`.
 
 * Open the rviz --> WebShell #2:   
  `roslaunch rviz rviz -d /home/user/catkin_ws/src/student_pkg/challenge_3/document_rviz/challenge_3.rviz`.
  
 * Run the code for automatic navigation --> WebShell #3: `roslaunch challenge_3 exploration.launch`.
 
 * In the rviz, you have to set up the environment you want to explore, as shown below:()少图片
 
   (We used the algorithm of rrt_exploration. These environment is very complex and our move_base algorithm was not optimized, so the robot would probably stop exploring after a while.)
   
 * During the exploration, if the robot decet the Nuka-Cola, the position will show in the WebShell #3.
 
