/**
 * llms.txt endpoint
 * A concise, LLM-friendly summary of the product and pages based on the landing copy.
 */
export const GET = ({ url }) => {
  const origin = url.origin;
  const lines = [
    'Product: ThermaSim',
    'Tagline: Simplify Heat Pump Design with Precision',
    'One-liner: ThermaSim streamlines complex heat pump design calculations for HVAC professionals and engineers.',
    'Audience: HVAC professionals, mechanical engineers, energy consultants',
    'Key capabilities:',
    '- 99% accurate simulations',
    '- Cut design time by up to 50%',
    '- Flexible refrigerants and parameter inputs',
    '- Instant CoP and energy metrics',
    'Primary CTA: Join the waitlist for early access',
    `CTA URL: ${origin}/waitlist`,
    'Secondary pages:',
    `- Privacy Policy: ${origin}/privacy`,
    'Brand tone: professional, precise, practical',
    'Keywords: heat pump simulator, HVAC design, CoP, energy metrics, refrigerants, engineering, simulation',
    'Notes: GDPR-compliant waitlist; email used only for ThermaSim updates'
  ];

  const body = lines.join('\n') + '\n';
  return new Response(body, {
    headers: {
      'content-type': 'text/plain; charset=utf-8',
      'cache-control': 'public, max-age=86400'
    }
  });
};
