<script>
  import '../app.css';
  import '../components/Navbar.svelte';
  import Navbar from '../components/Navbar.svelte';
  let { children } = $props();
</script>

<Navbar />
{@render children()}
