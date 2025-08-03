<script lang="js">
  import { clsx } from 'clsx';

  let { class: className, url = '', children } = $props();
</script>

<a href={url}>
  <div class={clsx(className, `text-button-14-medium lg:text-button-16-medium font-geist-sans`)}>
    {@render children()}
  </div>
</a>
