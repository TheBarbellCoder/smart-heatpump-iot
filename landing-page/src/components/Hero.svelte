<script lang="js">
  import { clsx } from 'clsx';

  let { class: className } = $props();
</script>

<div class="flex h-[90vh] flex-col items-center justify-center p-6 xl:px-8">
  <div
    class={clsx(
      className,
      `flex flex-col items-center justify-center gap-7 md:w-[640px] lg:w-[768px] xl:w-[1024px]`
    )}
  >
    <div class="self-start font-bold tracking-wide uppercase lg:text-xl dark:text-gray-200">
      Cut Design Time by 50%
    </div>
    <div
      class="self-start text-4xl font-semibold tracking-wide md:text-5xl lg:text-6xl xl:text-7xl dark:text-gray-200"
    >
      Stop Wasting Hours on Heat Pump Designs
    </div>
    <div
      class="self-start text-2xl font-light tracking-wide text-gray-800 lg:text-3xl dark:text-gray-200"
    >
      Simulate and optimize systems with precision—no guesswork. Built for HVAC pros and engineers.
    </div>
  </div>
</div>
