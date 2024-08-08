To track a location without using the native location services on a mobile device, such as GPS, cellular, or Wi-Fi settings, is generally not feasible with standard location tracker apps. Location tracking typically relies on these services to determine geographic coordinates accurately. Here’s why:

## Why Location Services Are Necessary:
### GPS:
Provides the most accurate location data by using satellite signals. It's essential for precise tracking.
### Cellular Networks:
Can estimate location based on the proximity to cell towers but is less accurate than GPS.
### Wi-Fi Networks:
Can help determine location by referencing known Wi-Fi networks, but it also requires network access.


# MIT App Inventor and Location Services:
MIT App Inventor uses the device’s built-in location services to track and display location data. The LocationSensor component in MIT App Inventor relies on:

### GPS: 
For accurate, real-time location tracking.
### Network-based methods:
As a fallback when GPS is not available.

# Conclusion:
For a location tracker app created with MIT App Inventor or any other mobile development platform, it is crucial to have location services enabled on the device for accurate tracking. Without these services, the app cannot reliably track the location of the device.