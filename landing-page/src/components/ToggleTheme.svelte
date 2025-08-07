<script lang="js">
  import { Sun, Moon } from 'phosphor-svelte';
  import { onMount } from 'svelte';

  let darkMode = $state(false);
  function toggleTheme() {
    darkMode = !darkMode;
    updateTheme();
  }

  function updateTheme() {
    if (darkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }

  onMount(() => {
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    darkMode = savedTheme === 'dark' || prefersDark;
    updateTheme();
  });
</script>

<button
  onclick={toggleTheme}
  class="hover:bg-component-hover active:bg-component-active inline-flex h-10 w-10
  items-center justify-center rounded-full transition-colors duration-300"
  aria-label="Toggle Theme"
>
  {#if darkMode}
    <Sun class="h-6 w-6" />
  {:else}
    <Moon class="h-6 w-6" />
  {/if}
</button>
