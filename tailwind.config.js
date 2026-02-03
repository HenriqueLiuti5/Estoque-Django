/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './estoque/templates/**/*.html',
    './**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      colors: {
        // A paleta exata que você estava usando no HTML
        brand: {
          50: '#ecfdf5',
          600: '#059669',
          700: '#047857',
          900: '#064e3b',
        }
      }
    },
  },
  plugins: [],
}