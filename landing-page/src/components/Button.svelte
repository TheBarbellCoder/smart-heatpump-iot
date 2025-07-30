<script lang="js">
  import { clsx } from 'clsx';
  let { class: className, children } = $props();
</script>

<button
  class={clsx(
    className,
    `text-button-14-medium lg:text-button-16-medium font-geist-sans rounded-full p-3`
  )}>{@render children()}</button
>
