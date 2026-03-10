import { readFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Read the index.html file
const htmlPath = resolve(__dirname, '..', 'index.html');
const htmlContent = readFileSync(htmlPath, 'utf-8');

// Extract the script content from the HTML
const scriptMatch = htmlContent.match(/<script>([\s\S]*?)<\/script>/);
const scriptContent = scriptMatch ? scriptMatch[1] : '';

// Load the HTML into jsdom (vitest jsdom environment provides document/window)
document.documentElement.innerHTML = htmlContent.match(/<html[^>]*>([\s\S]*)<\/html>/i)?.[1] || htmlContent;

// Transform the script so key declarations become window properties.
const transformedScript = scriptContent
  .replace(/\bvar\s+(GLOSSARY|FAQ_ITEMS|FUNDS_DATA|RIDERS_DATA)\s*=/g, 'window.$1 =')
  .replace(/\bfunction\s+(vnd|calcSTBH|stbhAtYear|calcFamilyBonus|estimateAccountValue|recommendFund|rateForRisk|buildScenarios|renderScenarioButtons|renderRiders|renderFunds|renderFAQ|renderGlossary|renderPersonalizedBenefits|selectScenario|showSlide|nextSlide|prevSlide|startAutoAdvance|clearAutoAdvance|togglePause|showScreen|collectInputs|startExperience|initTabs|initRiskOptions)\s*\(/g, 'window.$1 = function(')
  .replace(/\bvar\s+(state|currentScenarios)\s*=/g, 'window.$1 =');

// Execute the transformed script in the window context
try {
  const fn = new Function(transformedScript);
  fn.call(window);
} catch (e) {
  console.warn('Setup: Error executing script:', e.message);
}

// Verify key globals are available
const requiredGlobals = [
  'GLOSSARY', 'FAQ_ITEMS', 'FUNDS_DATA', 'RIDERS_DATA',
  'vnd', 'calcSTBH', 'stbhAtYear', 'calcFamilyBonus',
  'estimateAccountValue', 'recommendFund', 'rateForRisk', 'state'
];

const missing = requiredGlobals.filter(name => !(name in window));
if (missing.length > 0) {
  console.warn('Setup: Missing globals after initialization:', missing.join(', '));
}
