<script>
  import "../app.css";
  import { setContext } from "svelte";
  import IconContext from "phosphor-svelte/lib/IconContext";
  import Thermometer from "phosphor-svelte/lib/Thermometer";
  import { Button } from "$lib/components/ui/button";
  import { Switch } from "$lib/components/ui/switch";
  import { Label } from "$lib/components/ui/label";

  let isChecked = $state(false);
  let isSimulated = $state(true);

  setContext("systemState", {
    getOnOffState: () => isChecked,
    setOnOffState: (value) => isChecked = value,
    toggleOnOffState: () => isChecked = !isChecked,

    getSimulationState: () => isSimulated,
    setSimulationState: (value) => isSimulated = value,
    toggleSimulationState: () => isSimulated = !isSimulated,
  });

  let { children } = $props();
</script>

<div class="sticky flex justify-between items-center p-2 border-b box-border shadow-sx">
  <div class="flex items-center gap-4">
    <Thermometer weight="fill" size="32" />
    <div class="text-lg font-medium">
      Heatpump {isSimulated ? "Simulator" : "Dashboard"}
    </div>
  </div>
  <div class="flex items-center gap-y-4 gap-x-6">
    <div class="flex items-center gap-x-2">
      <Switch bind:checked={isChecked} />
      <Label for="system-state">{isChecked ? "System On" : "System Off"}</Label>
    </div>
    <Button variant="outline" disabled={!isSimulated}
    >Restart Simulation</Button>
  </div>
</div>

{@render children()}
