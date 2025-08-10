<script lang="js">
  import { Sun, Moon } from 'phosphor-svelte';
  import { theme } from '$lib/stores/theme.svelte.js';
  // import { onMount } from 'svelte';

  // let darkMode = $state(false);
  // function toggleTheme() {
  //   darkMode = !darkMode;
  //   updateTheme();
  // }
  // export function getTheme() {
  //   return darkMode;
  // }

  // function updateTheme() {
  //   if (darkMode) {
  //     document.documentElement.classList.add('dark');
  //     localStorage.setItem('themeSvelte', 'dark');
  //   } else {
  //     document.documentElement.classList.remove('dark');
  //     localStorage.setItem('themeSvelte', 'light');
  //   }
  // }

  // onMount(() => {
  //   const savedTheme = localStorage.getItem('themeSvelte');
  //   const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  //
  //   darkMode = savedTheme === 'dark' || prefersDark;
  //   updateTheme();
  // });
</script>

<button
  onclick={() => {
    theme.toggle();
  }}
  class="hover:bg-component-hover active:bg-component-active inline-flex h-10 w-10
  items-center justify-center rounded-full transition-colors duration-300"
  aria-label="Toggle Theme"
>
  {#if theme.isDark}
    <Sun class="h-6 w-6" />
  {:else}
    <Moon class="h-6 w-6" />
  {/if}
</button>
