<script lang="js">
  import Button from './Button.svelte';
  import ToggleTheme from './ToggleTheme.svelte';
</script>

<div
  class="fixed top-0 container box-border flex w-full items-center justify-between p-6 lg:px-8
"
>
  <img
    class="h-8 w-auto"
    src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=gray&shade=50"
    alt=""
  />
  <!-- Add menu items here-->
  <div class="flex items-center justify-center gap-6">
    <ToggleTheme />
    <Button
      class="bg-button-default hover:bg-button-hover active:bg-button-active text-color-secondary hover:text-color-default active:text-color-default"
      >Join the Waitlist
    </Button>
  </div>
</div>
