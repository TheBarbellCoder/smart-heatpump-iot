<script lang="js">
  import { ArrowRight } from 'phosphor-svelte';
  import { clsx } from 'clsx';
  import Button from './Button.svelte';

  let { class: className } = $props();
</script>

<div class="hero-container flex flex-col items-center justify-center p-6 xl:p-8">
  <div class={clsx(className, `flex flex-col items-center justify-center gap-7`)}>
    <div
      class="tablet:block hidden font-medium tracking-wide text-indigo-600 uppercase lg:text-lg dark:text-gray-200"
    >
      Cut Design Time by 50%
    </div>
    <div
      class="text-center text-4xl font-semibold tracking-wide md:text-5xl lg:text-6xl xl:text-7xl dark:text-gray-200"
    >
      Stop Struggling with Heat Pump Designs
    </div>
    <div
      class="text-center text-xl font-light tracking-wide text-gray-800 md:w-5/6 lg:text-2xl dark:text-gray-200"
    >
      Build and optimize systems faster with our Python-based simulator. Made for HVAC pros and
      engineers.
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
      `aspect-orientation flex-col items-center justify-center rounded-lg bg-gray-400 p-6 xl:px-8 dark:bg-indigo-300`
    )}
  ></div>
</div>
