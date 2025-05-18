<script>
  import { getContext } from "svelte";
  import { AreaChart } from "layerchart";
  import * as Card from "$lib/components/ui/card";
  import { Badge } from "$lib/components/ui/badge";
  import { Slider } from "$lib/components/ui/slider";
  import { ThermometerSimple, Fire, Snowflake, Fan, Lightning, Park, CaretDown, CaretUp, Minus } from "phosphor-svelte"

  const systemState = getContext("systemState");

  let targetTemp = $state(19);  // °C
  let currentTemp = $state(19); // °C
  let outdoorTemp = $state(21); // °C
  // svelte-ignore state_referenced_locally
  // Make deltaTemp a $devrived() state
  let deltaTemp = $derived(targetTemp - currentTemp);

  const opModes = {op1: "Heating", op2: "Cooling", op3: "Fan"};
  let currentMode = $derived(outdoorTemp < targetTemp ? "op1" : outdoorTemp > targetTemp ? "op2" : "op3");

  let cop = 0.1;
  let currentEnergyConsumed = 1; // kW

</script>

<Card.Root class="flex-row p-2 m-6 shadow-xs" disabled={ !systemState.getOnOffState() }>
  <Card.Header class="flex-row justify-between w-full items-center p-2 box-border">
    <div class="flex-row">
      <Card.Title class="text-xl font-medium">System Overview</Card.Title>
      <Card.Description class="text-base">Current heatpump perfomance and status</Card.Description>
    </div>
    <div class="flex gap-x-2 box-border">
      <Badge variant={ systemState.getOnOffState() ? "default" :"secondary" } class="text-sm font-medium">{ systemState.getOnOffState() ? "Running" :"Offline" }</Badge>
      <Badge variant="outline" class="flex gap-x-1 text-sm font-medium">
        {#if opModes[currentMode] === "Heating"}
          <Fire color="#aa201f" weight="duotone" size=20 />
        {:else if opModes[currentMode] === "Cooling"}
          <Snowflake class="text-muted-foreground" weight="duotone" size=20 />
        {:else}
          <Fan class="text-muted-foreground" weight="fill" size=20 />
        {/if}
        { opModes[currentMode] }</Badge>
    </div>
  </Card.Header>
  <Card.Content class="flex gap-x-6">
    <Card.Root class="w-full shadow-2xs">
      <Card.Header>
        <div class="flex gap-x-1 items-center">
          <ThermometerSimple color="#0b6c89" weight="duotone" size=24 />
          <Card.Title class="text-base font-normal">Indoor Temperature</Card.Title>
        </div>
        <Card.Description>
          <span>
            <span class="flex items-baseline p-2 gap-x-1">
              <span class="text-5xl font-medium text-primary">{ currentTemp }</span>
              <span class="text-lg text-primary font-light">&deg;C</span>
            </span>
            <span class="flex px-2 gap-x-1 items-center">
            {#if deltaTemp > 0}
              <CaretUp color="#aa210f" weight="bold" />
              <span>{ Math.abs(deltaTemp) }&deg;C to target</span>
            {:else if deltaTemp < 0}
              <CaretDown color="#aa210f" weight="bold" />
              <span>{ Math.abs(deltaTemp) }&deg;C from target</span>
            {:else}
              <Minus color="#0b6c89" weight="bold" />
              <span>At target temperature</span>
            {/if}
          </span>
        </Card.Description> 
      </Card.Header>
    </Card.Root>
    <Card.Root class="w-full shadow-2xs">
      <Card.Header>
        <div class="flex gap-x-1 items-center">
          <Park color="#ba6e13" weight="duotone" size=24 />
          <Card.Title class="text-base font-normal">Outdoor Temperature</Card.Title>
        </div>
        <Card.Description>
          <span>
            <span class="flex items-baseline p-2 gap-x-1">
              <span class="text-5xl font-medium text-primary">{ outdoorTemp }</span>
              <span class="text-lg text-primary font-light">&deg;C</span>
            </span>
            <span>{ systemState.getSimulationState() ? "Simulated environment": "Current temperature" }</span>
          </span>
        </Card.Description> 
      </Card.Header>
    </Card.Root>
    <Card.Root class="w-full shadow-2xs">
      <Card.Header>
        <div class="flex gap-x-1 items-center">
          <Lightning color="#5515c9" weight="duotone" size=24 />
          <Card.Title class="text-base font-normal">Energy Consumption</Card.Title>
        </div>
        <Card.Description>
          <span>
            <span class="flex items-baseline p-2 gap-x-1">
              <span class="text-5xl font-medium text-primary">{ currentEnergyConsumed }</span>
              <span class="text-lg text-primary font-light">kW</span>
            </span>
            <span class="px-2">COP: { cop }</span>
          </span>
        </Card.Description> 
      </Card.Header>
    </Card.Root>
  </Card.Content>
</Card.Root>

<Card.Root class="flex-row p-2 m-6 shadow-xs" disabled={ !systemState.getOnOffState() }>
  <Card.Header class="flex-row justify-between w-full items-center p-2 box-border">
    <Card.Title class="text-xl font-medium">Temperature Control</Card.Title>
  </Card.Header>
  <Card.Description>
    <div class="flex-row px-2 w-1/4">
      <span class="flex justify-between items-center {systemState.getSimulationState()?'':'hidden'}">
        <span class="text-primary text-base">Outdoor Temperature: { outdoorTemp }&deg;C</span>
        <span class="flex gap-x-2">
          <Snowflake class="text-muted-foreground" weight="duotone" size=18 />
          <Slider value={ [outdoorTemp] } onValueChange={ (values) => outdoorTemp = values[0] } min={-20} max={42} step={0.5} class="w-xs" />
          <Fire color="#aa210f" weight="duotone" size=18 />
        </span>
      </span>
      <span class="flex justify-between items-center">
        <span class="text-primary text-base">Indoor Temperature: { targetTemp }&deg;C</span>
        <span class="flex gap-x-2">
          <Snowflake class="text-muted-foreground" weight="duotone" size=18 />
          <Slider value={ [targetTemp] } onValueChange={ (values) => targetTemp = values[0] } min={18} max={22} step={0.5} class="w-xs"/>
          <Fire color="#aa210f" weight="duotone" size=18 />
        </span>
      </span>
    </div>
  </Card.Description>
</Card.Root>
<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
