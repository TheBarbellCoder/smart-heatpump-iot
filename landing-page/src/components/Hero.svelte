<script lang="js">
  import { ArrowRight } from 'phosphor-svelte';
  import Button from './Button.svelte';
</script>

<div
  class="mt-24 box-border flex h-auto min-h-[90vh] flex-col items-center justify-center gap-14 p-6 lg:p-8"
>
  <div class="flex flex-col items-start justify-center gap-7 landscape:items-center">
    <div
      class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold text-foreground-primary font-geist-sans uppercase"
    >
      Cut Design Time by 50%
    </div>
    <div
      class="text-heading-48 md:text-heading-64 lg:text-heading-72 text-foreground-primary font-geist-sans text-start landscape:text-center"
    >
      Stop Struggling with Heat Pump Designs
    </div>
  </div>

  <div
    class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium text-foreground-secondary font-geist-sans landscape:text-center"
  >
    Build and optimize systems faster with our Python-based simulator. Made for HVAC pros and
    engineers.
  </div>
  <div class="flex gap-7 self-start landscape:self-center">
    <Button
      class="bg-component-default hover:bg-component-hover active:bg-component-active text-foreground-primary"
      >Join the Waitlist
    </Button>
    <Button
      class="text-foreground-secondary hover:text-foreground-primary active:text-foreground-primary items-center justify-center gap-1"
    >
      <div>Learn more</div>
      <ArrowRight weight="regular" size="16" />
    </Button>
  </div>
  <!-- Placeholder for the simulator image -->
  <div class="bg-foreground-secondary aspect-square w-full 2xl:hidden landscape:aspect-video"></div>
</div>

<!-- Placeholder for the simulator image -->
<div
  class="bg-foreground-secondary hidden aspect-square w-full p-6 lg:p-8 2xl:block landscape:aspect-video"
></div>
