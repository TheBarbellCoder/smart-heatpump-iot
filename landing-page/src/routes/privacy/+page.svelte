<script lang="js">
  import { page } from '$app/stores';
  const siteName = 'ThermaSim';
  const title = `Privacy Policy — ${siteName}`;
  const description =
    'Read the ThermaSim Privacy Policy: GDPR-compliant handling of your email and consent for the waitlist. Learn what we collect, why, and your rights.';
  const canonical = $derived(
    $page.url && $page.url.origin
      ? `${$page.url.origin}${$page.url.pathname}`
      : ($page.url?.pathname ?? '/privacy')
  );
  // TODO Set ogImage to the snapshot of the dashboard.
  const ogImage = $derived(
    $page.url && $page.url.origin ? `${$page.url.origin}/ThermaSim.svg` : '/ThermaSim.svg'
  );
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />
  <meta property="og:site_name" content={siteName} />
  <meta property="og:type" content="article" />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:url" content={canonical} />
  <meta property="og:image" content={ogImage} />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content={ogImage} />
  <link rel="canonical" href={canonical} />
</svelte:head>

<div
  class="mt-24 box-border flex flex-col items-center justify-center gap-14 p-6 py-[100px] lg:mt-28 lg:p-8 lg:py-[100px]"
>
  <div class="text-heading-40 md:text-heading-48 lg:text-heading-56 text-start md:text-center">
    Privacy Policy
  </div>

  <div
    class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light flex flex-col justify-center gap-1 self-start"
  >
    <div>
      <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold"
        >Effective Date:</span
      > August 3, 2025
    </div>
    <div>
      <span class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold"
        >Data Controller:</span
      > Avinash Chikkadlur Ravi Shankar, Frankfurt am Main, Germany
    </div>
  </div>

  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      1. Introduction
    </div>
    <p class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
      I, Avinash Chikkadlur Ravi Shankar, am developing ThermaSim, a heat pump simulator to help
      HVAC professionals and engineers design systems faster and more accurately. This Privacy
      Policy explains how I collect, use, and protect your personal data when you join the ThermaSim
      waitlist via my website. As an individual based in Germany, I comply with the General Data
      Protection Regulation (GDPR) and the German Federal Data Protection Act (BDSG).
    </p>
  </div>
  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      2. Data I Collect
    </div>
    <div
      class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light flex flex-col items-start justify-start gap-3"
    >
      <p>I collect the following personal data via the waitlist form:</p>
      <ul class="flex list-outside list-disc flex-col gap-1 py-3 pr-3 pl-6">
        <li>Email address (required)</li>
        <li>Consent status (via checkbox)</li>
      </ul>
      <p>
        I may also collect anonymized website analytics (e.g., via Google Analytics) that cannot
        identify you.
      </p>
    </div>
  </div>
  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      3. Purpose of Data Collection
    </div>
    <div
      class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light flex flex-col items-start justify-start gap-3"
    >
      <p>I use your data to:</p>
      <ul class="flex list-outside list-disc flex-col gap-1 py-3 pr-3 pl-6">
        <li>Send you updates about ThermaSim’s beta program and launch.</li>
        <li>Respond to waitlist-related inquiries.</li>
        <li>Improve the website based on anonymized analytics.</li>
      </ul>
      <p>Data processing is based on your explicit consent (GDPR Article 6(1)(a)).</p>
    </div>
  </div>
  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      4. Data Sharing and Transfers
    </div>
    <div
      class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light flex flex-col items-start justify-start gap-3"
    >
      <p>Your data is not shared with third parties, except:</p>
      <ul class="flex list-outside list-disc flex-col gap-1 py-3 pr-3 pl-6">
        <li>
          Formspark, a GDPR-compliant service provider for form management, under a data processing
          agreement.
        </li>
        <li>
          Hosting providers (e.g., Vercel), which may process data in the United States. Data
          transfers outside the EEA are protected by Standard Contractual Clauses or the EU-U.S.
          Data Privacy Framework, per GDPR Article 46.
        </li>
        <li>If required by law to protect my legal rights.</li>
      </ul>
    </div>
  </div>
  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      5. Data Storage and Security
    </div>
    <p class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
      Your data is stored securely using encrypted systems (e.g., HTTPS). Data may be stored in the
      EEA or the US, depending on the hosting provider. I retain data only until the beta program
      concludes or you unsubscribe.
    </p>
  </div>
  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      6. Your Rights
    </div>
    <div
      class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light flex flex-col items-start justify-start gap-3"
    >
      <p>Under GDPR, you have the right to:</p>
      <ul class="flex list-outside list-disc flex-col gap-1 py-3 pr-3 pl-6">
        <li>Access, correct, or delete your data (Articles 15-17).</li>
        <li>Restrict or object to processing (Articles 18, 21).</li>
        <li>Data portability (Article 20).</li>
        <li>Withdraw consent at any time (e.g., by unsubscribing).</li>
      </ul>
      <p>
        Contact me at avinash.ravishankar@outlook.com to exercise these rights. I’ll respond within
        one month, per GDPR.
      </p>
    </div>
  </div>
  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      7. Cookies
    </div>
    <p class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
      The website may use cookies for anonymized analytics (e.g., Google Analytics). You can manage
      cookies via your browser settings. A cookie consent banner is provided, per GDPR.
    </p>
  </div>

  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      8. Changes to This Policy
    </div>
    <p class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
      I may update this policy as ThermaSim develops. Changes will be posted here, and significant
      updates will be emailed to waitlist members.
    </p>
  </div>

  <div class="flex flex-col items-start justify-stretch gap-5 self-start text-start">
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium"
    >
      9. Contact
    </div>
    <p class="text-copy-16-light md:text-copy-18-light lg:text-copy-20-light">
      For questions or complaints, email me at avinash.ravishankar@outlook.com. You can also contact
      the supervisory authority, such as the <span
        class="text-copy-16-semibold md:text-copy-18-semibold lg:text-copy-20-semibold"
      >
        Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen</span
      >.
    </p>
  </div>
</div>
