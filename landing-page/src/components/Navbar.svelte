<script lang="js">
  import Button from './Button.svelte';
  import ToggleTheme from './ToggleTheme.svelte';
</script>

<div
  class="bg-default border-b-border-hover fixed top-0 z-50 container box-border flex w-full items-center justify-between border-b p-6 lg:p-8
"
>
  <a
    href="/"
    aria-label="Go to homepage"
    class="text-foreground-primary inline-flex items-center justify-center gap-3"
  >
    <svg viewBox="0 0 16 16" x mlns="http://www.w3.org/2000/svg" class="h-6 w-6" aria-hidden="true">
      <g clip-path="url(#clip0_6_138)">
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M8 1.33333C8.59393 4.7391 11.2609 7.40607 14.6667 8C11.2609 8.59393 8.59393 11.2609 8 14.6667C7.40607 11.2609 4.7391 8.59393 1.33333 8C4.7391 7.40607 7.40607 4.7391 8 1.33333V1.33333Z"
          fill="currentColor"
        />
      </g>
      <defs>
        <clipPath id="clip0_6_138">
          <rect width="16" height="16" fill="white" />
        </clipPath>
      </defs>
    </svg>
    <div class="font-geist-sans text-subheading-20-medium lg:text-subheading-32-medium">
      ThermaSim
    </div>
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
