<script lang="js">
  import { Target, Lightning, Sliders, ChartLine } from 'phosphor-svelte';
</script>

<div
  class="box-border flex flex-col items-center justify-center gap-14 p-6 py-[100px] lg:p-8 lg:py-[100px]"
>
  <div class="flex w-full flex-col items-start justify-center gap-7 md:items-center">
    <div class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold uppercase">
      Work Faster, Smarter
    </div>
    <div class="text-heading-40 md:text-heading-48 lg:text-heading-56 text-start md:text-center">
      Solve Design Challenges Effortlessly
    </div>
  </div>

  <!-- Features -->
  <!-- Feature: Accurate Simulations -->
  <div class="container box-border grid grid-cols-1 gap-7 lg:grid-cols-2">
    <div
      class="bg-component-default box-border flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8"
    >
      <div class="flex h-6 w-6 items-center justify-center">
        <Target size={24} weight="duotone" class="" />
      </div>
      <div class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold"
          >Accurate Simulations.</span
        >
        Achieve 99% accuracy without manual effort.
      </div>
    </div>

    <!-- Feature: Faster Workflow -->
    <div class="bg-component-default flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8">
      <div class="flex h-6 w-6 items-center justify-center">
        <Lightning size={24} weight="duotone" class="" />
      </div>
      <div class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Faster Workflow.</span
        >
        Cut design time by up to 50% with automated tools.
      </div>
    </div>

    <!-- Feature: Flexible Settings -->
    <div class="bg-component-default flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8">
      <div class="flex h-6 w-6 items-center justify-center">
        <Sliders size={24} weight="duotone" class="" />
      </div>
      <div class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Flexible Settings.</span
        >
        Customise refrigerants and parameters for any project.
      </div>
    </div>

    <!-- Feature: Clear Data -->
    <div class="bg-component-default flex items-center justify-start gap-5 rounded-3xl p-6 lg:p-8">
      <div class="flex h-6 w-6 items-center justify-center">
        <ChartLine size={26} weight="duotone" class="" />
      </div>
      <div
        class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light
"
      >
        <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold">
          Clear Data.
        </span>
        Access CoP and energy metrics instantly.
      </div>
    </div>
  </div>
</div>
