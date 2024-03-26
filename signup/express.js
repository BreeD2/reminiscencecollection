app.use((req, res, next) => {
  res.setHeader("Content-Security-Policy", "script-src 'self' https://ajax.googleapis.com https://breed2.github.io; style-src 'self' 'unsafe-inline' https://www.w3schools.com https://cdnjs.cloudflare.com;");
  next();
});

app.use((req, res, next) => {
  res.setHeader("Content-Security-Policy", "script-src 'self' https://ajax.googleapis.com https://breed2.github.io; style-src 'self' 'unsafe-inline' https://www.w3schools.com https://cdnjs.cloudflare.com;");
  // Consider adding CSP reporting for monitoring and debugging: 'report-uri /path-to-report-violations';
  next();
});
