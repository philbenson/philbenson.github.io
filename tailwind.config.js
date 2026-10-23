/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/templates/**/*.html"],
  darkMode: ['variant', [
    '@media (prefers-color-scheme: dark) { &:not(.light *) }',
    '&:is(.dark *)',
  ]],
  theme: {
    colors: {
      'black': '#2d2c2b',
      'grey': '#b3b1af',
      'white': '#faf8f4',
      'purple': '#6c6471',
      'fuschia': '#9a6770',
      'pink': '#d17372',
      'orange': '#e39c68',
      'yellow': '#dec894',
    },
    fontFamily: {
      'sans': ['"HelveticaNeue-Light"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
      'serif': ['"HarrietDisplay-Bold"', '"Harriet Display"', 'Georgia', 'serif'],
      'title': ['"HarrietDisplay-Black"', '"Harriet Display"', 'Georgia', 'serif'],
    },
    extend: {},
  },
  plugins: [],
}

