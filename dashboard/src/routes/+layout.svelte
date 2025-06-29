<script>
  import '../app.css';

  import { setContext } from 'svelte';
  import IconContext from 'phosphor-svelte/lib/IconContext';
  import { Thermometer } from 'phosphor-svelte';
  import { Button, Label, Switch } from 'bits-ui';

  let isChecked = $state(false);
  let isSimulated = $state(true);

  setContext('systemState', {
    getOnOffState: () => isChecked,
    setOnOffState: (value) => (isChecked = value),
    toggleOnOffState: () => (isChecked = !isChecked),

    getSimulationState: () => isSimulated,
    setSimulationState: (value) => (isSimulated = value),
    toggleSimulationState: () => (isSimulated = !isSimulated),
  });

  let { children } = $props();
</script>

<div class="sticky flex justify-between items-center p-3 border-b box-border shadow-sx">
  <div class="flex items-center gap-4">
    <Thermometer weight="fill" size="32" />
    <div class="text-xl tracking-tight font-bold">
      Heatpump {isSimulated ? 'Simulator' : 'Dashboard'}
    </div>
  </div>
  <div class="flex items-center gap-y-4 gap-x-6">
    <div class="flex items-center gap-x-2">
      <Switch.Root
        id="on-off"
        bind:checked={isChecked}
        class="
          focus-visible:ring-foreground focus-visible:ring-offset-background
          data-[state=checked]:bg-foreground data-[state=unchecked]:bg-dark-10
          data-[state=unchecked]:shadow-mini-inset dark:data-[state=checked]:bg-foreground
          focus-visible:outline-hidden peer inline-flex h-[31px] min-h-[31px] w-[54px]
          shrink-0 cursor-pointer items-center rounded-full px-[3px] transition-colors
          focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed
          disabled:opacity-50
        "
      >
        <Switch.Thumb
          class="
            bg-background data-[state=unchecked]:shadow-mini dark:border-background/30
            dark:bg-foreground dark:shadow-popover pointer-events-none block size-[24px]
            shrink-0 rounded-full transition-transform data-[state=checked]:translate-x-6
            data-[state=unchecked]:translate-x-0 dark:border
            dark:data-[state=unchecked]:border
          "
        />
      </Switch.Root>
      <Label.Root for="on-off" class="text-sm font-medium">{isChecked ? 'System On' : 'System Off'}</Label.Root>
    </div>
    <Button.Root
      class="
        rounded-input bg-dark text-background shadow-mini hover:bg-dark/95 inline-flex
        h-12 items-center justify-center px-[21px] text-[15px] font-semibold
        active:scale-[0.98] active:transition-all disabled:bg-muted
        disabled:text-muted-foreground
      "
      disabled={!isSimulated}>Restart Simulation</Button.Root
    >
  </div>
</div>

{@render children()}
