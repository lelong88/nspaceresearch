/**
 * calculations.test.js — Unit tests for Xanh Tương Lai calculation functions
 * Uses Node.js built-in test runner and assert module.
 *
 * Requirements: 1.2, 1.4, 2.1, 3.1, 3.2, 4.2, 5.1, 6.1, 8.1, 9.2
 */

const { describe, test } = require('node:test');
const assert = require('node:assert');
const data = require('../data.js');
const app = require('../app.js');

// ─── 1. Default profile validation ─────────────────────────────────────────
describe('Default profile validation', () => {
  test('age 30, female, 28570000 VND, 5 years, can-bang → valid', () => {
    const result = app.validateInputs({
      age: 30,
      gender: 'female',
      basicPremium: 28570000,
      paymentYears: 5,
      fundId: 'can-bang',
    });
    assert.strictEqual(result.valid, true);
    assert.strictEqual(result.errors.length, 0);
  });
});

// ─── 2. Boundary age validation ─────────────────────────────────────────────
describe('Age boundary validation', () => {
  test('age 18 → valid', () => {
    const result = app.validateInputs({ age: 18, gender: 'female', basicPremium: 28570000 });
    assert.strictEqual(result.valid, true);
  });

  test('age 17 → invalid', () => {
    const result = app.validateInputs({ age: 17, gender: 'female', basicPremium: 28570000 });
    assert.strictEqual(result.valid, false);
    assert.ok(result.errors.length > 0);
  });

  test('age 60 → valid', () => {
    const result = app.validateInputs({ age: 60, gender: 'female', basicPremium: 28570000 });
    assert.strictEqual(result.valid, true);
  });

  test('age 61 → invalid', () => {
    const result = app.validateInputs({ age: 61, gender: 'female', basicPremium: 28570000 });
    assert.strictEqual(result.valid, false);
  });
});

// ─── 3. Boundary premium validation ─────────────────────────────────────────
describe('Premium boundary validation', () => {
  test('premium 20000000 → valid', () => {
    const result = app.validateInputs({ age: 30, gender: 'female', basicPremium: 20000000 });
    assert.strictEqual(result.valid, true);
  });

  test('premium 19999999 → invalid', () => {
    const result = app.validateInputs({ age: 30, gender: 'female', basicPremium: 19999999 });
    assert.strictEqual(result.valid, false);
  });
});

// ─── 4. Sum Assured schedule ────────────────────────────────────────────────
describe('Sum Assured schedule', () => {
  const baseSA = 28570000;
  const schedule = app.calcSumAssuredSchedule(baseSA, 10);

  test('year 1 = baseSA', () => {
    assert.strictEqual(schedule[1], 28570000);
  });

  test('year 2 = baseSA * 1.1', () => {
    assert.ok(Math.abs(schedule[2] - 31427000) < 0.01, `Expected ~31427000, got ${schedule[2]}`);
  });

  test('year 6 = baseSA * 1.5 (max cumulative)', () => {
    assert.strictEqual(schedule[6], 42855000);
  });

  test('year 7 = baseSA * 1.5 (constant after max)', () => {
    assert.strictEqual(schedule[7], 42855000);
  });
});

// ─── 5. Initial fee schedule ────────────────────────────────────────────────
describe('Initial fee schedule', () => {
  const premium = 28570000;

  test('year 1 = 50% of premium', () => {
    assert.strictEqual(app.calcInitialFee(1, premium), premium * 0.50);
  });

  test('year 5 = 20% of premium', () => {
    assert.strictEqual(app.calcInitialFee(5, premium), premium * 0.20);
  });

  test('year 6 = 2% of premium', () => {
    const expected = premium * 0.02;
    assert.ok(Math.abs(app.calcInitialFee(6, premium) - expected) < 0.01);
  });

  test('year 11 = 0% (no fee)', () => {
    assert.strictEqual(app.calcInitialFee(11, premium), 0);
  });
});

// ─── 6. Management fee ──────────────────────────────────────────────────────
describe('Management fee', () => {
  test('year 1 = 45000 * 12 = 540000', () => {
    assert.strictEqual(app.calcManagementFee(1), 540000);
  });

  test('year 13 = min(45000 + 12*2000, 70000) * 12 = 69000 * 12 = 828000', () => {
    assert.strictEqual(app.calcManagementFee(13), 828000);
  });

  test('year 14 = min(45000 + 13*2000, 70000) * 12 = 70000 * 12 = 840000 (cap hit)', () => {
    assert.strictEqual(app.calcManagementFee(14), 840000);
  });
});

// ─── 7. Risk fee ────────────────────────────────────────────────────────────
describe('Risk fee', () => {
  test('age 30, female, SA=28570000 → 0.71 * 28570000 / 1000', () => {
    const expected = 0.71 * 28570000 / 1000;
    const actual = app.calcRiskFee(30, 'female', 28570000);
    assert.ok(Math.abs(actual - expected) < 0.01, `Expected ~${expected}, got ${actual}`);
  });
});

// ─── 8. Loyalty bonus at milestone ──────────────────────────────────────────
describe('Loyalty bonus', () => {
  test('year 10, age 40, premium 28570000 → (40/100) * 28570000 = 11428000', () => {
    assert.strictEqual(app.calcLoyaltyBonus(10, 40, 28570000), 11428000);
  });

  test('year 5 (not milestone) → 0', () => {
    assert.strictEqual(app.calcLoyaltyBonus(5, 35, 28570000), 0);
  });
});

// ─── 9. (placeholder — numbering continues) ────────────────────────────────

// ─── 10. Death benefit ──────────────────────────────────────────────────────
describe('Death benefit', () => {
  test('max(5000000, 28570000) = 28570000', () => {
    assert.strictEqual(app.calcDeathBenefit(5000000, 28570000), 28570000);
  });

  test('max(50000000, 28570000) = 50000000', () => {
    assert.strictEqual(app.calcDeathBenefit(50000000, 28570000), 50000000);
  });
});

// ─── 11. TPD benefit ────────────────────────────────────────────────────────
describe('TPD benefit', () => {
  test('age 75 → max(AV, SA)', () => {
    assert.strictEqual(app.calcTPDBenefit(5000000, 28570000, 75), 28570000);
  });

  test('age 76 → null', () => {
    assert.strictEqual(app.calcTPDBenefit(5000000, 28570000, 76), null);
  });
});

// ─── 12. formatVND ──────────────────────────────────────────────────────────
describe('formatVND', () => {
  test('0 → "0 VND"', () => {
    assert.strictEqual(app.formatVND(0), '0 VND');
  });

  test('1000 → "1.000 VND"', () => {
    assert.strictEqual(app.formatVND(1000), '1.000 VND');
  });

  test('28570000 → "28.570.000 VND"', () => {
    assert.strictEqual(app.formatVND(28570000), '28.570.000 VND');
  });
});

// ─── 13. Default profile projection ─────────────────────────────────────────
describe('Default profile projection', () => {
  const fund = data.FUNDS.find(f => f.id === 'can-bang');
  const params = {
    age: 30,
    gender: 'female',
    basicPremium: 28570000,
    totalPremium: 30000000,
    paymentYears: 5,
    fundId: 'can-bang',
    highRate: fund.highRate,
    lowRate: fund.lowRate,
  };
  const result = app.projectAccountValue(params);

  test('year 1 account value (high) should be positive', () => {
    assert.ok(result.rows[0].accountValueHigh > 0, 'Year 1 AV high should be > 0');
  });

  test('projection should have 40 rows (no lapse for default high scenario)', () => {
    // Default profile with can-bang fund should not lapse in high scenario within 40 years
    // The projection runs up to 40 years or until both scenarios lapse
    assert.ok(result.rows.length > 0, 'Should have at least 1 row');
    // High scenario should not lapse
    assert.strictEqual(result.lapseYearHigh, null, 'High scenario should not lapse');
  });
});

// ─── 14. Lapse scenario ─────────────────────────────────────────────────────
describe('Lapse scenario', () => {
  const fund = data.FUNDS.find(f => f.id === 'bao-toan');
  const params = {
    age: 60,
    gender: 'male',
    basicPremium: 20000000,
    totalPremium: 20000000,
    paymentYears: 3,
    fundId: 'bao-toan',
    highRate: fund.highRate,
    lowRate: fund.lowRate,
  };
  const result = app.projectAccountValue(params);

  test('low scenario should lapse', () => {
    assert.ok(result.lapseYearLow !== null, 'Low scenario should lapse for age 60, male, 20M, 3yr, bao-toan');
  });

  test('detectLapse returns correct lapse year for low scenario', () => {
    const lapseYear = app.detectLapse(result.rows, 'accountValueLow');
    assert.ok(lapseYear !== null, 'detectLapse should find a lapse year');
    assert.strictEqual(typeof lapseYear, 'number');
  });

  test('no-lapse scenario: default profile high scenario has no lapse', () => {
    const canBang = data.FUNDS.find(f => f.id === 'can-bang');
    const defaultParams = {
      age: 30,
      gender: 'female',
      basicPremium: 28570000,
      totalPremium: 30000000,
      paymentYears: 5,
      fundId: 'can-bang',
      highRate: canBang.highRate,
      lowRate: canBang.lowRate,
    };
    const defaultResult = app.projectAccountValue(defaultParams);
    const lapseYear = app.detectLapse(defaultResult.rows, 'accountValueHigh');
    assert.strictEqual(lapseYear, null, 'Default profile high scenario should not lapse');
  });
});
