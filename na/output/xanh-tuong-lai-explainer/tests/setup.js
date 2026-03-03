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

// Transform the script so all declarations become window properties.
// - `const X =` and `let X =` → `window.X =`
// - `var X =` → `window.X =`
// - `function X(` → `window.X = function(`
// This ensures everything is accessible on the global window object.
const transformedScript = scriptContent
  .replace(/\b(const|let|var)\s+(GLOSSARY|FAQ_ITEMS|FUNDS|RIDERS|BENEFITS|STBH_GROWTH|AUDIENCE_PROFILES)\s*=/g, 'window.$2 =')
  .replace(/\bfunction\s+(calculateSTBH|calculateFamilySTBHIncrease)\s*\(/g, 'window.$1 = function(')
  .replace(/\bvar\s+(ScrollAnimator|TooltipManager|AccordionController|NavController|ChartAnimator)\s*=/g, 'window.$1 =');

// Execute the transformed script in the window context
try {
  const fn = new Function(transformedScript);
  fn.call(window);
} catch (e) {
  console.warn('Setup: Error executing script:', e.message);
}

// Verify key globals are available
const requiredGlobals = [
  'GLOSSARY', 'FAQ_ITEMS', 'FUNDS', 'RIDERS', 'BENEFITS',
  'STBH_GROWTH', 'AUDIENCE_PROFILES', 'calculateSTBH',
  'calculateFamilySTBHIncrease', 'ScrollAnimator', 'TooltipManager',
  'AccordionController', 'NavController', 'ChartAnimator'
];

const missing = requiredGlobals.filter(name => !(name in window));
if (missing.length > 0) {
  console.warn('Setup: Missing globals after initialization:', missing.join(', '));
}
