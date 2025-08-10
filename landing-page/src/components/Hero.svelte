<script lang="js">
  import { theme } from '$lib/stores/theme.svelte.js';
  import Button from './Button.svelte';
</script>

<div
  class="mt-24 box-border flex flex-col items-center justify-center gap-12 p-6 py-[100px] lg:mt-28 lg:p-8 lg:py-[100px]"
>
  <div class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold uppercase">
    No More Slow Design Cycles
  </div>
  <div class="text-heading-48 md:text-heading-64 lg:text-heading-72 text-start md:text-center">
    Simplify Heat Pump Design with Precision
  </div>

  <div
    class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium text-foreground-secondary font-geist-sans md:text-center"
  >
    ThermaSim streamlines complex calculations for fast and accurate designs &mdash; tailored to
    HVAC pros and engineers.
  </div>
  <div class="flex gap-7 self-start md:self-center">
    <Button
      url="/waitlist"
      class="bg-component-default hover:bg-component-hover active:bg-component-active rounded-full p-3"
      >Join the Waitlist
    </Button>
  </div>
</div>

<!-- Placeholder for the simulator image -->
<div
  class="container box-border flex aspect-square items-center justify-center rounded-lg p-6 py-[100px] lg:p-8 lg:py-[100px] landscape:aspect-video"
>
  <!-- Light mode image -->
  {#if theme.isLight}
    <img src="/ThermaSim-Light.png" alt="Simulator" class="rounded-lg" />
    <!-- Dark mode image -->
  {:else}
    <img src="/ThermaSim-Dark.png" alt="Simulator (dark)" class="rounded-lg" />
  {/if}
</div>
