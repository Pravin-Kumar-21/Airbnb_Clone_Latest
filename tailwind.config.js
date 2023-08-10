// tailwind.config.js
module.exports = {
  content: ['./templates/**/*.{html}',"./templates/*.{html}"],
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      spacing: {
        "25vh": "25vh",
        "75vh": "75vh"
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
