<script lang="js">
  import { Target, Lightning, Sliders, ChartLine } from 'phosphor-svelte';
</script>

<div
  class="box-border flex flex-col items-center justify-center gap-14 p-6 py-[100px] lg:p-8 lg:py-[100px]"
>
  <div class="flex w-full flex-col items-start justify-center gap-7 md:items-center">
    <div class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold uppercase">
      Transform Your Workflow
    </div>
    <div class="text-heading-40 md:text-heading-48 lg:text-heading-56 text-start md:text-center">
      Design Smarter, Not Harder
    </div>
  </div>

  <!-- Features -->
  <!-- Feature: Pinpoint Accuracy -->
  <div class="container box-border grid grid-cols-1 gap-7 lg:grid-cols-2">
    <div
      class="bg-component-default box-border flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8"
    >
      <div class="flex h-6 w-6 items-center justify-center">
        <Target size={24} weight="duotone" class="" />
      </div>
      <div class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold"
          >Pinpoint Accuracy.</span
        >
        Simulate with 99% precision—no manual math needed.
      </div>
    </div>

    <!-- Feature: Lightning Fast -->
    <div class="bg-component-default flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8">
      <div class="flex h-6 w-6 items-center justify-center">
        <Lightning size={24} weight="duotone" class="" />
      </div>
      <div class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Lightning Fast.</span
        >
        Cut design time by up to 50% with automated tools.
      </div>
    </div>

    <!-- Feature: Fully Customizable -->
    <div class="bg-component-default flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8">
      <div class="flex h-6 w-6 items-center justify-center">
        <Sliders size={24} weight="duotone" class="" />
      </div>
      <div class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Fully Customizable.</span
        >
        Tweak refrigerants and settings to fit your project.
      </div>
    </div>

    <!-- Feature: Instant Insights -->
    <div class="bg-component-default flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8">
      <div class="flex h-6 w-6 items-center justify-center">
        <ChartLine size={26} weight="duotone" class="" />
      </div>
      <div
        class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light
"
      >
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Instant Insights.
        </span> Visualize CoP, energy use, and more in real-time.
      </div>
    </div>
  </div>
</div>
