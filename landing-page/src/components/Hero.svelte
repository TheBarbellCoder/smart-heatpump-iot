<script lang="js">
  import { ArrowRight } from 'phosphor-svelte';
  import Button from './Button.svelte';
</script>

<div
  class="box-border flex h-[90vh] flex-col items-center justify-center gap-14 p-6 pt-24 lg:p-8 lg:pt-24 landscape:h-auto landscape:pt-28 landscape:lg:h-[90vh]"
>
  <div class="flex flex-col items-start justify-center gap-7 2xl:items-center">
    <div
      class="text-copy-16 md:text-copy-18 lg:text-copy-20 text-foreground-primary font-geist-sans uppercase"
    >
      Cut Design Time by 50%
    </div>
    <div
      class="text-heading-48 md:text-heading-64 lg:text-heading-72 text-foreground-primary font-geist-sans 2xl:text-center"
    >
      Stop Struggling with Heat Pump Designs
    </div>
  </div>

  <div
    class="text-subheading-20 md:text-subheading-24 lg:text-subheading-32 text-foreground-secondary font-geist-sans"
  >
    Build and optimize systems faster with our Python-based simulator. Made for HVAC pros and
    engineers.
  </div>
  <div class="flex gap-7">
    <Button
      class="bg-button-default hover:bg-button-hover active:bg-button-active text-color-default"
      >Join the Waitlist
    </Button>
    <Button
      class="text-foreground-secondary hover:text-foreground-primary active:text-foreground-primary items-center justify-center gap-1"
    >
      <div>Learn more</div>
      <ArrowRight weight="regular" size="16" />
    </Button>
  </div>
</div>
