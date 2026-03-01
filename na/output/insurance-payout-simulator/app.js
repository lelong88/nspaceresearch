/**
 * app.js — Calculation engine and UI logic for Xanh Tương Lai Insurance Payout Simulator
 */

// ─── Node.js Compatibility ──────────────────────────────────────────────────
if (typeof require !== 'undefined' && typeof FUNDS === 'undefined') {
  const data = require('./data.js');
  var FUNDS = data.FUNDS;
  var DEFAULTS = data.DEFAULTS;
  var INITIAL_FEE_RATES = data.INITIAL_FEE_RATES;
  var EARLY_TERMINATION_RATES = data.EARLY_TERMINATION_RATES;
  var MGMT_FEE = data.MGMT_FEE;
  var RISK_RATES = data.RISK_RATES;
  var LOYALTY_MILESTONES = data.LOYALTY_MILESTONES;
  var SA_INCREASE = data.SA_INCREASE;
  var RIDERS = data.RIDERS;
}

// ─── Input Handling ─────────────────────────────────────────────────────────

/**
 * Reads form values from the DOM and returns an InputParams object.
 * Looks up fund high/low rates from the FUNDS array.
 * @returns {Object} InputParams
 */
function collectInputs() {
  var age = parseInt(document.getElementById('age').value, 10);
  var gender = document.getElementById('gender').value;
  var basicPremium = parseFloat(document.getElementById('basic-premium').value);
  var paymentYears = parseInt(document.getElementById('payment-years').value, 10);
  var fundId = document.getElementById('fund').value;

  var fund = FUNDS.find(function (f) { return f.id === fundId; });
  var highRate = fund ? fund.highRate : 0;
  var lowRate = fund ? fund.lowRate : 0;

  return {
    age: age,
    gender: gender,
    basicPremium: basicPremium,
    totalPremium: DEFAULTS.totalPremium,
    paymentYears: paymentYears,
    fundId: fundId,
    highRate: highRate,
    lowRate: lowRate,
  };
}

/**
 * Validates input parameters.
 * @param {Object} params - InputParams object
 * @returns {{ valid: boolean, errors: string[] }}
 */
function validateInputs(params) {
  var errors = [];

  if (!Number.isInteger(params.age) || params.age < 18 || params.age > 60) {
    errors.push('Tuổi phải là số nguyên từ 18 đến 60.');
  }

  if (typeof params.basicPremium !== 'number' || isNaN(params.basicPremium) || params.basicPremium < 20000000) {
    errors.push('Phí bảo hiểm cơ bản phải từ 20.000.000 VND trở lên.');
  }

  return {
    valid: errors.length === 0,
    errors: errors,
  };
}

// ─── Exports ────────────────────────────────────────────────────────────────
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    collectInputs: collectInputs,
    validateInputs: validateInputs,
  };
}
if (typeof window !== 'undefined') {
  window.collectInputs = collectInputs;
  window.validateInputs = validateInputs;
}
