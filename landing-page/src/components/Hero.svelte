<script lang="js">
  import { ArrowRight } from 'phosphor-svelte';
  import Button from './Button.svelte';
</script>

<div
  class="mt-24 box-border flex flex-col items-center justify-center gap-14 p-6 py-[100px] lg:mt-28 lg:p-8 lg:py-[100px]"
>
  <div class="flex flex-col items-start justify-center gap-7 md:items-center">
    <div class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold uppercase">
      No More Slow Design Cycles
    </div>
    <div class="text-heading-48 md:text-heading-64 lg:text-heading-72 text-start md:text-center">
      Simplify Heat Pump Design with Precision
    </div>
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
    <!--    <Button-->
    <!--      class="text-foreground-secondary hover:text-foreground-primary active:text-foreground-primary inline-flex items-center justify-center gap-1 rounded-full p-3"-->
    <!--    >-->
    <!--      <div>Learn more</div>-->
    <!--      <ArrowRight weight="regular" size="16" />-->
    <!--    </Button>-->
  </div>
</div>

<!-- Placeholder for the simulator image -->
<!-- TODO Change margins to padding once you insert the image -->
<div
  class="bg-foreground-secondary/50 container my-[100px] box-border aspect-square rounded-lg p-6 lg:my-[100px] lg:p-8 landscape:aspect-video"
></div>
