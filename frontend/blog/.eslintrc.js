module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/essential',
    '@vue/airbnb',
  ],
rules: {
    // other stuff
    "import/no-extraneous-dependencies": ["error", {"devDependencies": true}],
    'import/extensions': ['error', 'always', {
      js: 'never',
      mjs: 'never',
      jsx: 'never',
      ts: 'never',
      tsx: 'never',
      vue: 'never',
    }]
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
};
