/**
 * app.js — Calculation engine and UI logic for Xanh Tương Lai Insurance Payout Simulator
 */

// ─── Node.js Compatibility ──────────────────────────────────────────────────
/* eslint-disable no-var */
if (typeof window === 'undefined' && typeof require !== 'undefined') {
  var _data = require('./data.js');
  /* global FUNDS, DEFAULTS, INITIAL_FEE_RATES, EARLY_TERMINATION_RATES, MGMT_FEE, RISK_RATES, LOYALTY_MILESTONES, SA_INCREASE, RIDERS */
  Object.assign(globalThis, _data);
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

// ─── Sum Assured & Fee Calculations ─────────────────────────────────────────

/**
 * Calculates the Sum Assured schedule with 10% annual increase from year 2–6.
 * Increase is additive (not compounding): year 2 = baseSA*1.1, year 3 = baseSA*1.2, etc.
 * Max cumulative increase is 50%. From year 7 onward SA stays at baseSA * 1.5.
 * @param {number} baseSA - Base Sum Assured
 * @param {number} maxYear - Last year to compute (inclusive)
 * @returns {number[]} Array indexed 1..maxYear with SA values
 */
function calcSumAssuredSchedule(baseSA, maxYear) {
  var schedule = [0]; // index 0 unused, 1-based
  for (var y = 1; y <= maxYear; y++) {
    if (y === 1) {
      schedule[y] = baseSA;
    } else if (y >= SA_INCREASE.startYear && y <= SA_INCREASE.endYear) {
      var increase = (y - 1) * SA_INCREASE.annualRate;
      if (increase > SA_INCREASE.maxCumulative) {
        increase = SA_INCREASE.maxCumulative;
      }
      schedule[y] = baseSA * (1 + increase);
    } else {
      // year 7+: constant at max cumulative
      schedule[y] = baseSA * (1 + SA_INCREASE.maxCumulative);
    }
  }
  return schedule;
}

/**
 * Calculates the initial fee for a given contract year.
 * Year 1: 50%, Year 2: 30%, Year 3-5: 20%, Year 6-10: 2%, Year 11+: 0%
 * @param {number} year - Contract year (1-based)
 * @param {number} basicPremium - Annual basic premium
 * @returns {number} Initial fee amount
 */
function calcInitialFee(year, basicPremium) {
  var rate = INITIAL_FEE_RATES[year];
  if (rate === undefined) {
    rate = 0; // Year 11+
  }
  return basicPremium * rate;
}

/**
 * Calculates the annual management fee for a given contract year.
 * Monthly fee = min(baseMonthly + (year-1)*annualIncrease, maxMonthly)
 * Annual fee = monthly * 12
 * @param {number} year - Contract year (1-based)
 * @returns {number} Annual management fee
 */
function calcManagementFee(year) {
  var monthly = MGMT_FEE.baseMonthly + (year - 1) * MGMT_FEE.annualIncrease;
  if (monthly > MGMT_FEE.maxMonthly) {
    monthly = MGMT_FEE.maxMonthly;
  }
  return monthly * 12;
}

/**
 * Calculates the annual risk fee based on age, gender, and Sum Assured.
 * @param {number} age - Customer's age at the contract year
 * @param {string} gender - 'male' or 'female'
 * @param {number} sumAssured - Sum Assured for the year
 * @returns {number} Annual risk fee
 */
function calcRiskFee(age, gender, sumAssured) {
  if (!RISK_RATES[gender] || RISK_RATES[gender][age] === undefined) {
    return 0;
  }
  return RISK_RATES[gender][age] * sumAssured / 1000;
}

/**
 * Calculates the loyalty bonus for a given contract year.
 * Bonus is awarded at milestone years (10, 15, 20):
 *   bonus = (ageAtYear / 100) * firstYearPremium
 * Returns 0 for non-milestone years.
 * @param {number} year - Contract year (1-based)
 * @param {number} ageAtYear - Customer's age at this contract year
 * @param {number} firstYearPremium - First year basic premium
 * @returns {number} Loyalty bonus amount
 */
function calcLoyaltyBonus(year, ageAtYear, firstYearPremium) {
  if (LOYALTY_MILESTONES.indexOf(year) === -1) {
    return 0;
  }
  return (ageAtYear / 100) * firstYearPremium;
}

// ─── Projection Engine ──────────────────────────────────────────────────────

/**
 * Calculates the death benefit for a given year.
 * Death benefit = max(Account Value, Sum Assured)
 * @param {number} accountValue - Current account value
 * @param {number} sumAssured - Current sum assured
 * @returns {number} Death benefit amount
 */
function calcDeathBenefit(accountValue, sumAssured) {
  return Math.max(accountValue, sumAssured);
}

/**
 * Calculates the TPD (Total Permanent Disability) benefit.
 * Same as death benefit if age ≤ 75, null otherwise.
 * @param {number} accountValue - Current account value
 * @param {number} sumAssured - Current sum assured
 * @param {number} age - Customer's current age
 * @returns {number|null} TPD benefit amount or null if age > 75
 */
function calcTPDBenefit(accountValue, sumAssured, age) {
  if (age > 75) {
    return null;
  }
  return Math.max(accountValue, sumAssured);
}

/**
 * Formats a number as Vietnamese currency string with dot separators and " VND" suffix.
 * @param {number} amount - The amount to format
 * @returns {string} Formatted string, e.g. "28.570.000 VND"
 */
function formatVND(amount) {
  var rounded = Math.round(amount);
  if (rounded === 0) {
    return '0 VND';
  }
  var isNegative = rounded < 0;
  var absVal = Math.abs(rounded);
  var str = absVal.toString();
  var result = '';
  var count = 0;
  for (var i = str.length - 1; i >= 0; i--) {
    if (count > 0 && count % 3 === 0) {
      result = '.' + result;
    }
    result = str[i] + result;
    count++;
  }
  return (isNegative ? '-' : '') + result + ' VND';
}

/**
 * Detects the first lapse year in a projection.
 * A lapse occurs when the account value ≤ 0 or is insufficient to cover
 * that year's risk fee + management fee.
 * @param {Object[]} rows - Array of YearRow objects
 * @param {string} avKey - Property name for account value ('accountValueHigh' or 'accountValueLow')
 * @returns {number|null} The year number of first lapse, or null if no lapse
 */
function detectLapse(rows, avKey) {
  for (var i = 0; i < rows.length; i++) {
    var row = rows[i];
    var av = row[avKey];
    if (av <= 0) {
      return row.year;
    }
    if (av < row.riskFee + row.managementFee) {
      return row.year;
    }
  }
  return null;
}

/**
 * Main projection engine. Computes year-by-year account value projection
 * for both high and low return scenarios, up to 40 years or until both lapse.
 * @param {Object} params - InputParams object
 * @returns {Object} ProjectionResult: { rows, lapseYearHigh, lapseYearLow, inputParams }
 */
function projectAccountValue(params) {
  var maxYear = 40;
  var baseSA = params.basicPremium; // SA based on basic premium
  var saSchedule = calcSumAssuredSchedule(baseSA, maxYear);

  var rows = [];
  var prevAVHigh = 0;
  var prevAVLow = 0;
  var lapsedHigh = false;
  var lapsedLow = false;
  var lapseYearHigh = null;
  var lapseYearLow = null;

  for (var year = 1; year <= maxYear; year++) {
    // Stop if both scenarios have lapsed
    if (lapsedHigh && lapsedLow) {
      break;
    }

    var currentAge = params.age + year - 1;

    // Stop if age exceeds 99
    if (currentAge > 99) {
      break;
    }

    var sa = saSchedule[year];
    var premiumPaid = (year <= params.paymentYears) ? params.basicPremium : 0;
    var initialFee = (year <= params.paymentYears) ? calcInitialFee(year, params.basicPremium) : 0;
    var amountInvested = premiumPaid - initialFee;
    var managementFee = calcManagementFee(year);
    var riskFee = calcRiskFee(currentAge, params.gender, sa);

    // Loyalty bonus — only if the respective scenario hasn't lapsed
    var loyaltyBonusHigh = 0;
    var loyaltyBonusLow = 0;
    if (!lapsedHigh) {
      loyaltyBonusHigh = calcLoyaltyBonus(year, currentAge, params.basicPremium);
    }
    if (!lapsedLow) {
      loyaltyBonusLow = calcLoyaltyBonus(year, currentAge, params.basicPremium);
    }

    // HIGH scenario
    var accountValueHigh;
    if (lapsedHigh) {
      accountValueHigh = 0;
    } else {
      accountValueHigh = prevAVHigh * (1 + params.highRate) + amountInvested - riskFee - managementFee + loyaltyBonusHigh;
      if (accountValueHigh <= 0) {
        accountValueHigh = 0;
        lapsedHigh = true;
        lapseYearHigh = year;
      }
    }

    // LOW scenario
    var accountValueLow;
    if (lapsedLow) {
      accountValueLow = 0;
    } else {
      accountValueLow = prevAVLow * (1 + params.lowRate) + amountInvested - riskFee - managementFee + loyaltyBonusLow;
      if (accountValueLow <= 0) {
        accountValueLow = 0;
        lapsedLow = true;
        lapseYearLow = year;
      }
    }

    // Use the common loyalty bonus for the row display (use high scenario value as representative)
    var loyaltyBonus = (!lapsedHigh || !lapsedLow) ? calcLoyaltyBonus(year, currentAge, params.basicPremium) : 0;

    // Benefits
    var deathBenefitHigh = lapsedHigh ? 0 : calcDeathBenefit(accountValueHigh, sa);
    var deathBenefitLow = lapsedLow ? 0 : calcDeathBenefit(accountValueLow, sa);
    var tpdBenefitHigh = lapsedHigh ? null : calcTPDBenefit(accountValueHigh, sa, currentAge);
    var tpdBenefitLow = lapsedLow ? null : calcTPDBenefit(accountValueLow, sa, currentAge);

    rows.push({
      year: year,
      age: currentAge,
      premiumPaid: premiumPaid,
      initialFee: initialFee,
      amountInvested: amountInvested,
      riskFee: riskFee,
      managementFee: managementFee,
      loyaltyBonus: loyaltyBonus,
      accountValueHigh: accountValueHigh,
      accountValueLow: accountValueLow,
      sumAssured: sa,
      deathBenefitHigh: deathBenefitHigh,
      deathBenefitLow: deathBenefitLow,
      tpdBenefitHigh: tpdBenefitHigh,
      tpdBenefitLow: tpdBenefitLow,
      lapsedHigh: lapsedHigh,
      lapsedLow: lapsedLow,
    });

    prevAVHigh = accountValueHigh;
    prevAVLow = accountValueLow;
  }

  return {
    rows: rows,
    lapseYearHigh: lapseYearHigh,
    lapseYearLow: lapseYearLow,
    inputParams: params,
  };
}

// ─── Rendering Functions (browser-only) ─────────────────────────────────────

/**
 * renderTable(projection) — builds HTML table with year-by-year data.
 * Highlights lapse years with .lapse-row class.
 * Vietnamese column headers.
 */
function renderTable(projection) {
  var container = document.getElementById('projection-table-container');
  if (!container) return;

  var rows = projection.rows;
  var html = '<table>';
  html += '<thead><tr>';
  html += '<th>Năm</th>';
  html += '<th>Tuổi</th>';
  html += '<th>Phí đóng</th>';
  html += '<th>Phí ban đầu</th>';
  html += '<th>Đầu tư</th>';
  html += '<th>Phí rủi ro</th>';
  html += '<th>Phí quản lý</th>';
  html += '<th>Thưởng duy trì</th>';
  html += '<th>GTTKC</th>';
  html += '<th>GTTKT</th>';
  html += '<th>STBH</th>';
  html += '</tr></thead>';
  html += '<tbody>';

  for (var i = 0; i < rows.length; i++) {
    var r = rows[i];
    var cls = (r.lapsedHigh || r.lapsedLow) ? ' class="lapse-row"' : '';
    html += '<tr' + cls + '>';
    html += '<td>' + r.year + '</td>';
    html += '<td>' + r.age + '</td>';
    html += '<td>' + formatVND(Math.round(r.premiumPaid)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.initialFee)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.amountInvested)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.riskFee)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.managementFee)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.loyaltyBonus)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.accountValueHigh)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.accountValueLow)) + '</td>';
    html += '<td>' + formatVND(Math.round(r.sumAssured)) + '</td>';
    html += '</tr>';
  }

  html += '</tbody></table>';
  container.innerHTML = html;
}

/**
 * renderAccountChart(projection) — draws Canvas line chart with high/low scenario lines.
 * Axis labels in Vietnamese. Green line = high, orange line = low.
 */
function renderAccountChart(projection) {
  var canvas = document.getElementById('account-chart');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  var rows = projection.rows;
  if (rows.length === 0) return;

  // Size canvas to container
  var containerWidth = canvas.parentElement.clientWidth || 600;
  var canvasWidth = Math.max(containerWidth, 400);
  var canvasHeight = 350;
  canvas.width = canvasWidth;
  canvas.height = canvasHeight;

  // Chart area with padding
  var padLeft = 90;
  var padRight = 30;
  var padTop = 30;
  var padBottom = 50;
  var chartW = canvasWidth - padLeft - padRight;
  var chartH = canvasHeight - padTop - padBottom;

  // Data ranges
  var maxVal = 0;
  for (var i = 0; i < rows.length; i++) {
    if (rows[i].accountValueHigh > maxVal) maxVal = rows[i].accountValueHigh;
    if (rows[i].accountValueLow > maxVal) maxVal = rows[i].accountValueLow;
  }
  if (maxVal === 0) maxVal = 1;
  // Round up to nice number
  var magnitude = Math.pow(10, Math.floor(Math.log10(maxVal)));
  maxVal = Math.ceil(maxVal / magnitude) * magnitude;

  var numYears = rows.length;

  // Helper: data to pixel
  function xPos(idx) { return padLeft + (idx / Math.max(numYears - 1, 1)) * chartW; }
  function yPos(val) { return padTop + chartH - (val / maxVal) * chartH; }

  // Clear
  ctx.clearRect(0, 0, canvasWidth, canvasHeight);

  // Grid lines and Y axis labels
  ctx.strokeStyle = '#e0e0e0';
  ctx.lineWidth = 1;
  ctx.fillStyle = '#555';
  ctx.font = '11px sans-serif';
  ctx.textAlign = 'right';
  var gridSteps = 5;
  for (var g = 0; g <= gridSteps; g++) {
    var gVal = (maxVal / gridSteps) * g;
    var gy = yPos(gVal);
    ctx.beginPath();
    ctx.moveTo(padLeft, gy);
    ctx.lineTo(canvasWidth - padRight, gy);
    ctx.stroke();
    // Label in millions
    var label = Math.round(gVal / 1000000) + 'tr';
    ctx.fillText(label, padLeft - 8, gy + 4);
  }

  // X axis labels
  ctx.textAlign = 'center';
  ctx.fillStyle = '#555';
  var xStep = Math.max(1, Math.floor(numYears / 10));
  for (var xi = 0; xi < numYears; xi += xStep) {
    var xx = xPos(xi);
    ctx.fillText('Năm ' + rows[xi].year, xx, canvasHeight - padBottom + 20);
  }
  // Always show last year
  if ((numYears - 1) % xStep !== 0) {
    ctx.fillText('Năm ' + rows[numYears - 1].year, xPos(numYears - 1), canvasHeight - padBottom + 20);
  }

  // Draw high scenario line (green)
  ctx.strokeStyle = '#00a758';
  ctx.lineWidth = 2;
  ctx.beginPath();
  for (var h = 0; h < numYears; h++) {
    var hx = xPos(h);
    var hy = yPos(rows[h].accountValueHigh);
    if (h === 0) ctx.moveTo(hx, hy);
    else ctx.lineTo(hx, hy);
  }
  ctx.stroke();

  // Draw low scenario line (orange)
  ctx.strokeStyle = '#ff9800';
  ctx.lineWidth = 2;
  ctx.beginPath();
  for (var l = 0; l < numYears; l++) {
    var lx = xPos(l);
    var ly = yPos(rows[l].accountValueLow);
    if (l === 0) ctx.moveTo(lx, ly);
    else ctx.lineTo(lx, ly);
  }
  ctx.stroke();

  // Axis lines
  ctx.strokeStyle = '#999';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(padLeft, padTop);
  ctx.lineTo(padLeft, padTop + chartH);
  ctx.lineTo(canvasWidth - padRight, padTop + chartH);
  ctx.stroke();

  // Legend
  var legendX = padLeft + 10;
  var legendY = padTop + 10;
  // High
  ctx.fillStyle = '#00a758';
  ctx.fillRect(legendX, legendY, 16, 3);
  ctx.fillStyle = '#333';
  ctx.font = '12px sans-serif';
  ctx.textAlign = 'left';
  ctx.fillText('Kịch bản cao', legendX + 22, legendY + 5);
  // Low
  ctx.fillStyle = '#ff9800';
  ctx.fillRect(legendX, legendY + 18, 16, 3);
  ctx.fillStyle = '#333';
  ctx.fillText('Kịch bản thấp', legendX + 22, legendY + 23);
}

/**
 * renderFeeChart(projection) — renders CSS stacked bar chart showing
 * initial fee, management fee, risk fee per year.
 */
function renderFeeChart(projection) {
  var container = document.getElementById('fee-chart-container');
  if (!container) return;

  var rows = projection.rows;
  // Show first 15 years or until all fees are 0
  var maxBars = Math.min(rows.length, 15);
  var displayRows = [];
  for (var i = 0; i < maxBars; i++) {
    var r = rows[i];
    var total = r.initialFee + r.managementFee + r.riskFee;
    if (total > 0 || i < (projection.inputParams.paymentYears || 5) + 2) {
      displayRows.push(r);
    }
  }

  // Find max total for scaling
  var maxTotal = 0;
  for (var j = 0; j < displayRows.length; j++) {
    var t = displayRows[j].initialFee + displayRows[j].managementFee + displayRows[j].riskFee;
    if (t > maxTotal) maxTotal = t;
  }
  if (maxTotal === 0) maxTotal = 1;

  var html = '';
  for (var k = 0; k < displayRows.length; k++) {
    var row = displayRows[k];
    var initPct = (row.initialFee / maxTotal) * 100;
    var mgmtPct = (row.managementFee / maxTotal) * 100;
    var riskPct = (row.riskFee / maxTotal) * 100;

    html += '<div class="fee-bar-label">Năm ' + row.year + '</div>';
    html += '<div class="fee-bar">';
    if (initPct > 0) {
      html += '<div class="fee-initial" style="width:' + initPct.toFixed(1) + '%" title="Phí ban đầu: ' + formatVND(Math.round(row.initialFee)) + '"></div>';
    }
    if (mgmtPct > 0) {
      html += '<div class="fee-management" style="width:' + mgmtPct.toFixed(1) + '%" title="Phí quản lý: ' + formatVND(Math.round(row.managementFee)) + '"></div>';
    }
    if (riskPct > 0) {
      html += '<div class="fee-risk" style="width:' + riskPct.toFixed(1) + '%" title="Phí rủi ro: ' + formatVND(Math.round(row.riskFee)) + '"></div>';
    }
    html += '</div>';
  }

  // Legend
  html += '<div class="fee-legend">';
  html += '<div class="fee-legend-item"><span class="fee-swatch" style="background:#ff9800"></span> Phí ban đầu</div>';
  html += '<div class="fee-legend-item"><span class="fee-swatch" style="background:#42a5f5"></span> Phí quản lý</div>';
  html += '<div class="fee-legend-item"><span class="fee-swatch" style="background:#ef5350"></span> Phí rủi ro</div>';
  html += '</div>';

  container.innerHTML = html;
}

/**
 * renderBenefits(projection) — updates benefits section with death benefit,
 * TPD benefit, rider summary, and lapse warnings.
 */
function renderBenefits(projection) {
  var container = document.getElementById('benefits-container');
  if (!container) return;

  var rows = projection.rows;
  var params = projection.inputParams;
  var html = '';

  // Lapse warnings
  if (projection.lapseYearHigh !== null) {
    var lapseRowH = rows[projection.lapseYearHigh - 1];
    html += '<div class="lapse-warning">⚠ Kịch bản cao: Hợp đồng mất hiệu lực vào năm thứ ' + projection.lapseYearHigh + ' (tuổi ' + (lapseRowH ? lapseRowH.age : '?') + ')</div>';
  }
  if (projection.lapseYearLow !== null) {
    var lapseRowL = rows[projection.lapseYearLow - 1];
    html += '<div class="lapse-warning">⚠ Kịch bản thấp: Hợp đồng mất hiệu lực vào năm thứ ' + projection.lapseYearLow + ' (tuổi ' + (lapseRowL ? lapseRowL.age : '?') + ')</div>';
  }
  if (projection.lapseYearHigh === null && projection.lapseYearLow === null) {
    html += '<div class="benefit-card"><p>✓ Hợp đồng duy trì hiệu lực trong suốt 40 năm ở cả hai kịch bản.</p></div>';
  }

  // Latest active year benefits
  var lastRow = rows[rows.length - 1];
  if (lastRow) {
    // Death benefit card
    html += '<div class="benefit-card">';
    html += '<h4>Quyền lợi tử vong</h4>';
    html += '<p>Kịch bản cao: ' + formatVND(Math.round(lastRow.deathBenefitHigh)) + '</p>';
    html += '<p>Kịch bản thấp: ' + formatVND(Math.round(lastRow.deathBenefitLow)) + '</p>';
    html += '</div>';

    // TPD benefit card
    html += '<div class="benefit-card">';
    html += '<h4>Quyền lợi thương tật toàn bộ vĩnh viễn</h4>';
    if (lastRow.tpdBenefitHigh !== null) {
      html += '<p>Kịch bản cao: ' + formatVND(Math.round(lastRow.tpdBenefitHigh)) + '</p>';
      html += '<p>Kịch bản thấp: ' + formatVND(Math.round(lastRow.tpdBenefitLow !== null ? lastRow.tpdBenefitLow : 0)) + '</p>';
    } else {
      html += '<p>Không áp dụng (tuổi trên 75)</p>';
    }
    html += '</div>';
  }

  // Rider summary cards
  for (var i = 0; i < RIDERS.length; i++) {
    var rider = RIDERS[i];
    html += '<div class="benefit-card">';
    html += '<h4>' + rider.name + ' — ' + rider.desc + '</h4>';
    html += '<p>' + rider.benefits + '</p>';
    html += '</div>';
  }

  // Rider premium
  var riderPremium = DEFAULTS.totalPremium - params.basicPremium;
  html += '<div class="benefit-card">';
  html += '<h4>Phí sản phẩm bổ trợ hàng năm</h4>';
  html += '<p>' + formatVND(Math.round(riderPremium)) + '</p>';
  html += '</div>';

  container.innerHTML = html;
}

// ─── Recalculate (master function) ──────────────────────────────────────────

/**
 * Master recalculation function: collectInputs → validateInputs → projectAccountValue → render all.
 * Shows validation errors inline when invalid; updates all result sections when valid.
 */
function recalculate() {
  try {
    var params = collectInputs();
    var validation = validateInputs(params);

  var ageError = document.getElementById('age-error');
  var premiumError = document.getElementById('premium-error');
  var ageInput = document.getElementById('age');
  var premiumInput = document.getElementById('basic-premium');
  var placeholder = document.getElementById('results-placeholder');
  var projectionSection = document.getElementById('projection-section');
  var chartSection = document.getElementById('chart-section');
  var feeSection = document.getElementById('fee-section');
  var benefitsSection = document.getElementById('benefits-section');

  if (!validation.valid) {
    // Show error messages
    var ageMsg = '';
    var premiumMsg = '';
    for (var i = 0; i < validation.errors.length; i++) {
      if (validation.errors[i].indexOf('Tuổi') === 0) {
        ageMsg = validation.errors[i];
      }
      if (validation.errors[i].indexOf('Phí') === 0) {
        premiumMsg = validation.errors[i];
      }
    }

    if (ageError) ageError.textContent = ageMsg;
    if (premiumError) premiumError.textContent = premiumMsg;
    if (ageInput) {
      if (ageMsg) { ageInput.classList.add('invalid'); } else { ageInput.classList.remove('invalid'); }
    }
    if (premiumInput) {
      if (premiumMsg) { premiumInput.classList.add('invalid'); } else { premiumInput.classList.remove('invalid'); }
    }

    // Show placeholder, hide results
    if (placeholder) placeholder.style.display = 'block';
    if (projectionSection) projectionSection.style.display = 'none';
    if (chartSection) chartSection.style.display = 'none';
    if (feeSection) feeSection.style.display = 'none';
    if (benefitsSection) benefitsSection.style.display = 'none';
    return;
  }

  // Valid — clear errors
  if (ageError) ageError.textContent = '';
  if (premiumError) premiumError.textContent = '';
  if (ageInput) ageInput.classList.remove('invalid');
  if (premiumInput) premiumInput.classList.remove('invalid');

  // Hide placeholder, show results
  if (placeholder) placeholder.style.display = 'none';
  if (projectionSection) projectionSection.style.display = 'block';
  if (chartSection) chartSection.style.display = 'block';
  if (feeSection) feeSection.style.display = 'block';
  if (benefitsSection) benefitsSection.style.display = 'block';

  // Run projection and render
  var result = projectAccountValue(params);
  renderTable(result);
  renderAccountChart(result);
  renderFeeChart(result);
  renderBenefits(result);
  } catch (e) {
    console.error('recalculate error:', e);
  }
}

// ─── Event Wiring ───────────────────────────────────────────────────────────

if (typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', function() {
    var inputs = ['age', 'gender', 'basic-premium', 'payment-years', 'fund'];
    inputs.forEach(function(id) {
      var el = document.getElementById(id);
      if (el) {
        el.addEventListener('input', recalculate);
        el.addEventListener('change', recalculate);
      }
    });
    // Initial calculation on page load
    recalculate();
  });
}

// ─── Exports ────────────────────────────────────────────────────────────────
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    collectInputs: collectInputs,
    validateInputs: validateInputs,
    calcSumAssuredSchedule: calcSumAssuredSchedule,
    calcInitialFee: calcInitialFee,
    calcManagementFee: calcManagementFee,
    calcRiskFee: calcRiskFee,
    calcLoyaltyBonus: calcLoyaltyBonus,
    calcDeathBenefit: calcDeathBenefit,
    calcTPDBenefit: calcTPDBenefit,
    formatVND: formatVND,
    detectLapse: detectLapse,
    projectAccountValue: projectAccountValue,
  };
}
if (typeof window !== 'undefined') {
  window.collectInputs = collectInputs;
  window.validateInputs = validateInputs;
  window.calcSumAssuredSchedule = calcSumAssuredSchedule;
  window.calcInitialFee = calcInitialFee;
  window.calcManagementFee = calcManagementFee;
  window.calcRiskFee = calcRiskFee;
  window.calcLoyaltyBonus = calcLoyaltyBonus;
  window.calcDeathBenefit = calcDeathBenefit;
  window.calcTPDBenefit = calcTPDBenefit;
  window.formatVND = formatVND;
  window.detectLapse = detectLapse;
  window.projectAccountValue = projectAccountValue;
  window.renderTable = renderTable;
  window.renderAccountChart = renderAccountChart;
  window.renderFeeChart = renderFeeChart;
  window.renderBenefits = renderBenefits;
  window.recalculate = recalculate;
}
