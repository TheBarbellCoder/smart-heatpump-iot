<script>
  import { getContext } from "svelte";
  import * as Card from "$lib/components/ui/card";
  import { Badge } from "$lib/components/ui/badge";
  import { ThermometerSimple, Fire, Snowflake, Lightning, Park } from "phosphor-svelte"

  const systemState = getContext("systemState");
  const opModes = {op1: "Heating", op2: "Cooling"};
  let currentMode = "op1";

  // $effect(()=>{console.log(systemState.get());});
</script>

<Card.Root class="flex-row p-2 m-6 shadow-xs">
  <Card.Header class="flex-row justify-between w-full items-center p-2 box-border">
    <div class="flex-row">
      <Card.Title class="text-xl font-medium">System Overview</Card.Title>
      <Card.Description class="text-base">Current heatpump perfomance and status</Card.Description>
    </div>
    <div class="flex gap-x-2 box-border">
      <Badge variant={ systemState.get() ? "default" :"secondary" } class="text-sm font-medium">{ systemState.get() ? "Running" :"Offline" }</Badge>
      <Badge variant="outline" class="flex gap-x-1 text-sm font-medium">
        {#if opModes[currentMode] === "Heating"}
          <Fire color="#aa201f" weight="duotone" size=20 />
        {:else}
          <Snowflake color="#9a9996" weight="duotone" size=20 />
        {/if}
        {opModes[currentMode]}</Badge>
    </div>
  </Card.Header>
  <Card.Content class="flex gap-x-6">
    <Card.Root class="w-full shadow-2xs">
      <Card.Header>
        <div class="flex gap-x-1 items-center">
          <ThermometerSimple color="#0b6c89" weight="duotone" size=24 />
          <Card.Title class="text-base font-normal">Indoor Temperature</Card.Title>
        </div>
        <Card.Description></Card.Description> 
      </Card.Header>
    </Card.Root>
    <Card.Root class="w-full shadow-2xs">
      <Card.Header>
        <div class="flex gap-x-1 items-center">
          <Park color="#ba6e13" weight="duotone" size=24 />
          <Card.Title class="text-base font-normal">Outdoor Temperature</Card.Title>
        </div>
        <Card.Description></Card.Description> 
      </Card.Header>
    </Card.Root>
    <Card.Root class="w-full shadow-2xs">
      <Card.Header>
        <div class="flex gap-x-1 items-center">
          <Lightning color="#5515c9" weight="duotone" size=24 />
          <Card.Title class="text-base font-normal">Energy Consumption</Card.Title>
        </div>
        <Card.Description></Card.Description> 
      </Card.Header>
    </Card.Root>

  </Card.Content>
  
</Card.Root>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
