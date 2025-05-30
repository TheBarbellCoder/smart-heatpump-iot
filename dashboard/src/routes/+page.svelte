<script>
  import { getContext } from "svelte";
  import { AreaChart } from "layerchart";
  import { Slider } from "bits-ui";
  import cn from "clsx";
  import {
    CaretDown,
    CaretUp,
    Fan,
    Fire,
    Lightning,
    Minus,
    Park,
    Snowflake,
    ThermometerSimple,
  } from "phosphor-svelte";

  const systemState = getContext("systemState");

  let targetTemp = $state(19); // °C
  let currentTemp = $state(19); // °C
  let outdoorTemp = $state(21); // °C
  let deltaTemp = $derived(targetTemp - currentTemp);

  const opModes = { op1: "Heating", op2: "Cooling", op3: "Fan" };
  let currentMode = $derived(
    outdoorTemp < targetTemp
      ? "op1"
      : outdoorTemp > targetTemp
      ? "op2"
      : "op3",
  );

  let cop = 0.1;
  let currentEnergyConsumed = 1; // kW
</script>

<!-- System Overview section -->
<div class="flex-row p-3 m-6 border rounded-card-sm box-border items-center">
  <div class="flex justify-between">
    <div class="text-lg font-semibold tracking-tight">System Overview</div>
    <div class="flex gap-x-3 box-border justify-center items-center">
      <div
        class="
          text-sm font-semibold border box-border px-3 py-1 rounded-15px
          { systemState.getOnOffState()? 'bg-dark text-background' :
          'bg-muted text-muted-foreground border-muted-foreground' }
        "
      >
        {systemState.getOnOffState() ? "Running" : "Offline"}
      </div>
      <div class="flex gap-x-1 text-sm font-semibold box-border border border-muted-foreground rounded-15px px-3 py-1">
        {#if opModes[currentMode] === "Heating"}
          <Fire weight="fill" size="20" />
        {:else if opModes[currentMode] === "Cooling"}
          <Snowflake weight="bold" size="20" />
        {:else}
          <Fan weight="fill" size="20" />
        {/if}
        {opModes[currentMode]}
      </div>
    </div>
  </div>
  <div class="text-sm text-foreground/70 font-semibold">
    Current heatpump performance and status
  </div>

  <!-- Cards -->
  <div class="flex m-6 gap-6 justify-between items-center">
    <!-- Indoor Temperature Card -->
    <div class="flex-row w-full p-3 box-border border rounded-card-sm">
      <div class="flex gap-x-1 items-center">
        <ThermometerSimple weight="regular" size="24" />
        <div class="font-medium">Indoor Temperature</div>
      </div>
      <div class="flex items-baseline p-3 gap-x-1">
        <span class="text-6xl font-medium text-primary">{targetTemp}</span>
        <span class="text-lg text-primary font-light">&deg;C</span>
      </div>
      <div class="flex px-3 gap-x-1 items-center">
        {#if deltaTemp > 0}
          <CaretUp weight="bold" />
          <span class="text-sm text-foreground/70">{Math.abs(deltaTemp)}&deg;C
            to target</span>
        {:else if deltaTemp < 0}
          <CaretDown weight="bold" />
          <span class="text-sm text-foreground/70">{Math.abs(deltaTemp)}&deg;C
            from target</span>
        {:else}
          <Minus weight="bold" />
          <span class="text-sm text-foreground/70">At target temperature</span>
        {/if}
      </div>
    </div>

    <!-- Outdoor Temperature Card -->
    <div class="flex-row w-full p-3 box-border border rounded-card-sm">
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
          {
            systemState.getSimulationState()
            ? "Simulated environment"
            : "Current temperature"
          }
        </div>
      </div>
    </div>

    <!-- Energy Consumption Card -->
    <div class="flex-row w-full p-3 box-border border rounded-card-sm">
      <div class="flex gap-x-1 items-center">
        <Lightning weight="regular" size="24" />
        <div class="font-medium">Energy Consumption</div>
      </div>
      <div class="flex items-baseline p-3 gap-x-1">
        <span class="text-6xl font-medium text-primary">{
          currentEnergyConsumed
        }</span>
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

<!-- Temperature Control section -->
<div class="flex-row p-3 m-6 border rounded-card-sm box-border items-center">
  <div class="flex justify-between">
    <div class="text-lg font-semibold tracking-tight">Temperature Control</div>
    <div class="flex-row box-border justify-center items-center">
      <!-- Slider for outdoor temperature setting -->
      <div class="flex gap-x-3 h-7 justify-between items-center">
        <div class="text-sm text-foreground/70 font-semibold w-[210px]">
          Outdoor Temperature: {outdoorTemp}&deg;C
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
          <span
            class="bg-dark-10 relative h-2 w-[200px] cursor-pointer overflow-hidden rounded-full"
          >
            <Slider.Range class="bg-foreground absolute h-full" />
          </span>
          <Slider.Thumb
            index={0}
            class={cn(
              "border-border-input bg-background hover:border-dark-40 focus-visible:ring-foreground dark:bg-foreground dark:shadow-card focus-visible:outline-hidden data-active:scale-[0.98] data-active:border-dark-40 block size-[23px] cursor-pointer rounded-full border shadow-sm transition-colors focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
            )}
          />
        </Slider.Root>
        <Fire weight="bold" size="20" />
      </div>

      <!-- Slider for indoor temperature setting -->
      <div class="flex gap-x-3 h-7 justify-between items-center">
        <div class="text-sm text-foreground/70 font-semibold w-[210px]">
          Indoor Temperature: {targetTemp}&deg;C
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
          <span
            class="bg-dark-10 relative h-2 w-[200px] cursor-pointer overflow-hidden rounded-full"
          >
            <Slider.Range class="bg-foreground absolute h-full" />
          </span>
          <Slider.Thumb
            index={0}
            class={cn(
              "border-border-input bg-background hover:border-dark-40 focus-visible:ring-foreground dark:bg-foreground dark:shadow-card focus-visible:outline-hidden data-active:scale-[0.98] data-active:border-dark-40 block size-[23px] cursor-pointer rounded-full border shadow-sm transition-colors focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
            )}
          />
        </Slider.Root>
        <Fire weight="bold" size="20" />
      </div>
    </div>
  </div>
</div>

<h1>Welcome to SvelteKit</h1>
<p>
  Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read
  the documentation
</p>
