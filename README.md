# StayEnlightened: A Brighter Study Space for Students

1. Background: The lighting in Myhal does not provide an ideal studying place. There currently exists two problems:
   1. To reduce energy consumption, Myhal uses a motion sensor to detect if there are people. This mechanism is used heavily in the non-popular floors, e.g. 8th floor.  This sensor works well with movement(e.g. when people walk by), however it doesn’t always  account for stationary students. As a result, the lights in Myhal 8th floor will completely turn off after 20 minutes if no motion is sensed. The student will then have to get up and wave at the sensor to re-activate the lights.

   2. Myhal also does not provide lighting in certain areas that are well-lit in the day, e.g. window-side desks near the window. During the late afternoon and evening, there is often not enough sunlight to study. This detracts people from going there and wastes the space.  

2. Objective: Maintain constant lighting in an energy-efficient way

3. Opportunity:

   1. Develop a new occupant detection via room-level occupant count and identify areas in use

      1. Once the (conventional motion) sensor detects people entering, the camera will be triggered and actively detects the occupancy based on OpenCV/machine learning. The conventional motion sensor will thus be kept at low sensitivity (sleep mode).
      2. This computer vision occupant detection will be the primary mechanism of monitoring occupancy. If the occupant detection reports no occupancy, the occupation detection will be de-activated and the (conventional motion) sensor will be activated.
      3. This detection method will more accurately report the usage of spaces and accordingly turn on/off lights in certain areas.
   2. Light sensing mechanism which monitors natural light and changes the light intensity based on the natural lighting. This is also activated when people are detected. The measured natural light intensity data will be sent back to the central system and thus determines the optimal lighting condition.
   3. IoT- this IoT platform that we build will consist of components connected to the internet:
       1. Camera for occupant detection
       2. Light sensing module
       3. Node at each location at risk of poor lighting with controllable light.
       4. Cloud software will receive the data uploaded by the camera and light sensors, process the data and return insights, and send new commands to each node.
       5. User interface: website/app to display current room occupancy. The student can then use that to determine where to study.
   4. Future steps: Predict peak occupancy times and implement smart building.
      As a future step, we could consider using more machine learning algorithms to predict usage of space in Myhal. This is based on the premise that people tend to go to the same space to study at regular times. (Though this may be harder to implement in the makeathon, might only reach an early prototype)
      
Documentation on Python-Arduino Serial Communication: https://docs.google.com/document/d/1F516TYp9qw56w44bUsVvy9g6Uo8SrwlXF3STm-RwaHA/edit?usp=sharing

4. References:
      1. https://www.nature.com/articles/s41597-019-0274-4#Sec6
      2. https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+
      3. https://www.kaggle.com/parulpandey/analysing-machine-learning-models-with-yellowbrick
      4. https://senstar.com/products/video-analytics/crowd-detection/
      5. https://www.analyticsvidhya.com/blog/2019/02/building-crowd-counting-model-python/
      6. https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/
