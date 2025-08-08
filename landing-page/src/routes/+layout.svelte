<script lang="js">
  import '../app.css';
  import Navbar from '../components/Navbar.svelte';
  import Footer from '../components/Footer.svelte';
  let { children } = $props();
</script>

<svelte:head>
  <title>ThermaSim</title>
  <meta
    name="description"
    content="ThermaSim streamlines heat pump design for HVAC pros—99% accurate simulations, faster workflows, flexible settings, and instant CoP/energy metrics."
  />
  <meta property="og:site_name" content="ThermaSim" />
  <meta name="robots" content="index, follow" />
</svelte:head>

<Navbar />
{@render children()}
<Footer />
