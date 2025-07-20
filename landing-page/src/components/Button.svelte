<script lang="js">
  import { clsx } from 'clsx';
  let { class: className, children } = $props();
</script>

<button
  class={clsx(
    className,
    `text-button-14 lg:text-button-16 font-geist-sans inline-flex rounded-full p-3`
  )}>{@render children()}</button
>
