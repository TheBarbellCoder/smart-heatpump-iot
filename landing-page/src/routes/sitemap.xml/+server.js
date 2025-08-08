/**
 * sitemap.xml endpoint
 */
export const GET = ({ url }) => {
  const origin = url.origin;
  const lastmod = new Date().toISOString();
  const pages = [
    { loc: `${origin}/`, changefreq: 'weekly', priority: '1.0' },
    { loc: `${origin}/waitlist`, changefreq: 'monthly', priority: '0.8' },
    { loc: `${origin}/privacy`, changefreq: 'yearly', priority: '0.3' }
  ];

  const urls = pages
    .map(
      (p) =>
        `<url>\n  <loc>${p.loc}</loc>\n  <lastmod>${lastmod}</lastmod>\n  <changefreq>${p.changefreq}</changefreq>\n  <priority>${p.priority}</priority>\n</url>`
    )
    .join('\n');

  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`;

  return new Response(body, {
    headers: {
      'content-type': 'application/xml; charset=utf-8',
      'cache-control': 'public, max-age=3600'
    }
  });
};
