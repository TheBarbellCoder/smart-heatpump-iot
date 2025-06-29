<script lang="js">
  import { getContext } from 'svelte';
  import { Slider } from 'bits-ui';
  import cn from 'clsx';
  import { CaretDown, CaretUp, Fan, Fire, Lightning, Minus, Park, Snowflake, ThermometerSimple } from 'phosphor-svelte';
  import TimeSeriesChart from '../components/TimeSeriesChart.svelte';

  const systemState = getContext('systemState');

  let targetTemp = $state(19); // °C
  let currentTemp = $state(19); // °C
  let outdoorTemp = $state(21); // °C
  let deltaTemp = $derived(targetTemp - currentTemp);

  const opModes = { op1: 'Heating', op2: 'Cooling', op3: 'Fan' };
  let currentMode = $derived(outdoorTemp < targetTemp ? 'op1' : outdoorTemp > targetTemp ? 'op2' : 'op3');

  let cop = $state(0.1);
  let energyConsumed = $state(1); // kW
  let compressorSpeed = $state(3000);
  let fanSpeed = $state(1500);
  let refrigerantPressure = $state(120);
  let refrigerantTemperature = $state(45);
  let defrostCycle = $state('Active');
  let flowRate = $state(13.0);
  let defrost = $state(false);

  const temperatureData = Array.from({ length: 24 }, (_, i) => {
    const date = new Date();
    date.setHours(date.getHours() - (23 - i));
    return {
      date: date,
      value: 42 + Math.sin(i * 0.3) * 8 + Math.random() * 2,
    };
  });
</script>

<!-- System Overview section -->
<div class="flex flex-col px-3 mt-12 mb-6 mr-6 ml-6 box-border items-start">
  <div class="flex w-full justify-between">
    <div class="text-lg font-semibold tracking-tight">System Overview</div>
    <div class="flex gap-x-3 box-border justify-center items-center">
      <div
        class="
          text-sm font-semibold border box-border px-3 py-1 rounded-15px
          {systemState.getOnOffState()
          ? 'bg-dark text-background'
          : 'bg-muted text-muted-foreground border-muted-foreground'}
        "
      >
        {systemState.getOnOffState() ? 'Running' : 'Offline'}
      </div>
      <div class="flex gap-x-1 text-sm font-semibold box-border border border-muted-foreground rounded-15px px-3 py-1">
        {#if opModes[currentMode] === 'Heating'}
          <Fire weight="fill" size="20" />
        {:else if opModes[currentMode] === 'Cooling'}
          <Snowflake weight="bold" size="20" />
        {:else}
          <Fan weight="fill" size="20" />
        {/if}
        {opModes[currentMode]}
      </div>
    </div>
  </div>
  <div class="text-sm text-foreground/50 font-semibold">Current heatpump performance and status</div>

  <!-- Cards -->
  <div class="flex w-full my-6 gap-6 justify-between items-center">
    <!-- Indoor Temperature Card -->
    <div class="flex flex-col w-full p-3 box-border border rounded-card-sm">
      <div class="flex gap-x-1 items-center">
        <ThermometerSimple weight="regular" size="24" />
        <div class="font-medium">Indoor Temperature</div>
      </div>
      <div class="flex items-baseline p-3 gap-x-1">
        <span class="text-6xl font-medium text-primary">{currentTemp}</span>
        <span class="text-lg text-primary font-light">&deg;C</span>
      </div>
      <div class="flex px-3 gap-x-1 items-center">
        {#if deltaTemp > 0}
          <CaretUp weight="bold" />
          <span class="text-sm text-foreground/70"
            >{Math.abs(deltaTemp)}
            &deg;C to target</span
          >
        {:else if deltaTemp < 0}
          <CaretDown weight="bold" />
          <span class="text-sm text-foreground/70"
            >{Math.abs(deltaTemp)}
            &deg;C from target</span
          >
        {:else}
          <Minus weight="bold" />
          <span class="text-sm text-foreground/70">At target temperature</span>
        {/if}
      </div>
    </div>

    <!-- Outdoor Temperature Card -->
    <div class="flex flex-col w-full p-3 box-border border rounded-card-sm">
      <div class="flex gap-x-1 items-center">
        <Park weight="regular" size="24" />
        <div class="font-medium">Outdoor Temperature</div>
      </div>
      <div class="flex items-baseline p-3 gap-x-1">
        <span class="text-6xl font-medium text-primary">{outdoorTemp}</span>
        <span class="text-lg text-primary font-light">&deg;C</span>
      </div>
      <div class="flex px-3 gap-x-1 items-center">
        <div Class="text-sm text-foreground/70">
          {systemState.getSimulationState() ? 'Simulated environment' : 'Current temperature'}
        </div>
      </div>
    </div>

    <!-- Energy Consumption Card -->
    <div class="flex flex-col w-full p-3 box-border border rounded-card-sm">
      <div class="flex gap-x-1 items-center">
        <Lightning weight="regular" size="24" />
        <div class="font-medium">Energy Consumption</div>
      </div>
      <div class="flex items-baseline p-3 gap-x-1">
        <span class="text-6xl font-medium text-primary">{energyConsumed}</span>
        <span class="text-lg text-primary font-light">kW</span>
      </div>
      <div class="flex px-3 gap-x-1 items-center">
        <div Class="text-sm text-foreground/70">
          COP: {cop}
        </div>
      </div>
    </div>
  </div>
</div>

<div class="flex m-6 gap-6 box-border">
  <div class="flex flex-col w-2/3 gap-12 box-border">
    <!-- Temperature Control section -->
    <div class="flex flex-col p-3 border rounded-card-sm box-border items-start">
      <div class="text-lg font-semibold tracking-tight">Temperature Control</div>
      <div class="flex flex-col w-full box-border justify-start items-end">
        <!-- Slider for outdoor temperature setting -->
        <div class="flex gap-x-3 h-7 justify-end items-center">
          <div class="text-sm text-foreground/50 font-semibold w-[210px]">
            Outdoor Temperature: <span class="text-foreground/70 font-bold"
              >{outdoorTemp}
              &deg; C</span
            >
          </div>
          <Snowflake weight="bold" size="20" />
          <Slider.Root
            type="single"
            bind:value={outdoorTemp}
            min={-20}
            max={42}
            step={0.5}
            class="relative flex w-[200px] touch-none select-none items-center"
          >
            <span class="bg-dark-10 relative h-2 w-[200px] cursor-pointer overflow-hidden rounded-full">
              <Slider.Range class="bg-foreground absolute h-full" />
            </span>
            <Slider.Thumb
              index={0}
              class={cn(
                'border-border-input bg-background hover:border-dark-40 focus-visible:ring-foreground dark:bg-foreground dark:shadow-card focus-visible:outline-hidden data-active:scale-[0.98] data-active:border-dark-40 block size-[23px] cursor-pointer rounded-full border shadow-sm transition-colors focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50'
              )}
            />
          </Slider.Root>
          <Fire weight="bold" size="20" />
        </div>

        <!-- Slider for indoor temperature setting -->
        <div class="flex gap-x-3 h-7 justify-end items-center">
          <div class="text-sm text-foreground/50 font-semibold w-[210px]">
            Indoor Temperature: <span class="text-foreground/70 font-bold"
              >{targetTemp}
              &deg; C</span
            >
          </div>
          <Snowflake weight="bold" size="20" />
          <Slider.Root
            type="single"
            bind:value={targetTemp}
            min={18}
            max={22}
            step={0.5}
            class="relative flex w-[200px] touch-none select-none items-center"
          >
            <span class="bg-dark-10 relative h-2 w-[200px] cursor-pointer overflow-hidden rounded-full">
              <Slider.Range class="bg-foreground absolute h-full" />
            </span>
            <Slider.Thumb
              index={0}
              class={cn(
                'border-border-input bg-background hover:border-dark-40 focus-visible:ring-foreground dark:bg-foreground dark:shadow-card focus-visible:outline-hidden data-active:scale-[0.98] data-active:border-dark-40 block size-[23px] cursor-pointer rounded-full border shadow-sm transition-colors focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50'
              )}
            />
          </Slider.Root>
          <Fire weight="bold" size="20" />
        </div>
      </div>

      <!-- Temperature Chart -->
      <TimeSeriesChart data={temperatureData} class="w-full h-[300px]" />
    </div>

    <!-- Energy Consumption Section -->
    <div class="flex flex-col p-3 border rounded-card-sm box-border items-start">
      <div class="text-lg font-semibold tracking-tight">Energy Consumption</div>
      <!-- Energy Chart -->
      <TimeSeriesChart data={temperatureData} class="w-full h-[300px] mt-[56px]" />
    </div>
  </div>

  <!-- System Properties -->
  <div class="flex flex-col w-1/3 p-3 box-border">
    <div class="text-lg font-semibold tracking-tight">System Properties</div>
    <div class=" grid grid-cols-2 gap-y-4 my-6 box-border">
      <div class="box-border border-b-2">
        <div class="text-foreground/50 font-semibold text-sm tracking-wide">Compressor Speed</div>
        <div>
          {compressorSpeed}
          <span
            class="text-xs tracking-wider font-medium text-foreground/80
">RPM</span
          >
        </div>
      </div>
      <div class="box-border border-b-2 pb-4">
        <div class="text-foreground/50 font-semibold text-sm tracking-wide">Fan Speed</div>
        <div>{fanSpeed} <span class="text-xs tracking-wider font-medium text-foreground/80">RPM</span></div>
      </div>
      <div class="box-border border-b-2 pb-4">
        <div class="text-foreground/50 font-semibold text-sm tracking-wide">Refrigerant Pressure</div>
        <div>{refrigerantPressure} <span class="text-xs tracking-wider font-medium text-foreground/80">PSI</span></div>
      </div>
      <div class="box-border border-b-2 pb-4">
        <div class="text-foreground/50 font-semibold text-sm tracking-wide">Refrigerant Temperature</div>
        <div>
          {refrigerantTemperature} <span class="text-xs tracking-wider font-medium text-foreground/80">&deg;C</span>
        </div>
      </div>
      <div class="box-border border-b-2 pb-4">
        <div class="text-foreground/50 font-semibold text-sm tracking-wide">Defrost Cycle</div>
        <div>{defrost ? 'Active' : 'Inactive'}</div>
      </div>
      <div class="box-border border-b-2 pb-4">
        <div class="text-foreground/50 font-semibold text-sm tracking-wide">Flow Rate</div>
        <div>{flowRate} <span class="text-xs tracking-wider font-medium text-foreground/80">L/min</span></div>
      </div>
    </div>
    <!-- TODO Continue here -->
  </div>
</div>

<h1>Welcome to SvelteKit</h1>
<p>
  Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation
</p>
