<script lang="js">
  import { page } from '$app/stores';
  import Button from './Button.svelte';

  // Change Privacy-policy link based on the current page
  const isPrivacyPage = $derived($page.url.pathname === '/privacy');
</script>

<div
  class="border-t-border-hover box-border flex items-center justify-end gap-14 border-t p-6 pt-[50px] pb-[100px] lg:p-8 lg:pt-[50px] lg:pb-[100px]"
>
  <div class="flex gap-3">
    <Button
      url="/privacy"
      class="hover:text-foreground-primary {isPrivacyPage
        ? 'hidden'
        : 'inline-block'} active:text-foreground-primary
      text-copy-16-light text-foreground-secondary underline underline-offset-6 transition-colors duration-300"
      >Privacy Policy</Button
    >
  </div>
</div>
