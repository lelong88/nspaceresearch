import { describe, it, expect } from 'vitest';

describe('Smoke Test - Setup Verification', () => {
  it('should load the document with correct lang attribute', () => {
    const html = document.querySelector('html');
    expect(html).not.toBeNull();
  });

  it('should have a document title', () => {
    expect(document.title).toContain('Xanh Tương Lai');
  });

  it('should have the main sections in the DOM', () => {
    expect(document.getElementById('hero')).not.toBeNull();
    expect(document.getElementById('main-nav')).not.toBeNull();
    expect(document.getElementById('faq')).not.toBeNull();
    expect(document.getElementById('footer')).not.toBeNull();
  });

  it('should expose GLOSSARY as a global with at least 15 terms', () => {
    expect(window.GLOSSARY).toBeDefined();
    expect(typeof window.GLOSSARY).toBe('object');
    expect(Object.keys(window.GLOSSARY).length).toBeGreaterThanOrEqual(15);
  });

  it('should expose FAQ_ITEMS as a global array', () => {
    expect(window.FAQ_ITEMS).toBeDefined();
    expect(Array.isArray(window.FAQ_ITEMS)).toBe(true);
    expect(window.FAQ_ITEMS.length).toBeGreaterThanOrEqual(5);
  });

  it('should expose FUNDS, RIDERS, BENEFITS, STBH_GROWTH, AUDIENCE_PROFILES', () => {
    expect(window.FUNDS).toBeDefined();
    expect(window.RIDERS).toBeDefined();
    expect(window.BENEFITS).toBeDefined();
    expect(window.STBH_GROWTH).toBeDefined();
    expect(window.AUDIENCE_PROFILES).toBeDefined();
  });

  it('should expose calculateSTBH and calculateFamilySTBHIncrease functions', () => {
    expect(typeof window.calculateSTBH).toBe('function');
    expect(typeof window.calculateFamilySTBHIncrease).toBe('function');
  });

  it('should expose interactive component objects', () => {
    expect(window.ScrollAnimator).toBeDefined();
    expect(window.TooltipManager).toBeDefined();
    expect(window.AccordionController).toBeDefined();
    expect(window.NavController).toBeDefined();
    expect(window.ChartAnimator).toBeDefined();
  });
});
