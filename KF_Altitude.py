import numpy as np
import matplotlib.pyplot as plt

# Simulate true altitude (UAV maintaining 10m)
n_timesteps = 50
true_altitude = np.full(n_timesteps, 10)  # Constant 10m altitude

# Simulate noisy sensor readings
np.random.seed(42)
measurement_noise = np.random.normal(0, 0.5, n_timesteps)  # Small noise
sensor_readings = true_altitude + measurement_noise

# Initialize variables for Kalman Filter
altitude_estimate = 9.5  # Initial guess
error_covariance = 1  # Initial uncertainty
process_noise = 0.01  # Process noise covariance (small)
measurement_noise_covariance = 0.5**2  # Measurement noise covariance
altitude_estimates = []  # Store the estimates

# Kalman Filter Implementation
for z in sensor_readings:
    # Prediction step
    predicted_altitude = altitude_estimate
    predicted_error_covariance = error_covariance + process_noise
    
    # Update step
    kalman_gain = predicted_error_covariance / (predicted_error_covariance + measurement_noise_covariance)
    altitude_estimate = predicted_altitude + kalman_gain * (z - predicted_altitude)
    error_covariance = (1 - kalman_gain) * predicted_error_covariance
    
    # Store the result
    altitude_estimates.append(altitude_estimate)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(true_altitude, label='True Altitude', color='green', linestyle='dashed')
plt.plot(sensor_readings, label='Noisy Sensor Readings', color='red', linestyle='dotted')
plt.plot(altitude_estimates, label='Kalman Filter Estimate', color='blue')
plt.xlabel('Time step')
plt.ylabel('Altitude (m)')
plt.legend()
plt.title('Kalman Filter for UAV Altitude Estimation')
plt.grid(True)
plt.show()
