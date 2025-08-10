import { browser } from '$app/environment';

class ThemeStore {
  darkMode = $state(false);
  constructor() {
    if (browser) {
      this.initialize();
    }
  }

  initialize() {
    const savedTheme = localStorage.getItem('themeSvelte');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    this.darkMode = savedTheme === 'dark' || (savedTheme === null && prefersDark);
    this.updateDOM();
  }

  toggle() {
    this.darkMode = !this.darkMode;
    this.updateDOM();
  }

  setTheme(isDark) {
    this.darkMode = isDark;
    this.updateDOM();
  }

  updateDOM() {
    if (browser) {
      const root = document.documentElement;
      if (this.darkMode) {
        root.classList.add('dark');
        localStorage.setItem('themeSvelte', 'dark');
      } else {
        root.classList.remove('dark');
        localStorage.setItem('themeSvelte', 'light');
      }
    }
  }

  get isDark() {
    return this.darkMode;
  }

  get isLight() {
    return !this.darkMode;
  }
}

export const theme = new ThemeStore();
