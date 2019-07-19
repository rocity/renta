const withSass = require('@zeit/next-sass');

module.exports = withSass({
  // Config
  cssModules: true,
  env: {
    API_URL: process.env.API_URL || 'http://localhost:8000'
  }
});
