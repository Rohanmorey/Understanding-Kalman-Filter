# Understanding-Kalman-Filter
Easy approach to understand Kalman filter. A quick and short crisp information to understand it in a easy way

# Kalman Filter for 1D Position Estimation

A Kalman filter is a powerful algorithm used for estimating the state of a system over time, even when measurements are uncertain or noisy. For a single value like position, it helps you estimate the actual position of an object over time, based on sensor readings, which are often noisy or inaccurate.

## How the Kalman Filter Works

### 1. State Representation

- **State**: The position you want to estimate.
- **State estimate**: An estimate of the current position.
- **Error covariance**: How confident you are in your estimate (uncertainty).

### 2. Process and Measurement Models

- **Process model**: Describes how the position changes over time (could be constant or involve velocity, acceleration, etc.).

    \[
    x_k = x_{k-1} + v_{k-1} + \text{process noise}
    \]

    where \( x_k \) is the current position, \( x_{k-1} \) is the previous position, and \( v_{k-1} \) is velocity.

- **Measurement model**: Describes how you measure the position.

    \[
    z_k = x_k + \text{measurement noise}
    \]

    where \( z_k \) is the actual measurement (which includes some noise).

### 3. Kalman Filter Steps

The Kalman filter operates in two phases: **predict** and **update**.

#### A. Prediction

In this step, you predict the next position based on the current estimate and the process model. You also update the uncertainty.

- **Predicted state**:
  
    \[
    \hat{x}_k^{-} = \hat{x}_{k-1} + v_{k-1}
    \]

    where \( \hat{x}_k^{-} \) is the predicted position.

- **Predicted error covariance**:

    \[
    P_k^{-} = P_{k-1} + Q
    \]

    where \( P_k^{-} \) is the predicted uncertainty, and \( Q \) is the process noise covariance.

#### B. Update

Once you have a new measurement, you update your position estimate and reduce the uncertainty.

- **Kalman Gain**:

    \[
    K_k = \frac{P_k^{-}}{P_k^{-} + R}
    \]

    where \( R \) is the measurement noise covariance, and \( K_k \) is the Kalman Gain (it determines how much the measurement influences the estimate).

- **Updated state estimate**:

    \[
    \hat{x}_k = \hat{x}_k^{-} + K_k (z_k - \hat{x}_k^{-})
    \]

    where \( z_k \) is the measured position, and \( \hat{x}_k \) is the updated position estimate.

- **Updated error covariance**:

    \[
    P_k = (1 - K_k) P_k^{-}
    \]

### 4. Repeat

With every new measurement, the process repeats: predict the next position, and then update based on the measurement.

## Summary of Key Equations

- **Prediction**:

    \[
    \hat{x}_k^{-} = \hat{x}_{k-1} + v_{k-1}
    \]

    \[
    P_k^{-} = P_{k-1} + Q
    \]

- **Update**:

    \[
    K_k = \frac{P_k^{-}}{P_k^{-} + R}
    \]

    \[
    \hat{x}_k = \hat{x}_k^{-} + K_k (z_k - \hat{x}_k^{-})
    \]

    \[
    P_k = (1 - K_k) P_k^{-}
    \]

