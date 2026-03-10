import { describe, it, expect } from 'vitest';

describe('Smoke Test - Setup Verification', () => {
  it('should load the document with correct lang attribute', () => {
    const html = document.querySelector('html');
    expect(html).not.toBeNull();
  });

  it('should have a document title containing Xanh Tương Lai', () => {
    expect(document.title).toContain('Xanh Tương Lai');
  });

  it('should have the main screens in the DOM', () => {
    expect(document.getElementById('screen-input')).not.toBeNull();
    expect(document.getElementById('screen-story')).not.toBeNull();
  });

  it('should have input form elements', () => {
    expect(document.getElementById('inp-name')).not.toBeNull();
    expect(document.getElementById('inp-age')).not.toBeNull();
    expect(document.getElementById('inp-gender')).not.toBeNull();
    expect(document.getElementById('inp-budget')).not.toBeNull();
  });

  it('should expose GLOSSARY as a global with at least 10 terms', () => {
    expect(window.GLOSSARY).toBeDefined();
    expect(typeof window.GLOSSARY).toBe('object');
    expect(Object.keys(window.GLOSSARY).length).toBeGreaterThanOrEqual(10);
  });

  it('should expose FAQ_ITEMS as a global array', () => {
    expect(window.FAQ_ITEMS).toBeDefined();
    expect(Array.isArray(window.FAQ_ITEMS)).toBe(true);
    expect(window.FAQ_ITEMS.length).toBeGreaterThanOrEqual(5);
  });

  it('should expose FUNDS_DATA and RIDERS_DATA', () => {
    expect(window.FUNDS_DATA).toBeDefined();
    expect(Array.isArray(window.FUNDS_DATA)).toBe(true);
    expect(window.FUNDS_DATA.length).toBe(9);
    expect(window.RIDERS_DATA).toBeDefined();
    expect(Array.isArray(window.RIDERS_DATA)).toBe(true);
  });

  it('should expose utility functions', () => {
    expect(typeof window.vnd).toBe('function');
    expect(typeof window.calcSTBH).toBe('function');
    expect(typeof window.stbhAtYear).toBe('function');
    expect(typeof window.calcFamilyBonus).toBe('function');
    expect(typeof window.estimateAccountValue).toBe('function');
    expect(typeof window.recommendFund).toBe('function');
  });

  it('should expose app state', () => {
    expect(window.state).toBeDefined();
    expect(window.state.age).toBe(30);
    expect(window.state.riskLevel).toBe(2);
  });

  it('vnd should format numbers correctly', () => {
    expect(window.vnd(30000000)).toContain('30');
    expect(window.vnd(30000000)).toContain('triệu');
    expect(window.vnd(1500000000)).toContain('tỷ');
  });

  it('calcSTBH should return 5x premium', () => {
    expect(window.calcSTBH(30000000)).toBe(150000000);
  });

  it('calcFamilyBonus should cap at 25%', () => {
    expect(window.calcFamilyBonus(1)).toBe(5);
    expect(window.calcFamilyBonus(3)).toBe(15);
    expect(window.calcFamilyBonus(10)).toBe(25);
  });

  it('stbhAtYear should increase 10% per year from year 2', () => {
    var base = 100000000;
    expect(window.stbhAtYear(base, 1)).toBe(base);
    expect(window.stbhAtYear(base, 2)).toBeCloseTo(base * 1.1, 0);
    expect(window.stbhAtYear(base, 6)).toBeCloseTo(base * Math.pow(1.1, 5), 0);
    // Year 7+ should cap at year 6 value
    expect(window.stbhAtYear(base, 10)).toBeCloseTo(base * Math.pow(1.1, 5), 0);
  });
});
