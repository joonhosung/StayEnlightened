import React, { Component } from 'react'

class About extends Component {
    render() {
        return (
            <div>
                <p>Background: The lighting in Myhal does not provide an ideal studying place. There currently exists two problems:
To reduce energy consumption,Myhal uses a motion sensor to detect if there are people. This mechanism is used heavily in the non-popular floors, e.g. 8th floor.  This sensor works well with movement(e.g. When people walk by), however it doesn’t always  account for stationary students. As a result, the lights in Myhal 8th floor will completely turn off after 20 minutes if no motion is sensed. The student will then have to get up and wave at the sensor to re-activate the lights.
Myhal also does not provide lighting in certain areas that are well-lit in the day, e.g. window-side desks near the window. During the late afternoon and evening, there is often not enough sunlight to study. This detracts people from going there and wastes the space.
Objective: Maintain constant lighting in an energy-efficient way
</p>
<p>
Opportunity
Develop a new occupant detection via room-level occupant count and identify areas in use
Once the (conventional motion) sensor detects people entering, the camera will be triggered and actively detects the occupancy based on OpenCV/machine learning. The conventional motion sensor will thus be kept at low sensitivity (sleep mode).
This computer vision occupant detection will be the primary mechanism of monitoring occupancy. If the occupant detection reports no occupancy, the occupation detection will be de-activated and the (conventional motion) sensor will be activated.
This detection method will more accurately report the usage of spaces and accordingly turn on/off lights in certain areas.
Light sensing mechanism which monitors natural light and changes the light intensity based on the natural lighting. This is also activated when people are detected. The measured natural light intensity data will be sent back to the central system and thus determines the optimal lighting condition.
IoT- this IoT platform that we build will consist of components connected to the internet:
</p>
<p>
Camera for occupant detection
Light sensing module
Node at each location at risk of poor lighting with controllable light.
Cloud software will receive the data uploaded by the camera and light sensors, process the data and return insights, and send new commands to each node.
User interface: website/app to display current room occupancy. The student can then use that to determine where to study.
Future steps: Predict peak occupancy times and implement smart building.
As a future step, we could consider using more machine learning algorithms to predict usage of space in Myhal. This is based on the premise that people tend to go to the same space to study at regular times. (Though this may be harder to implement in the makeathon, might only reach an early prototype)
</p>
            </div>
        )
    }
}

export default About
