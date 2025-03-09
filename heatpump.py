import polars as pl
import plotly.express as px


class HeatPump:
    # TODO Explain how an heatpump works and what are the steps involved
    refrigerant_properties = {
        "R410A": {
            "critical_temp": 72.5,  # °C: Temperature above which a gas cannot be liquified.
            "boiling_point": -48.5,  # °C: Temperature where refrigerant changes phase
            "specific_heat_capacity_liquid": 1.55,  # kJ/(Kg.K): Energy required to raise temperature
            "specific_heat_capacity_gas": 0.85,  # kJ/(Kg.K): Energy required to raise temperature
            "latent_heat": 240,  # kJ/Kg: Energy required to change phase without temperature change
            "molecular_weight": 72.58,  # g/mol
        },
        "R134A": {
            "critical_temp": 101.1,  # °C: Temperature above which a gas cannot be liquified.
            "boiling_point": -26.1,  # °C: Temperature where refrigerant changes phase
            "specific_heat_capacity_liquid": 1.4,  # kJ/(Kg.K): Energy required to raise temperature
            "specific_heat_capacity_gas": 0.93,  # kJ/(Kg.K): Energy required to raise temperature
            "latent_heat": 215,  # kJ/Kg: Energy required to change phase without temperature change
            "molecular_weight": 102.03,  # g/mol
        },
    }

    def __init__(self, refrigerant="R410A", rated_power=3):  # rated_power in Watts
        """
        Advanced Heat Pump Simulation with Detailed Thermodynamic Modeling

        :param refrigerant: Type of refrigerant used in the system
        """

        # System parameters
        self.refrigerant = refrigerant
        self.mass_flow_rate = 0.05  # kg/s
        self.compressor_efficiency = 0.85
        self.heat_exchanger_efficiency = 0.75

        # Thermodynamic Cycle Parameters
        self.pressure_ratio = 4.0  # Compression ratio
        self.superheat_temp = 5  # °C above saturated vapor
        self.subcooling_temp = 5  # °C below saturated liquid

        # Energy Consumption Parameters
        self.rated_power = rated_power
        self.standby_power = 0.001  # kW: Usually 5-30 Watts.
        self.defrost_power = rated_power * 1.2  # Assumes 20% more power during defrost
        self.auxiliary_heater_power = 2  # kW

        # Operating Cost Parameters
        self.electricity_rate = 0.80  # $/kWh

    def calculate_carnot_cop(self, source_temp, sink_temp):
        """
        Calculate the ideal (Carnot) Coefficient of Performance

        :param source_temp: Temperature of heat source (K)
        :param sink_temp: Temperature of heat sink (K)
        :return: Ideal CoP
        """
        return sink_temp / (sink_temp - source_temp)

    def calculate_real_cop(self, source_temp, sink_temp):
        """
        Calculate realistic Coefficient of Performance
        Considers real-world inefficiencies

        :param source_temp: Temperature of heat source (K)
        :param sink_temp: Temperature of heat sink (K)
        :return: Realistic CoP
        """

        carnot_cop = self.calculate_carnot_cop(source_temp, sink_temp)

        # Apply compressor and heat exchanger inefficiencies
        real_cop = (
            carnot_cop * self.compressor_efficiency * self.heat_exchanger_efficiency
        )
        return real_cop

    def simulate_thermodynamic_cycle(
        self, mode="cooling", source_temp=35, sink_temp=20
    ):
        """
        Simulate complete themodynamic cycle

        :param mode: 'heating' or 'cooling'
        :param source_temp: Source temperature (°C)
        :param sink_temp: Sink temperature (°C)
        :return: Detailed cycle performance
        """
        # Convert temperatures to Kelvin
        source_temp_k = source_temp + 273.15
        sink_temp_k = sink_temp + 273.15

        # Get refrigerant properties
        props = HeatPump.refrigerant_properties[self.refrigerant]

        # Cycle Stages
        # 1. Evaporation (Heat Absorption)
        # 2. Compression
        # 3. Condensation (Heat Rejection)
        # 4. Expansion

        # Calculate Performance Metrics
        cop = self.calculate_real_cop(source_temp_k, sink_temp_k)

        # TODO Add heat transfer equation and laws of energy conservation(thermodynamics) for reference

        # Latent heat (phase change)
        q_latent = self.mass_flow_rate * props["latent_heat"]

        # Superheat
        q_superheat = (
            self.mass_flow_rate
            * props["specific_heat_capacity_gas"]
            * self.superheat_temp
        )

        # Heat transfer calculations
        if mode == "heating":
            # Heat is absorbed from source

            # Sensible heat (liquid heating to boiling point)

            # TODO props["boiling_point"] is incorrect here.
            # This needs to be changed to actual temperature of the refrigerant.
            # The refrigerant is maintained at a particular temperature by
            # application of pressure by the compressor.
            q_sensible = (
                self.mass_flow_rate
                * props["specific_heat_capacity_liquid"]
                * (props["boiling_point"] + 273.15 - source_temp_k)
            )

            # Total heat absorption
            q_evaporator = abs(q_sensible) + q_latent + q_superheat

            # Work input to compressor
            w_compressor = q_evaporator / cop

            # Heat realease to the sink
            q_condensor = q_evaporator + w_compressor

        else:  # cooling mode
            # Calculations similar to heating but reversed for cooling

            # Heat rejected to the sink

            # Sensible heat (liquid heating to boiling point)

            # TODO props["boiling_point"] is incorrect here.
            # This needs to be changed to actual temperature of the refrigerant.
            # The refrigerant is maintained at a particular temperature by
            # application of pressure by the compressor.
            q_sensible = (
                self.mass_flow_rate
                * props["specific_heat_capacity_liquid"]
                * (sink_temp_k - props["boiling_point"] + 273.15)
            )

            # Total heat absorption
            q_condensor = abs(q_sensible) + q_latent + q_superheat

            # Work input to compressor
            w_compressor = q_condensor / cop

            # Heat absorbed from source
            q_evaporator = q_condensor - w_compressor

        return {
            "mode": mode,
            "source_temp": source_temp,
            "sink_temp": sink_temp,
            "cop": cop,
            "evaporator_heat_transfer": q_evaporator,
            "compressor_work": w_compressor,
            "condensor_heat_transfer": q_condensor,
            "details": {
                "sensible_heat": q_sensible,
                "latent_heat": q_latent,
                "superheat": q_superheat,
            },
        }

    def performance_map(self, mode="heating", temp_range=None):
        """
        Generate comprehensive performance map

        :param mode: 'heating' or 'cooling'
        :param temp_range: Custom temperature range to simulate
        :return: Performance data across temperatures
        """
        if temp_range is None:
            # Default temperature ranges
            if mode == "heating":
                temp_range = {"source": range(-5, 20, 5), "sink": range(35, 55, 5)}
            else:  # cooling
                temp_range = {"source": range(20, 45, 5), "sink": range(18, 30, 5)}

        performance_data = []

        for so in temp_range["source"]:
            for si in temp_range["sink"]:
                cycle_data = self.simulate_thermodynamic_cycle(
                    mode=mode, source_temp=so, sink_temp=si
                )
                performance_data.append(cycle_data)

        return performance_data

    def visualize_performance(self, performance_data):
        """
        Create detailed visualization of heat pump performance

        :param performance_data: Performance data from simulation
        """

        # Extract data for plotting
        source_temps = [data["source_temp"] for data in performance_data]
        sink_temps = [data["sink_temp"] for data in performance_data]
        cops = [data["cop"] for data in performance_data]
        heat_transfers = [data["condensor_heat_transfer"] for data in performance_data]

        df_cops = pl.DataFrame(
            data={
                "Source Temperature (°C)": source_temps,
                "Sink Temperature (°C)": sink_temps,
                "Coefficient of Performance (CoP)": cops,
                "Condensor Heat Transfer": heat_transfers,
            }
        )

        # Create plots

        # CoP plot
        cop_plot = px.scatter(
            data_frame=df_cops,
            x="Source Temperature (°C)",
            y="Sink Temperature (°C)",
            color="Coefficient of Performance (CoP)",
            title="Coefficient of Performance (CoP)",
        )
        cop_plot.show()

        # Heat Transfer Plot
        cht_plot = px.scatter(
            data_frame=df_cops,
            x="Source Temperature (°C)",
            y="Sink Temperature (°C)",
            color="Condensor Heat Transfer",
            title="Condensor Heat Transfer",
        )
        cht_plot.show()

    def calculate_power_consumption(self, outdoor_temp, indoor_temp, mode="heating"):
        """
        Calculate instantenous power consumpionbased on conditions

        :param outdoor_temp: Outdoor temperature (°C)
        :param indoor_temp: Indoor temperature (°C)
        :param mode: 'heating' or 'cooling'
        :return: Dictionary with power consumption details
        """

        # Base power calculation using temperature difference
        temp_diff = abs(outdoor_temp - indoor_temp)

        # Calculate Part Load Ratio (PLR)
        # PLR determines how hard the heat pump needs to work relative to its maximum capacity
        # Normaized to 20°C (assumes full capacity at >= 20°C)
        # Capped at 1.0 (100% capacity)
        plr = min(1.0, temp_diff / 20.0)

        # Calculate compressor power
        # Scales the rated power by the part load ratio
        # The compressor consumes more power when temperature differences are larger
        compressor_power = self.rated_power * plr

        # Fan power (constant)
        # Assumes fans consume 10% of the rated power
        # Fan power is constant regardless of the load
        fan_power = self.rated_power * 0.1

        # Additional power factors
        # 1. Defrosting is needed if outdoor temperature is < 5°C.
        # It prevents ice buildup on the outdoor coil.
        defrost_needed = mode == "heating" and 5 > outdoor_temp
        # 2. Auxiliary electric heating is activated below -5°C.
        # This suppliments the heat pump when it becomes less efficient in very cold weather
        auxiliary_heat_needed = mode == "heating" and -5 > outdoor_temp

        # Calculate total power
        total_power = self.standby_power + compressor_power + fan_power

        if defrost_needed:
            defrost_factor = 0.1  # Assumes 10% of operating time spent in defrost
            total_power += self.defrost_power * defrost_factor

        if auxiliary_heat_needed:
            # The factor increases as temperature drops below -5°C.
            # Scales linearly: at -15°C, factor=1.0 (full auciliary power)
            aux_heat_factor = (-outdoor_temp - 5) / 10
            total_power += self.auxiliary_heater_power * aux_heat_factor

        return {
            "total_power": total_power,
            "compressor_power": compressor_power,
            "fan_power": fan_power,
            "defrost_power": self.defrost_power if defrost_needed else 0,
            "auxiliary_power": self.auxiliary_heater_power
            if auxiliary_heat_needed
            else 0,
            "standby_power": self.standby_power,
            "part_load_ratio": plr,
        }

    def calculate_daily_consumption(self, daily_temps, mode="heating", target_temp=21):
        """
        Calculate daily energy consumption

        :param daily_temps: List fo 24 hourly temperatures
        :param mode: 'heating' or 'cooling'
        :param target_temp: Target indoor temperature
        :return: Dictionary with daily consumption metrics
        """
        hourly_consumption = []
        total_energy = 0
        peak_power = 0

        for hour, temp in enumerate(daily_temps):
            power_data = self.calculate_power_consumption(temp, target_temp, mode)
            hourly_energy = power_data["total_power"]
            total_energy += hourly_energy
            peak_power = max(peak_power, power_data["total_power"])

            hourly_consumption.append(
                {
                    "hour": hour,
                    "temperature": temp,
                    "power": power_data["total_power"],
                    "energy": hourly_energy,
                }
            )

        # Calculate costs
        daily_cost = total_energy * self.electricity_rate

        return {
            "total_energy": total_energy,
            "peak_power": peak_power,
            "daily_cost": daily_cost,
            "hourly_data": hourly_consumption,
        }

    # TODO Implement seasonal performance calculations
    # def calculate_seasonal_performance(self, seasonal_temps, mode="heating")

    def plot_energy_consumption(self, daily_consumption):
        """
        Visualize daily energy consumption patterns
        :param daily_consumption: Daily consumption data
        """

        hours = [data["hour"] for data in daily_consumption["hourly_data"]]
        power = [data["power"] for data in daily_consumption["hourly_data"]]
        temps = [data["temperature"] for data in daily_consumption["hourly_data"]]

        df_energy_consumption = pl.DataFrame(
            data={"Hour of Day": hours, "Power (kW)": power, "Temperature (°C)": temps}
        )

        # Create plots

        # Power consumption plot
        pc_plot = px.line(
            data_frame=df_energy_consumption,
            x="Hour of Day",
            y="Power (kW)",
            title="Daily Power Consumption Profile",
        )
        pc_plot.show()

        # Temperature plot
        temp_plot = px.line(
            data_frame=df_energy_consumption,
            x="Hour of Day",
            y="Temperature (°C)",
            title="Daily Temperature Profile",
        )
        temp_plot.show()


if __name__ == "__main__":
    # create heat pump instance
    heat_pump = HeatPump()
    heating_performance = heat_pump.performance_map()
    heat_pump.visualize_performance(heating_performance)
    # Example daily temperature profile
    daily_temps = [5, 4, 3, 2, 1, 0, 1, 2, 4, 6, 8, 10, 
                  12, 13, 14, 13, 12, 10, 8, 7, 6, 5, 4, 3]

    # Calculate daily consumption
    daily_data = heat_pump.calculate_daily_consumption(daily_temps, mode='heating')
    heat_pump.plot_energy_consumption(daily_data)
