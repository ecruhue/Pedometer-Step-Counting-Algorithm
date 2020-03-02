# Pedometer
1 Sensor
We attempted to collect data using Gyroscope within the Inertial Measurement Unit (IMU).
2 Location
We assumed that we use the pedometer as a smartphone and we mimic the scenario when a walker holds their smartphone to walk.
Specifically, human can have various activities with their smartphones (i.e., swinging hands,
device in the trousers’ pockets, standing and typing). This essence can largely distinguish it
from the pedometer for wearables/ smartwatch/ glasses, whose location is unitary and fixed.
For example, using smartphone to type can also cause jitters.
To make our problem clearer, we attempt to classify the following scenarios except counting
steps:
1. Walking when holding the smartphone
2. Standing and typing/ Standing

In order to classify activities based on both time domain and frequency domain features
extracted from sensory data, we used fast fourier transformation (FFT) to extract the clustering
features.
In order to let the data update when the user is walking or standing, we used the sliding window
to collect the data every 1.2s and fit the algorithm for the previous 1.2 seconds

In order to increase the step count accuracy, we choose 2.4 seconds sliding window to add more data points, however, this will make the processing a bit slow and hard to observe the classification result. If we decrease the sliding window duration to 1.2 seconds, the data points will be decreased and hence decrease the processing duration, yet the step count accuracy might be penalized.
