module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    purge: {
        enabled: false, //true for production build
        content: [
            './templates/**/*.html',
            './templates/*.html'
        ]
    },
    theme: {
        extend: {
          spacing: {
        "25vh": "25vh",
        "75vh": "75vh"
      }
        },
    },
    variants: {},
    plugins: [],
}