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
  var storySection = document.getElementById('story-section');

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
    if (storySection) storySection.style.display = 'none';
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
  if (storySection) storySection.style.display = 'block';

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
    // Initialize story player
    initStoryPlayer();
  });
}

// ─── Story Animation Engine ─────────────────────────────────────────────────

function buildScenarios() {
  // Use current input params for dynamic numbers
  var params;
  try { params = collectInputs(); } catch(e) {
    params = { age: DEFAULTS.age, gender: DEFAULTS.gender, basicPremium: DEFAULTS.basicPremium,
      totalPremium: DEFAULTS.totalPremium, paymentYears: DEFAULTS.paymentYears, fundId: DEFAULTS.fundId,
      highRate: 0.07, lowRate: 0.013 };
  }
  var result = projectAccountValue(params);
  var rows = result.rows;

  function rowAt(y) { return rows[y - 1] || rows[rows.length - 1]; }
  function vnd(n) { return formatVND(Math.round(n)); }

  var r3 = rowAt(3);
  var r10 = rowAt(10);
  var r15 = rowAt(15);
  var r20 = rowAt(20);
  var r30 = rowAt(30);
  var rLast = rows[rows.length - 1];

  var scenarios = {
    'early-death': [
      { icon: '👨‍👩‍👧‍👦', title: 'Khởi đầu hành trình', body: 'Bạn ' + params.age + ' tuổi, quyết định bảo vệ gia đình với Xanh Tương Lai.<br>Phí bảo hiểm cơ bản: <span class="story-amount">' + vnd(params.basicPremium) + '</span>/năm trong ' + params.paymentYears + ' năm.' },
      { icon: '📋', title: 'Năm thứ 1 — Hợp đồng bắt đầu', body: 'Số tiền bảo hiểm ban đầu: <span class="story-amount">' + vnd(rows[0].sumAssured) + '</span><br>Giá trị tài khoản cuối năm 1: ' + vnd(rows[0].accountValueHigh) + ' (kịch bản cao)' },
      { icon: '⏳', title: 'Năm thứ 2–3 — Tích lũy dần', body: 'Số tiền bảo hiểm tăng 10% mỗi năm.<br>Năm thứ 3, STBH đã là: <span class="story-amount">' + vnd(r3.sumAssured) + '</span><br>Giá trị tài khoản: ' + vnd(r3.accountValueHigh) },
      { icon: '💔', title: 'Biến cố — Tử vong năm thứ 3', body: 'Điều không ai mong muốn xảy ra. Nhưng gia đình bạn được bảo vệ.' },
      { icon: '🛡️', title: 'Quyền lợi tử vong', body: 'Gia đình nhận được số tiền lớn hơn giữa giá trị tài khoản và số tiền bảo hiểm:<br><span class="story-highlight story-amount">' + vnd(r3.deathBenefitHigh) + '</span><br><br>Đây là lá chắn tài chính cho những người bạn yêu thương.' },
      { icon: '🏥', title: 'Thêm quyền lợi bổ trợ', body: 'Nếu tử vong do bệnh hiểm nghèo, gia đình còn nhận thêm:<br>• Lá Chắn Xanh: <span class="story-highlight">200 triệu VND</span> (giai đoạn muộn)<br>• Tổng quyền lợi có thể lên đến <span class="story-amount">' + vnd(r3.deathBenefitHigh + 200000000) + '</span>' },
      { icon: '💚', title: 'Ý nghĩa', body: 'Chỉ sau <span class="story-highlight">3 năm đóng phí</span>, tổng phí đã đóng là ' + vnd(params.basicPremium * 3) + '.<br><br>Nhưng gia đình nhận được <span class="story-amount">' + vnd(r3.deathBenefitHigh) + '</span>.<br>Bảo hiểm không phải chi phí — đó là tình yêu được lượng hóa.' },
    ],
    'mid-death': [
      { icon: '🌿', title: 'Hành trình 15 năm', body: 'Bạn bắt đầu ở tuổi ' + params.age + '. Sau 15 năm kiên trì, tài khoản đã tích lũy đáng kể.' },
      { icon: '📈', title: 'Tài khoản tăng trưởng', body: 'Giá trị tài khoản năm thứ 15:<br>Kịch bản cao: <span class="story-amount">' + vnd(r15.accountValueHigh) + '</span><br>Kịch bản thấp: ' + vnd(r15.accountValueLow) },
      { icon: '🎁', title: 'Thưởng duy trì năm thứ 10', body: 'Vì duy trì hợp đồng đến năm thứ 10, bạn đã nhận thưởng:<br><span class="story-highlight">' + vnd(calcLoyaltyBonus(10, params.age + 9, params.basicPremium)) + '</span><br>(= tuổi ' + (params.age + 9) + ' / 100 × phí năm đầu)' },
      { icon: '🎁', title: 'Thưởng duy trì năm thứ 15', body: 'Tiếp tục nhận thưởng tại mốc 15 năm:<br><span class="story-highlight">' + vnd(calcLoyaltyBonus(15, params.age + 14, params.basicPremium)) + '</span><br>Tổng thưởng duy trì đã nhận: <span class="story-amount">' + vnd(calcLoyaltyBonus(10, params.age + 9, params.basicPremium) + calcLoyaltyBonus(15, params.age + 14, params.basicPremium)) + '</span>' },
      { icon: '💔', title: 'Biến cố — Tử vong năm thứ 15', body: 'Ở tuổi ' + r15.age + ', điều không may xảy ra.' },
      { icon: '🛡️', title: 'Quyền lợi cho gia đình', body: 'Quyền lợi tử vong = max(Giá trị tài khoản, Số tiền bảo hiểm):<br><span class="story-highlight story-amount">' + vnd(r15.deathBenefitHigh) + '</span><br><br>Sau 15 năm, giá trị tài khoản đã vượt xa số tiền bảo hiểm ban đầu.' },
      { icon: '💚', title: 'Tổng kết', body: 'Tổng phí đã đóng (' + params.paymentYears + ' năm): <span class="story-amount">' + vnd(params.basicPremium * params.paymentYears) + '</span><br>Gia đình nhận: <span class="story-highlight story-amount">' + vnd(r15.deathBenefitHigh) + '</span><br><br>Thời gian và lãi kép đã nhân giá trị bảo vệ lên nhiều lần.' },
    ],
    'critical-illness': [
      { icon: '💪', title: '10 năm khỏe mạnh', body: 'Bạn đóng phí đầy đủ ' + params.paymentYears + ' năm và duy trì hợp đồng.<br>Năm thứ 10, giá trị tài khoản: <span class="story-amount">' + vnd(r10.accountValueHigh) + '</span>' },
      { icon: '🏥', title: 'Phát hiện bệnh hiểm nghèo', body: 'Năm thứ 10, ở tuổi ' + r10.age + ', bạn được chẩn đoán bệnh hiểm nghèo giai đoạn muộn.' },
      { icon: '🛡️', title: 'Lá Chắn Xanh kích hoạt', body: 'Quyền lợi bệnh hiểm nghèo giai đoạn muộn:<br><span class="story-highlight story-amount">200.000.000 VND</span><br><br>Số tiền này giúp bạn trang trải chi phí điều trị ngay lập tức.' },
      { icon: '🏨', title: 'Nằm viện điều trị', body: 'Dự Phòng Xanh hỗ trợ thêm:<br><span class="story-highlight">200.000 VND/ngày</span> nằm viện<br><br>30 ngày nằm viện = <span class="story-amount">6.000.000 VND</span> hỗ trợ thêm.' },
      { icon: '📊', title: 'Hợp đồng chính vẫn duy trì', body: 'Giá trị tài khoản vẫn tiếp tục tăng trưởng.<br>Quyền lợi tử vong vẫn được bảo vệ: <span class="story-amount">' + vnd(r10.deathBenefitHigh) + '</span><br><br>Bảo hiểm chính không bị ảnh hưởng bởi quyền lợi bổ trợ.' },
      { icon: '💚', title: 'Tổng quyền lợi đã nhận', body: 'Bệnh hiểm nghèo: <span class="story-highlight">200 triệu VND</span><br>Hỗ trợ nằm viện: 6 triệu VND<br>Thưởng duy trì năm 10: ' + vnd(calcLoyaltyBonus(10, params.age + 9, params.basicPremium)) + '<br><br>Và hợp đồng chính vẫn bảo vệ gia đình bạn.' },
    ],
    'long-term': [
      { icon: '🌱', title: 'Sức mạnh của thời gian', body: 'Hãy xem điều gì xảy ra khi bạn kiên trì duy trì hợp đồng trong 30 năm.' },
      { icon: '💰', title: 'Giai đoạn đóng phí', body: 'Bạn đóng phí ' + params.paymentYears + ' năm, tổng: <span class="story-amount">' + vnd(params.basicPremium * params.paymentYears) + '</span><br><br>Sau đó, tài khoản tự tăng trưởng nhờ lãi đầu tư.' },
      { icon: '🎁', title: 'Ba lần thưởng duy trì', body: 'Năm 10: <span class="story-highlight">' + vnd(calcLoyaltyBonus(10, params.age + 9, params.basicPremium)) + '</span><br>Năm 15: <span class="story-highlight">' + vnd(calcLoyaltyBonus(15, params.age + 14, params.basicPremium)) + '</span><br>Năm 20: <span class="story-highlight">' + vnd(calcLoyaltyBonus(20, params.age + 19, params.basicPremium)) + '</span>' },
      { icon: '📈', title: 'Năm thứ 20', body: 'Giá trị tài khoản:<br>Kịch bản cao: <span class="story-amount">' + vnd(r20.accountValueHigh) + '</span><br>Kịch bản thấp: ' + vnd(r20.accountValueLow) + '<br><br>Tuổi: ' + r20.age },
      { icon: '🚀', title: 'Năm thứ 30', body: 'Giá trị tài khoản:<br>Kịch bản cao: <span class="story-highlight story-amount">' + vnd(r30.accountValueHigh) + '</span><br>Kịch bản thấp: ' + vnd(r30.accountValueLow) + '<br><br>Tuổi: ' + r30.age },
      { icon: '🛡️', title: 'Quyền lợi bảo vệ', body: 'Quyền lợi tử vong năm 30: <span class="story-amount">' + vnd(r30.deathBenefitHigh) + '</span>' + (r30.tpdBenefitHigh !== null ? '<br>Quyền lợi thương tật: ' + vnd(r30.tpdBenefitHigh) : '<br>Quyền lợi thương tật: Không áp dụng (tuổi > 75)') },
      { icon: '💚', title: 'Kết luận', body: 'Tổng phí đã đóng: <span class="story-amount">' + vnd(params.basicPremium * params.paymentYears) + '</span><br>Giá trị tài khoản sau 30 năm: <span class="story-highlight story-amount">' + vnd(r30.accountValueHigh) + '</span><br><br>Lãi kép biến khoản phí nhỏ thành tài sản lớn.' },
    ],
    'lapse': [
      { icon: '⚠️', title: 'Khi nào hợp đồng mất hiệu lực?', body: 'Hợp đồng mất hiệu lực khi giá trị tài khoản không đủ trả phí rủi ro và phí quản lý.' },
      { icon: '📉', title: 'Yếu tố ảnh hưởng', body: '• <span class="story-warn">Tuổi cao</span> → phí rủi ro tăng mạnh<br>• <span class="story-warn">Phí đóng thấp</span> → tích lũy ít<br>• <span class="story-warn">Thời hạn đóng ngắn</span> → ít năm nạp tiền<br>• <span class="story-warn">Lợi nhuận thấp</span> → tăng trưởng chậm' },
      { icon: '📊', title: 'Với thông số hiện tại', body: (result.lapseYearLow !== null ? 'Kịch bản thấp: Hợp đồng <span class="story-warn">mất hiệu lực năm thứ ' + result.lapseYearLow + '</span> (tuổi ' + (params.age + result.lapseYearLow - 1) + ')' : 'Kịch bản thấp: <span class="story-highlight">Hợp đồng duy trì 40 năm</span>') + '<br><br>' + (result.lapseYearHigh !== null ? 'Kịch bản cao: Mất hiệu lực năm thứ ' + result.lapseYearHigh : 'Kịch bản cao: <span class="story-highlight">Hợp đồng duy trì 40 năm</span>') },
      { icon: '💡', title: 'Cách tránh mất hiệu lực', body: '• Đóng phí cao hơn để tích lũy nhiều hơn<br>• Chọn quỹ có lợi nhuận kỳ vọng cao hơn<br>• Đóng phí 5 năm thay vì 3 năm<br>• Bắt đầu sớm khi phí rủi ro còn thấp' },
      { icon: '🔍', title: 'So sánh phí rủi ro', body: 'Phí rủi ro tăng theo tuổi:<br>Tuổi 30: ' + vnd(calcRiskFee(30, params.gender, rows[0].sumAssured)) + '/năm<br>Tuổi 50: ' + vnd(calcRiskFee(50, params.gender, rows[0].sumAssured * 1.5)) + '/năm<br>Tuổi 70: ' + vnd(calcRiskFee(70, params.gender, rows[0].sumAssured * 1.5)) + '/năm<br><br>Đây là lý do hợp đồng có thể mất hiệu lực ở tuổi cao.' },
      { icon: '💚', title: 'Lời khuyên', body: 'Hãy thử thay đổi các thông số ở bảng trên để xem ảnh hưởng đến thời điểm mất hiệu lực.<br><br>Một kế hoạch tài chính tốt bắt đầu từ việc hiểu rõ sản phẩm.' },
    ],
  };
  return scenarios;
}

function initStoryPlayer() {
  var player = document.getElementById('story-player');
  var buttons = document.getElementById('scenario-buttons');
  if (!player || !buttons) return;

  var slides = [];
  var currentSlide = 0;
  var autoTimer = null;
  var paused = false;
  var AUTO_INTERVAL = 6000;

  var slideIcon = document.getElementById('story-slide-icon');
  var slideTitle = document.getElementById('story-slide-title');
  var slideBody = document.getElementById('story-slide-body');
  var slideNum = document.getElementById('story-slide-number');
  var progressFill = document.getElementById('story-progress-fill');
  var prevBtn = document.getElementById('story-prev');
  var pauseBtn = document.getElementById('story-pause');
  var nextBtn = document.getElementById('story-next');
  var closeBtn = document.getElementById('story-close');

  function showSlide(idx) {
    if (idx < 0 || idx >= slides.length) return;
    currentSlide = idx;
    var s = slides[idx];

    // Re-trigger animation by cloning
    slideIcon.style.animation = 'none';
    slideTitle.style.animation = 'none';
    slideBody.style.animation = 'none';
    void slideIcon.offsetHeight;
    slideIcon.style.animation = '';
    slideTitle.style.animation = '';
    slideBody.style.animation = '';

    slideIcon.textContent = s.icon;
    slideTitle.textContent = s.title;
    slideBody.innerHTML = s.body;
    slideNum.textContent = (idx + 1) + ' / ' + slides.length;
    progressFill.style.width = ((idx + 1) / slides.length * 100) + '%';

    prevBtn.disabled = idx === 0;
  }

  function startAuto() {
    stopAuto();
    paused = false;
    pauseBtn.textContent = '⏸ Tạm dừng';
    autoTimer = setInterval(function() {
      if (currentSlide < slides.length - 1) {
        showSlide(currentSlide + 1);
      } else {
        stopAuto();
      }
    }, AUTO_INTERVAL);
  }

  function stopAuto() {
    if (autoTimer) { clearInterval(autoTimer); autoTimer = null; }
  }

  function playScenario(scenarioId) {
    var scenarios = buildScenarios();
    slides = scenarios[scenarioId] || [];
    if (slides.length === 0) return;

    // Highlight active button
    var allBtns = buttons.querySelectorAll('.scenario-btn');
    for (var i = 0; i < allBtns.length; i++) {
      allBtns[i].classList.toggle('active', allBtns[i].getAttribute('data-scenario') === scenarioId);
    }

    player.style.display = 'block';
    showSlide(0);
    startAuto();
    player.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // Scenario button clicks
  var scenarioBtns = buttons.querySelectorAll('.scenario-btn');
  for (var i = 0; i < scenarioBtns.length; i++) {
    scenarioBtns[i].addEventListener('click', function() {
      playScenario(this.getAttribute('data-scenario'));
    });
  }

  prevBtn.addEventListener('click', function() { stopAuto(); showSlide(currentSlide - 1); });
  nextBtn.addEventListener('click', function() { stopAuto(); showSlide(currentSlide + 1); });
  pauseBtn.addEventListener('click', function() {
    if (paused) { startAuto(); }
    else { stopAuto(); paused = true; pauseBtn.textContent = '▶ Tiếp tục'; }
  });
  closeBtn.addEventListener('click', function() {
    stopAuto();
    player.style.display = 'none';
    var allBtns = buttons.querySelectorAll('.scenario-btn');
    for (var j = 0; j < allBtns.length; j++) { allBtns[j].classList.remove('active'); }
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
