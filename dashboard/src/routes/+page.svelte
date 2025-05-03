<script>
  import { getContext } from "svelte";
  import * as Card from "$lib/components/ui/card";
  import { Badge } from "$lib/components/ui/badge";
  import { ThermometerSimple, Fire, Snowflake, Lightning, Park, CaretDown, CaretUp } from "phosphor-svelte"

  const systemState = getContext("systemState");

  let targetTemp = 19;  // °C
  let currentTemp = 20; // °C
  let outdoorTemp = 21; // °C
  let deltaTemp = targetTemp - currentTemp;

  const opModes = {op1: "Heating", op2: "Cooling", op3: "Fan"};
  let currentMode = outdoorTemp < targetTemp ? "op1" : outdoorTemp > targetTemp ? "op2" : "op3";

  let cop = 0.1;
  let currentEnergyConsumed = 1; // kW

  // $effect(()=>{console.log(systemState.get());});
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
        {:else}
          <Snowflake color="#9a9996" weight="duotone" size=20 />
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
          <div>
            <div class="flex items-baseline p-2 gap-x-1">
              <div class="text-5xl font-medium text-primary">{ currentTemp }</div>
              <div class="text-lg text-primary font-light">&deg;C</div>
            </div>
            <div class="flex px-2 gap-x-1">
            {#if deltaTemp > 0}
              <CaretUp />
              <span>{ deltaTemp }&deg;C from target</span> 
            {:else if deltaTemp < 0}
              <CaretDown />
              <span>{ deltaTemp }&deg;C from target</span> 
            {:else}
              <span>{ deltaTemp }&deg;C from target</span> 
            {/if}
          </div>
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
          <div>
            <div class="flex items-baseline p-2 gap-x-1">
              <div class="text-5xl font-medium text-primary">{ outdoorTemp }</div>
              <div class="text-lg text-primary font-light">&deg;C</div>
            </div>
            <div>{ systemState.getSimulationState() ? "Simulated environment": "Current temperature" }</div>
          </div>
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
          <div>
            <div class="flex items-baseline p-2 gap-x-1">
              <div class="text-5xl font-medium text-primary">{ currentEnergyConsumed }</div>
              <div class="text-lg text-primary font-light">kW</div>
            </div>
            <div class="px-2">COP: { cop }</div>
          </div>
        </Card.Description> 
      </Card.Header>
    </Card.Root>
  </Card.Content>
</Card.Root>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
