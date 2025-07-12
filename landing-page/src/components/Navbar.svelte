<script lang="js">
  import Button from './Button.svelte';
  import ToggleTheme from './ToggleTheme.svelte';
</script>

<div
  class="fixed top-0 flex w-full items-center justify-between p-6 lg:px-8
"
>
  <img
    class="h-8 w-auto"
    src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600"
    alt=""
  />
  <!-- Add menu items here-->
  <div class="flex items-center justify-center gap-x-5">
    <ToggleTheme />
    <Button variant="accent">Join the Waitlist</Button>
  </div>
</div>
