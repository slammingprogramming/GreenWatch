import random
import time


class Sensor:
    def __init__(self, name):
        self.name = name

    def read_value(self):
        """Simulate reading a sensor value."""
        return round(random.uniform(0, 100), 2)


class GreenWatch:
    def __init__(self):
        self.sensors = {
            "energy": Sensor("Energy Consumption Sensor"),
            "air_quality": Sensor("Air Quality Sensor"),
            "waste_management": Sensor("Waste Management Sensor")
        }
        self.data = {
            "energy": [],
            "air_quality": [],
            "waste_management": []
        }

    def monitor_environment(self):
        """Collect data from each sensor and store it."""
        for sensor_name, sensor in self.sensors.items():
            value = sensor.read_value()
            self.data[sensor_name].append(value)
            print(f"{sensor.name} reading: {value}")

    def analyze_data(self):
        """Analyze collected data to make recommendations."""
        recommendations = {}

        if self.data["energy"]:
            avg_energy = sum(self.data["energy"]) / len(self.data["energy"])
            if avg_energy > 75:
                recommendations["energy"] = "High energy use detected. Consider reducing appliance use for peak hours."
            elif avg_energy < 30:
                recommendations["energy"] = "Energy usage is optimal."

        if self.data["air_quality"]:
            avg_air_quality = sum(self.data["air_quality"]) / len(self.data["air_quality"])
            if avg_air_quality < 40:
                recommendations["air_quality"] = "Air quality poor. Consider using air purifier/improving ventilation."
            elif avg_air_quality > 80:
                recommendations["air_quality"] = "Air quality is excellent."

        if self.data["waste_management"]:
            avg_waste_management = sum(self.data["waste_management"]) / len(self.data["waste_management"])
            if avg_waste_management > 50:
                recommendations["waste_management"] = "Waste levels are high. Consider reducing and recycling waste."

        return recommendations

    def optimize_environment(self):
        """Optimize the environment based on sensor data."""
        recommendations = self.analyze_data()
        for area, recommendation in recommendations.items():
            print(f"Optimization Recommendation for {area}: {recommendation}")

    def display_dashboard(self):
        """Display current sensor data and environmental insights."""
        print("\n---- GreenWatch Dashboard ----")
        for sensor_name, values in self.data.items():
            if values:
                latest_value = values[-1]
                print(f"{sensor_name.capitalize()} - Latest Reading: {latest_value}")
        recommendations = self.analyze_data()
        for area, recommendation in recommendations.items():
            print(f"{area.capitalize()} Recommendation: {recommendation}")

# Main Loop


def main():
    greenwatch = GreenWatch()
    print("Starting GreenWatch Environmental Monitoring System...")

    try:
        while True:
            greenwatch.monitor_environment()
            time.sleep(2)  # Simulate time between sensor readings
            greenwatch.display_dashboard()
            greenwatch.optimize_environment()
            print("\nSleeping for next cycle...\n")
            time.sleep(5)  # Wait before the next monitoring cycle

    except KeyboardInterrupt:
        print("Stopping GreenWatch Monitoring System.")


if __name__ == "__main__":
    main()
