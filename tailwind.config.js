/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./views/**/*.ejs",
    "./public/**/*.html",
    "./**/*.ejs",
  ],
  theme: {
    extend: {
      colors: {
        // Add EVERY custom color you might ever use
        'neutral-primary': '#ffffff',
        'neutral-primary-medium': '#f9fafb',
        'neutral-secondary-soft': '#f3f4f6',
        'neutral-secondary-medium': '#f5f5f5',
        'neutral-tertiary': '#e5e7eb',
        'neutral-tertiary-medium': '#d1d5db',
        'default': '#e5e7eb',
        'default-medium': '#d1d5db',
        'default-strong': '#9ca3af',
        'heading': '#111827',
        'body': '#6b7280',
        'brand': '#3b82f6',
        'brand-strong': '#2563eb',
        'brand-medium': '#93c5fd',
        'fg-brand': '#3b82f6',
      },
      borderRadius: {
        'base': '0.5rem',
      },
      boxShadow: {
        'xs': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
      },
    },
  },
  plugins: [],
}