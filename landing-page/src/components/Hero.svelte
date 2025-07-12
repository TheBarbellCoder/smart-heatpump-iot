<script lang="js">
  import { ArrowRight } from 'phosphor-svelte';
  import { clsx } from 'clsx';
  import Button from './Button.svelte';

  let { class: className } = $props();
</script>

<div class="flex h-[85vh] flex-col items-center justify-center p-6 md:h-[75vh] xl:px-8">
  <div
    class={clsx(
      className,
      `flex flex-col items-center justify-center gap-7 md:w-[640px] lg:w-[768px] xl:w-[1024px]`
    )}
  >
    <div
      class="hidden font-medium tracking-wide text-indigo-600 uppercase lg:text-lg dark:text-gray-200"
    >
      Cut Design Time by 50%
    </div>
    <div
      class="text-center text-4xl font-semibold tracking-wide md:text-5xl lg:text-6xl xl:text-7xl dark:text-gray-200"
    >
      Stop Wasting Hours on Heat Pump Designs
    </div>
    <div
      class="text-center text-lg font-light tracking-wide text-gray-800 md:w-5/6 lg:text-xl xl:text-2xl dark:text-gray-200"
    >
      Simulate and optimize systems with precision—no guesswork. Built for HVAC pros and engineers.
    </div>
    <div class="flex gap-7">
      <Button variant="accent">Join the Waitlist</Button>
      <Button variant="clear" class="gap-1">
        <div>Learn more</div>
        <ArrowRight weight="regular" size="18" />
      </Button>
    </div>
  </div>
</div>

<!-- Placeholder for the simulator image -->
<div class="flex flex-col items-center justify-center p-6 xl:px-8">
  <div
    class={clsx(
      className,
      `h-[300px] flex-col items-center justify-center rounded-lg bg-gray-400 p-6 md:h-[500px] lg:h-[600px] xl:h-[800px] xl:px-8 dark:bg-indigo-300`
    )}
  ></div>
</div>
