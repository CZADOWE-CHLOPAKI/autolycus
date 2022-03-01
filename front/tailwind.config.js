module.exports = {
  mode: 'jit',
  purge: ['./**/**.html', './src/**/*.{js,jsx,ts,tsx,vue}'],
  content: [],
  theme: {
    extend: {
      fontFamily: {
        VT323: ['monospace'], //TODO FIX THIS
      },
      animation: {
        'spin-slow': 'spin 2s linear infinite',
        'spin-xslow': 'spin 10s linear infinite',
      },
    },
  },
  plugins: [],
};
