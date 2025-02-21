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

    def __init__(self, refrigerant="R410A"):
        """
        Advanced Heat Pump Simulation with Detailed Thermodynamic Modeling

        :param refrigerant: Type of refrigerant used in the system
        """

        # System parameters
        self.refrigerant = refrigerant
        self.mass_flow_rate = 0.05  # kg/s
        self.compressor_efficiency = 0.85
        self.heat_exchanger_efficiency = 0.75

        self.target_temp = None
        self.heat_output = None
        self.cooling_rate = None
        self.compressor_on = False

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

    def simulate_thermodynamic_cycle(self, mode="heating", source_temp=5, sink_temp=20):
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

        # Heat transfer calculations
        if mode == "heating":
            # Heat is absorbed from source
            q_evaporator = (
                self.mass_flow_rate
                * props["specific_heat_capacity_liquid"]
                * (sink_temp_k - source_temp_k)
            )

            # Work input to compressor
            w_compressor = q_evaporator / cop

            # Heat realease to the sink
            q_condensor = q_evaporator + w_compressor
        else:  # cooling mode
            # Calculations similar to heating but reversed for cooling

            # Heat rejected to the sink
            q_condensor = (
                self.mass_flow_rate
                * props["specific_heat_capacity_gas"]
                * (sink_temp_k - source_temp)
            )

            # Work input to compressor
            w_compressor = q_condensor / cop

            # Heat absorbed from source
            q_evaporator = q_condensor - w_compressor

            # TODO Missing return!!
