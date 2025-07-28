<script lang="js">
  import { Target, Lightning, Sliders, ChartLine } from 'phosphor-svelte';
</script>

<div
  class="box-border flex h-auto min-h-[90vh] flex-col items-center justify-center gap-14 p-6 lg:p-8"
>
  <div class="flex flex-col items-start justify-center gap-7 landscape:items-center">
    <div
      class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold text-foreground-primary font-geist-sans uppercase"
    >
      Transform Your Workflow
    </div>
    <div
      class="text-heading-40 md:text-heading-48 lg:text-heading-56 text-foreground-primary font-geist-sans text-start landscape:text-center"
    >
      Design Smarter, Not Harder
    </div>
  </div>

  <!-- Features -->
  <!-- Feature: Pinpoint Accuracy -->
  <div class="grid grid-cols-1 gap-7 lg:w-5xl lg:grid-cols-2 xl:w-6xl 2xl:gap-y-21">
    <div
      class="items-top bg-component-default flex justify-start gap-5 rounded-3xl p-6 lg:p-8 landscape:items-center"
    >
      <Target
        size="2em"
        weight="duotone"
        class="text-foreground-primary text-3xl landscape:text-lg"
      />
      <div
        class="text-foreground-primary text-copy-16-light md:text-copy-18-light lg:text-copy-20-light"
      >
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold"
          >Pinpoint Accuracy.</span
        >
        Simulate with 99% precision—no manual math needed.
      </div>
    </div>

    <!-- Feature: Lightning Fast -->
    <div
      class="items-top bg-component-default flex justify-start gap-5 rounded-3xl p-6 lg:p-8 landscape:items-center"
    >
      <Lightning
        size="2em"
        weight="duotone"
        class="text-foreground-primary text-3xl landscape:text-lg"
      />
      <div
        class="text-foreground-primary text-copy-16-light md:text-copy-18-light lg:text-copy-20-light"
      >
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Lightning Fast.</span
        >
        Cut design time by up to 50% with automated tools.
      </div>
    </div>

    <!-- Feature: Fully Customizable -->
    <div
      class="items-top bg-component-default flex justify-start gap-5 rounded-3xl p-6 lg:p-8 landscape:items-center"
    >
      <Sliders
        size="2em"
        weight="duotone"
        class="text-foreground-primary text-3xl landscape:text-lg"
      />
      <div
        class="text-foreground-primary text-copy-16-light md:text-copy-18-light lg:text-copy-20-light"
      >
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Fully Customizable.</span
        >
        Tweak refrigerants and settings to fit your project.
      </div>
    </div>

    <!-- Feature: Instant Insights -->
    <div
      class="items-top bg-component-default flex justify-start gap-5 rounded-3xl p-6 lg:p-8 landscape:items-center"
    >
      <ChartLine
        size="2em"
        weight="duotone"
        class="text-foreground-primary text-3xl landscape:text-lg"
      />
      <div
        class="text-foreground-primary text-copy-16-light md:text-copy-18-light lg:text-copy-20-light
"
      >
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Instant Insights.
        </span> Visualize CoP, energy use, and more in real-time.
      </div>
    </div>
  </div>
</div>
