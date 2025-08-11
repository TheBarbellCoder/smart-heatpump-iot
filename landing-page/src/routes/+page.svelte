<script lang="js">
  import Hero from '../components/Hero.svelte';
  import Features from '../components/Features.svelte';
  import CTA from '../components/CTA.svelte';
  import { page } from '$app/stores';

  const siteName = 'ThermaSim';
  const title = `${siteName} — Simplify Heat Pump Design with Precision`;
  const description =
    'ThermaSim streamlines heat pump design for HVAC pros—99% accurate simulations, cut design time by up to 50%, flexible refrigerants, and instant CoP/energy metrics.';
  const canonical = $derived(
    $page.url && $page.url.origin
      ? `${$page.url.origin}${$page.url.pathname}`
      : ($page.url?.pathname ?? '/')
  );
  const ogImage = $derived(
    $page.url && $page.url.origin
      ? `${$page.url.origin}/ThermaSim-Light-OG.png`
      : '/ThermaSim-Light-OG.png'
  );
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />
  <meta property="og:site_name" content={siteName} />
  <meta property="og:type" content="website" />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:url" content={canonical} />
  <meta property="og:image" content={ogImage} />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content={ogImage} />
  <link rel="canonical" href={canonical} />
</svelte:head>

<Hero />
<Features />
<CTA />
