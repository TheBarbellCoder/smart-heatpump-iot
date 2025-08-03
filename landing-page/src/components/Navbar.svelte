<script lang="js">
  import Button from './Button.svelte';
  import ToggleTheme from './ToggleTheme.svelte';
</script>

<div
  class="bg-default border-b-border-hover fixed top-0 z-50 container box-border flex w-full items-center justify-between border-b p-6 lg:p-8
"
>
  <a href="/">
    <img
      class="h-8 w-auto"
      src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=gray&shade=50"
      alt=""
    />
  </a>

  <!-- Add menu items here-->
  <div class="flex items-center justify-center gap-6">
    <ToggleTheme />
    <Button
      url="/waitlist"
      class="bg-component-default  hover:bg-component-hover active:bg-component-active text-foreground-primary hidden rounded-full p-3 md:block"
      >Join the Waitlist
    </Button>
  </div>
</div>
