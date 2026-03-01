/**
 * data.js — Hardcoded constants for Xanh Tương Lai Insurance Payout Simulator
 * All rate tables, fund definitions, fee schedules, and default values.
 */

// ─── Fund Definitions ────────────────────────────────────────────────────────
const FUNDS = [
  { id: 'bao-toan', name: 'Bảo Toàn', highRate: 0.035, lowRate: 0.015 },
  { id: 'tich-luy', name: 'Tích Lũy', highRate: 0.05, lowRate: 0.015 },
  { id: 'on-dinh', name: 'Ổn Định', highRate: 0.06, lowRate: 0.013 },
  { id: 'can-bang', name: 'Cân Bằng', highRate: 0.07, lowRate: 0.013 },
  { id: 'phat-trien', name: 'Phát Triển', highRate: 0.08, lowRate: 0.013 },
  { id: 'tang-truong', name: 'Tăng Trưởng', highRate: 0.09, lowRate: 0.013 },
  { id: 'hung-thinh-2035', name: 'Hưng Thịnh 2035', highRate: 0.07, lowRate: 0.013 },
  { id: 'hung-thinh-2040', name: 'Hưng Thịnh 2040', highRate: 0.07, lowRate: 0.013 },
  { id: 'hung-thinh-2045', name: 'Hưng Thịnh 2045', highRate: 0.07, lowRate: 0.013 },
];

// ─── Initial Fee Schedule (% of Basic Premium) ──────────────────────────────
const INITIAL_FEE_RATES = {
  1: 0.50, 2: 0.30, 3: 0.20, 4: 0.20, 5: 0.20,
  6: 0.02, 7: 0.02, 8: 0.02, 9: 0.02, 10: 0.02,
  // Year 11+: 0%
};

// ─── Early Termination Fee (% of Account Value) ─────────────────────────────
const EARLY_TERMINATION_RATES = {
  1: 0.90, 2: 0.90, 3: 0.50, 4: 0.30, 5: 0.20, 6: 0.10,
  // Year 7+: 0%
};

// ─── Management Fee Config ───────────────────────────────────────────────────
const MGMT_FEE = {
  baseMonthly: 45000,    // VND/month in year 1
  annualIncrease: 2000,  // VND/year increase
  maxMonthly: 70000,     // VND/month cap
};

// ─── Risk Fee Rate Table ─────────────────────────────────────────────────────
// Rate per 1,000 VND of Sum Assured, keyed by gender then age (18–99)
// Female rates are lower than male rates; rates increase with age.
const RISK_RATES = {
  male: {
    18: 1.05, 19: 1.05, 20: 1.06, 21: 1.08, 22: 1.10,
    23: 1.12, 24: 1.14, 25: 1.16, 26: 1.19, 27: 1.22,
    28: 1.25, 29: 1.29, 30: 1.33, 31: 1.38, 32: 1.43,
    33: 1.49, 34: 1.56, 35: 1.63, 36: 1.72, 37: 1.81,
    38: 1.92, 39: 2.04, 40: 2.17, 41: 2.32, 42: 2.49,
    43: 2.68, 44: 2.89, 45: 3.13, 46: 3.40, 47: 3.70,
    48: 4.04, 49: 4.42, 50: 4.84, 51: 5.31, 52: 5.83,
    53: 6.41, 54: 7.06, 55: 7.78, 56: 8.58, 57: 9.47,
    58: 10.46, 59: 11.56, 60: 12.79, 61: 14.16, 62: 15.69,
    63: 17.39, 64: 19.28, 65: 21.39, 66: 23.73, 67: 26.33,
    68: 29.22, 69: 32.42, 70: 35.98, 71: 39.93, 72: 44.32,
    73: 49.19, 74: 54.60, 75: 60.61, 76: 63.50, 77: 66.53,
    78: 69.70, 79: 73.02, 80: 76.50, 81: 78.50, 82: 80.50,
    83: 82.50, 84: 84.50, 85: 86.50, 86: 88.50, 87: 90.50,
    88: 92.50, 89: 94.50, 90: 96.50, 91: 98.50, 92: 100.50,
    93: 102.50, 94: 104.50, 95: 106.50, 96: 108.50, 97: 110.50,
    98: 112.50, 99: 114.50,
  },
  female: {
    18: 0.52, 19: 0.52, 20: 0.53, 21: 0.54, 22: 0.55,
    23: 0.56, 24: 0.57, 25: 0.59, 26: 0.61, 27: 0.63,
    28: 0.65, 29: 0.68, 30: 0.71, 31: 0.74, 32: 0.78,
    33: 0.82, 34: 0.87, 35: 0.92, 36: 0.98, 37: 1.04,
    38: 1.11, 39: 1.19, 40: 1.28, 41: 1.37, 42: 1.48,
    43: 1.60, 44: 1.73, 45: 1.88, 46: 2.04, 47: 2.22,
    48: 2.42, 49: 2.65, 50: 2.90, 51: 3.18, 52: 3.50,
    53: 3.85, 54: 4.24, 55: 4.67, 56: 5.15, 57: 5.68,
    58: 6.28, 59: 6.94, 60: 7.67, 61: 8.50, 62: 9.41,
    63: 10.43, 64: 11.57, 65: 12.83, 66: 14.24, 67: 15.80,
    68: 17.53, 69: 19.45, 70: 21.59, 71: 23.96, 72: 26.59,
    73: 29.52, 74: 32.76, 75: 36.37, 76: 38.10, 77: 39.92,
    78: 41.82, 79: 43.81, 80: 45.90, 81: 47.10, 82: 48.30,
    83: 49.50, 84: 50.70, 85: 51.90, 86: 53.10, 87: 54.30,
    88: 55.50, 89: 56.70, 90: 57.90, 91: 59.10, 92: 60.30,
    93: 61.50, 94: 62.70, 95: 63.90, 96: 65.10, 97: 66.30,
    98: 67.50, 99: 68.70,
  },
};

// ─── Loyalty Bonus Milestones ────────────────────────────────────────────────
const LOYALTY_MILESTONES = [10, 15, 20];

// ─── Sum Assured Auto-Increase Config ────────────────────────────────────────
const SA_INCREASE = {
  startYear: 2,
  endYear: 6,
  annualRate: 0.10,
  maxCumulative: 0.50,
};

// ─── Rider Definitions ──────────────────────────────────────────────────────
const RIDERS = [
  {
    name: 'Lá Chắn Xanh',
    desc: 'Bệnh hiểm nghèo',
    benefits: '200 triệu (giai đoạn muộn), 50 triệu (giai đoạn sớm), 50 triệu (đặc biệt)',
  },
  {
    name: 'Dự Phòng Xanh',
    desc: 'Nằm viện',
    benefits: '200.000 VND/ngày',
  },
  {
    name: 'Hộ Vệ Xanh',
    desc: 'Tai nạn',
    benefits: '250 triệu VND',
  },
];

// ─── Default Input Values ───────────────────────────────────────────────────
const DEFAULTS = {
  age: 30,
  gender: 'female',
  basicPremium: 28570000,
  totalPremium: 30000000,
  paymentYears: 5,
  fundId: 'can-bang',
};

// ─── Exports ────────────────────────────────────────────────────────────────
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    FUNDS,
    INITIAL_FEE_RATES,
    EARLY_TERMINATION_RATES,
    MGMT_FEE,
    RISK_RATES,
    LOYALTY_MILESTONES,
    SA_INCREASE,
    RIDERS,
    DEFAULTS,
  };
}
if (typeof window !== 'undefined') {
  window.FUNDS = FUNDS;
  window.INITIAL_FEE_RATES = INITIAL_FEE_RATES;
  window.EARLY_TERMINATION_RATES = EARLY_TERMINATION_RATES;
  window.MGMT_FEE = MGMT_FEE;
  window.RISK_RATES = RISK_RATES;
  window.LOYALTY_MILESTONES = LOYALTY_MILESTONES;
  window.SA_INCREASE = SA_INCREASE;
  window.RIDERS = RIDERS;
  window.DEFAULTS = DEFAULTS;
}
