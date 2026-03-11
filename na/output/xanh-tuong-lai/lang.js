/**
 * lang.js — Internationalization (i18n) for Xanh Tương Lai index page
 * Supports Vietnamese (vi) and English (en)
 */

var I18N = {
  vi: {
    // Page meta
    pageTitle: 'Xanh Tương Lai – Khám phá câu chuyện bảo hiểm của bạn | Manulife Việt Nam',
    brandSub: 'Câu chuyện bảo hiểm cá nhân hóa',
    manulife: 'Manulife Việt Nam',
    sidebarToggle: '☰ Danh mục',

    // Sidebar
    sidebarTitle: 'Danh mục',
    sidebarClose: 'Đóng',
    sidebarPages: 'Trang',
    sidebarNav: 'Điều hướng',
    sidebarProducts: 'Sản phẩm Manulife',
    sidebarRiders: 'Riders',
    navStory: '📖 Câu chuyện bảo hiểm',
    navCurrent: 'Hiện tại',
    navSimulator: '📊 Mô phỏng chi trả',
    navInput: '📝 Nhập thông tin',
    navYourStory: '📖 Câu chuyện của bạn',

    // Hero
    heroTitle1: 'Khám phá câu chuyện ',
    heroTitleHighlight: 'bảo hiểm',
    heroTitle2: ' của bạn',
    heroSubtitle: 'Nhập thông tin cơ bản để nhận câu chuyện bảo hiểm được thiết kế riêng cho bạn và gia đình.',
    badge1: 'Tự động tăng STBH +50%',
    badge2: '9 quỹ liên kết đơn vị',
    badge3: 'Cá nhân hóa theo hồ sơ',
    heroVisualText: 'Câu chuyện bảo hiểm cá nhân hóa',

    // Form
    formTitle: 'Hãy cho chúng tôi biết về bạn',
    labelName: 'Tên của bạn',
    placeholderName: 'VD: Minh',
    labelAge: 'Tuổi',
    labelGender: 'Giới tính',
    genderFemale: 'Nữ',
    genderMale: 'Nam',
    labelChildren: 'Số con nhỏ',
    children0: 'Chưa có con',
    children1: '1 con',
    children2: '2 con',
    children3: '3 con trở lên',
    labelBudget: 'Ngân sách phí BH / năm',
    budget20: '20 triệu',
    budget30: '30 triệu',
    budget50: '50 triệu',
    budget80: '80 triệu',
    labelPayment: 'Thời hạn đóng phí',
    payment3: '3 năm',
    payment5: '5 năm',
    labelRisk: 'Mức chấp nhận rủi ro đầu tư',
    riskConservative: 'Thận trọng',
    riskBalanced: 'Cân bằng',
    riskGrowth: 'Tăng trưởng',
    btnStart: 'Khám phá câu chuyện của bạn →',

    // Why section
    whyTitle: 'Tại sao chọn Xanh Tương Lai?',
    why1Title: 'Bảo vệ toàn diện',
    why1Desc: 'Tử vong, TTTBVV, tăng STBH tự động +10%/năm đến +50%.',
    why2Title: 'Đầu tư linh hoạt',
    why2Desc: '9 quỹ liên kết đơn vị, chuyển đổi quỹ miễn phí.',
    why3Title: 'Tăng theo gia đình',
    why3Desc: '+5% STBH mỗi thành viên mới, tối đa +25%, không thẩm định lại.',

    // Story screen
    btnBack: '← Thay đổi thông tin',
    storyHeadingPrefix: 'Câu chuyện bảo hiểm của ',
    btnPrev: '◀ Trước',
    btnPause: '⏸ Tạm dừng',
    btnResume: '▶ Tiếp tục',
    btnNext: 'Tiếp ▶',

    // Tabs
    tabBenefits: 'Quyền lợi',
    tabRiders: 'Riders',
    tabFunds: 'Quỹ đầu tư',
    tabFaq: 'FAQ',
    tabGlossary: 'Từ điển',

    // Benefits
    benefitDeathTitle: '🛡️ Tử vong / Thương tật toàn bộ vĩnh viễn',
    benefitDeathDesc: 'Chi trả giá trị cao hơn giữa STBH và giá trị tài khoản cơ bản, cộng giá trị tài khoản đóng thêm.',
    benefitSATitle: '📈 Tăng STBH tự động',
    benefitSADesc: 'STBH tự động tăng 10% mỗi năm từ năm thứ 2 đến năm thứ 6, không cần thẩm định lại sức khỏe.',
    benefitFamilyTitle: '👨‍👩‍👧‍👦 Tăng STBH khi có thành viên mới',
    benefitFamilyDesc: 'Mỗi thành viên mới trong gia đình → STBH tăng thêm +5%, tối đa +25%.',
    benefitMaturityTitle: '📅 Đáo hạn',
    benefitMaturityDesc: 'Nhận toàn bộ giá trị tài khoản khi hợp đồng đáo hạn.',
    benefitExtraTitle: '➕ Quyền lợi bổ sung',
    benefitExtra1: 'Tạm ứng mai táng: 30 triệu VND',
    benefitExtra2: 'Ung thư tuyến giáp: 10% STBH, tối đa 100 triệu VND',
    disclaimer: 'Giá trị tài khoản và quyền lợi bảo hiểm không được đảm bảo vì phụ thuộc vào kết quả đầu tư. Giá trị tài khoản có thể tăng hoặc giảm theo biến động thị trường.',

    // Funds
    fundSpectrumLow: 'Thận trọng',
    fundSpectrumHigh: 'Mạo hiểm',
    fundRecommendPrefix: '💡 Với mức chấp nhận rủi ro của bạn, quỹ phù hợp: ',
    fundDesc: '9 quỹ đầu tư đa dạng – từ thận trọng đến mạo hiểm.',

    // Footer
    footerTitle: 'Tài liệu chính thức',
    footerProductPage: 'Trang sản phẩm',
    footerXTL: 'Xanh Tương Lai – Phí Ổn Định',
    footerRiders: 'Danh mục rider',
    footerDisclaimer: '© 2026 · Trang tham khảo. Nội dung nhằm minh họa, không phải hợp đồng bảo hiểm. Lợi nhuận không được đảm bảo.',

    // Validation
    alertAge: 'Tuổi phải từ 18 đến 60.',

    // Language toggle
    langLabel: '🇬🇧 EN',
  },

  en: {
    // Page meta
    pageTitle: 'Xanh Tương Lai – Discover Your Insurance Story | Manulife Vietnam',
    brandSub: 'Your personalized insurance story',
    manulife: 'Manulife Vietnam',
    sidebarToggle: '☰ Menu',

    // Sidebar
    sidebarTitle: 'Menu',
    sidebarClose: 'Close',
    sidebarPages: 'Pages',
    sidebarNav: 'Navigation',
    sidebarProducts: 'Manulife Products',
    sidebarRiders: 'Riders',
    navStory: '📖 Insurance Story',
    navCurrent: 'Current',
    navSimulator: '📊 Payout Simulator',
    navInput: '📝 Enter Info',
    navYourStory: '📖 Your Story',

    // Hero
    heroTitle1: 'Discover your ',
    heroTitleHighlight: 'insurance',
    heroTitle2: ' story',
    heroSubtitle: 'Enter your basic information to receive a personalized insurance story designed for you and your family.',
    badge1: 'Auto SA increase +50%',
    badge2: '9 unit-linked funds',
    badge3: 'Personalized to your profile',
    heroVisualText: 'Your personalized insurance story',

    // Form
    formTitle: 'Tell us about yourself',
    labelName: 'Your name',
    placeholderName: 'e.g. Minh',
    labelAge: 'Age',
    labelGender: 'Gender',
    genderFemale: 'Female',
    genderMale: 'Male',
    labelChildren: 'Number of children',
    children0: 'No children',
    children1: '1 child',
    children2: '2 children',
    children3: '3 or more children',
    labelBudget: 'Annual premium budget',
    budget20: '20 million',
    budget30: '30 million',
    budget50: '50 million',
    budget80: '80 million',
    labelPayment: 'Premium payment term',
    payment3: '3 years',
    payment5: '5 years',
    labelRisk: 'Investment risk tolerance',
    riskConservative: 'Conservative',
    riskBalanced: 'Balanced',
    riskGrowth: 'Growth',
    btnStart: 'Discover your story →',

    // Why section
    whyTitle: 'Why choose Xanh Tương Lai?',
    why1Title: 'Comprehensive protection',
    why1Desc: 'Death, TPD, auto SA increase +10%/year up to +50%.',
    why2Title: 'Flexible investment',
    why2Desc: '9 unit-linked funds, free fund switching.',
    why3Title: 'Grows with your family',
    why3Desc: '+5% SA per new family member, max +25%, no re-underwriting.',

    // Story screen
    btnBack: '← Change info',
    storyHeadingPrefix: 'Insurance story of ',
    btnPrev: '◀ Prev',
    btnPause: '⏸ Pause',
    btnResume: '▶ Resume',
    btnNext: 'Next ▶',

    // Tabs
    tabBenefits: 'Benefits',
    tabRiders: 'Riders',
    tabFunds: 'Investment Funds',
    tabFaq: 'FAQ',
    tabGlossary: 'Glossary',

    // Benefits
    benefitDeathTitle: '🛡️ Death / Total Permanent Disability',
    benefitDeathDesc: 'Pays the higher of Sum Assured and basic account value, plus top-up account value.',
    benefitSATitle: '📈 Automatic SA Increase',
    benefitSADesc: 'SA automatically increases 10% per year from year 2 to year 6, no health re-assessment required.',
    benefitFamilyTitle: '👨‍👩‍👧‍👦 SA Increase for New Family Members',
    benefitFamilyDesc: 'Each new family member → SA increases by +5%, max +25%.',
    benefitMaturityTitle: '📅 Maturity',
    benefitMaturityDesc: 'Receive the full account value when the policy matures.',
    benefitExtraTitle: '➕ Additional Benefits',
    benefitExtra1: 'Funeral advance: 30 million VND',
    benefitExtra2: 'Thyroid cancer: 10% SA, max 100 million VND',
    disclaimer: 'Account value and insurance benefits are not guaranteed as they depend on investment performance. Account value may increase or decrease with market fluctuations.',

    // Funds
    fundSpectrumLow: 'Conservative',
    fundSpectrumHigh: 'Aggressive',
    fundRecommendPrefix: '💡 Based on your risk tolerance, recommended fund: ',
    fundDesc: '9 diverse investment funds – from conservative to aggressive.',

    // Footer
    footerTitle: 'Official Documents',
    footerProductPage: 'Product Page',
    footerXTL: 'Xanh Tương Lai – Stable Premium',
    footerRiders: 'Rider Catalog',
    footerDisclaimer: '© 2026 · Reference page. Content is for illustration only, not an insurance contract. Returns are not guaranteed.',

    // Validation
    alertAge: 'Age must be between 18 and 60.',

    // Language toggle
    langLabel: '🇻🇳 VI',
  }
};

// Glossary translations
var GLOSSARY_EN = {
  "ILP": "Unit-linked insurance – a product combining risk protection and investment through funds.",
  "SA (Sum Assured)": "Sum Assured – the maximum protection amount stated in the policy.",
  "TPD": "Total Permanent Disability – complete and permanent loss of ability to work.",
  "NAV": "Net Asset Value – the value of each fund unit at a given time.",
  "Risk Fee": "A fee deducted from the account to maintain protection benefits.",
  "Account Value": "Total value of fund units you own in the policy.",
  "Unit-Linked Fund": "Investment fund where premiums are allocated; value changes with the market.",
  "Maturity": "The date when the insurance policy ends as agreed.",
  "Initial Fee": "Fee deducted from regular premiums in the early years of the policy.",
  "Stable Premium": "Total regular premium designed to remain stable throughout the expected payment period.",
  "Unit-Linked Insurance": "Life insurance product combining protection and investment through linked funds.",
  "Late Stage": "The most severe stage of critical illness as defined in the policy.",
  "Early Stage": "Critical illness detected at a milder stage.",
  "Hospital Allowance": "Daily benefit paid when the insured is hospitalized.",
  "Serious Injury": "Serious injuries from accidents covered by insurance."
};

var FAQ_EN = [
  { q: "What is ILP? Are returns guaranteed?", a: "ILP (unit-linked insurance) combines risk protection and investment. Returns are NOT guaranteed as they depend on the performance of unit-linked funds." },
  { q: "Why should I review multiple scenarios?", a: "Each scenario reflects a different assumed rate of return. Reviewing multiple scenarios helps you understand the range of possible outcomes." },
  { q: "When can the policy lapse?", a: "The policy can lapse when the account value is insufficient to cover fees. This can happen during prolonged market downturns." },
  { q: "Can I switch investment funds?", a: "Yes. You can switch between funds according to the policy terms." },
  { q: "Where can I check the NAV?", a: "You can check the daily NAV on the Manulife Vietnam website or through the ManuConnect app." }
];

var FUNDS_DATA_EN = [
  { name: "Capital Preservation", risk: 1, desc: "Government bonds and deposits." },
  { name: "Accumulation", risk: 2, desc: "Mainly bonds, small portion of equities." },
  { name: "Stability", risk: 3, desc: "Balanced between bonds and equities." },
  { name: "Balance", risk: 4, desc: "Equal allocation between bonds and equities." },
  { name: "Development", risk: 5, desc: "Higher equity allocation than bonds." },
  { name: "Growth", risk: 6, desc: "Focused on equities, high return potential." },
  { name: "Prosperity 2035", risk: 3, desc: "Auto risk reduction approaching 2035." },
  { name: "Prosperity 2040", risk: 4, desc: "Auto risk reduction approaching 2040." },
  { name: "Prosperity 2045", risk: 5, desc: "Auto risk reduction approaching 2045." }
];

var RIDERS_DATA_EN = [
  { name: "Green Shield", sub: "Critical Illness", cls: "", highlights: ["Late stage: 100% SA", "78+ late-stage illnesses", "61 early-stage illnesses", "4 special illnesses"] },
  { name: "Green Reserve", sub: "Hospital Allowance", cls: "green", highlights: ["ICU: 300% SA / day", "General ward: 100% SA / day"] },
  { name: "Green Guard", sub: "Accident", cls: "teal", highlights: ["Accidental death: 100% SA", "Disability, fractures, burns"] }
];

var FUND_RECOMMEND_EN = { 1: "Capital Preservation or Accumulation", 2: "Balance or Stability", 3: "Development or Growth" };

// Current language state
var currentLang = 'vi';

/**
 * Apply translations to all static elements with data-i18n attributes
 */
function applyLanguage(lang) {
  currentLang = lang;
  var t = I18N[lang];
  document.title = t.pageTitle;
  document.documentElement.lang = lang;

  // Apply all data-i18n text
  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var key = el.getAttribute('data-i18n');
    if (t[key] !== undefined) {
      el.textContent = t[key];
    }
  });

  // Apply data-i18n-html (for innerHTML)
  document.querySelectorAll('[data-i18n-html]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-html');
    if (t[key] !== undefined) {
      el.innerHTML = t[key];
    }
  });

  // Apply data-i18n-placeholder
  document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-placeholder');
    if (t[key] !== undefined) {
      el.placeholder = t[key];
    }
  });

  // Update language toggle button
  var langBtn = document.getElementById('lang-toggle');
  if (langBtn) langBtn.textContent = t.langLabel;

  // Re-render dynamic content
  if (typeof renderFAQ === 'function') renderFAQ();
  if (typeof renderGlossary === 'function') renderGlossary();
  if (typeof renderFunds === 'function') renderFunds();
  if (typeof renderRiders === 'function') renderRiders();
}

function toggleLanguage() {
  applyLanguage(currentLang === 'vi' ? 'en' : 'vi');
}

// Expose globally
if (typeof window !== 'undefined') {
  window.I18N = I18N;
  window.GLOSSARY_EN = GLOSSARY_EN;
  window.FAQ_EN = FAQ_EN;
  window.FUNDS_DATA_EN = FUNDS_DATA_EN;
  window.RIDERS_DATA_EN = RIDERS_DATA_EN;
  window.FUND_RECOMMEND_EN = FUND_RECOMMEND_EN;
  window.currentLang = currentLang;
  window.applyLanguage = applyLanguage;
  window.toggleLanguage = toggleLanguage;
}


/**
 * English scenario builder — called from buildScenarios() when lang is 'en'
 */
function buildScenariosEN(s, name, Name, baseSA, sa3, sa6, rate, lowRate, av10h, av10l, av15h, av20h, av30h, av30l, death3, totalPaid, familyBonus) {
  function v(n) {
    if (n >= 1e9) return (n / 1e9).toFixed(1).replace('.0', '') + ' billion VND';
    if (n >= 1e6) return Math.round(n / 1e6).toLocaleString('en') + ' million VND';
    return Math.round(n).toLocaleString('en') + ' VND';
  }
  return {
    'family-shield': {
      icon: '🛡️', title: 'Family Shield', desc: 'Protection from day one',
      slides: [
        { icon: '👨‍👩‍👧‍👦', title: Name + '\'s journey begins', body: Name + ', age ' + s.age + ', decides to protect the family with Xanh Tương Lai.<br>Premium: <span class="amount">' + v(s.budget) + '</span>/year for ' + s.paymentYears + ' years.' },
        { icon: '📋', title: 'Policy starts', body: 'Initial Sum Assured: <span class="amount">' + v(baseSA) + '</span><br>SA auto-increases 10% per year until year 6.' },
        { icon: '📈', title: 'SA growth', body: 'By year 3, SA is: <span class="amount">' + v(sa3) + '</span><br>Year 6: <span class="amount">' + v(sa6) + '</span> (+61% from initial)' },
        { icon: '💔', title: 'Event — Death in year 3', body: 'The unexpected happens. But ' + name + '\'s family is protected.' },
        { icon: '💚', title: 'Family receives', body: 'Death benefit: <span class="amount">' + v(death3) + '</span><br><br>After just 3 years of premiums (' + v(s.budget * 3) + '), the family receives many times more.<br>Insurance is not a cost — it\'s love quantified.' },
        { icon: '🏥', title: 'Additional rider benefits', body: 'With Green Shield, the family also receives:<br>• Late-stage critical illness: <span class="highlight">200 million VND</span><br>• Funeral advance: <span class="highlight">30 million VND</span>' }
      ]
    },
    'growth-journey': {
      icon: '🌱', title: 'Growth Journey', desc: 'The power of 20-year compounding',
      slides: [
        { icon: '🌿', title: 'Long-term commitment', body: Name + ' starts at age ' + s.age + '. Let\'s see what happens with long-term persistence.' },
        { icon: '💰', title: 'Premium payment phase', body: 'Paying for ' + s.paymentYears + ' years, total: <span class="amount">' + v(totalPaid) + '</span><br>After that, the account grows through investment returns.' },
        { icon: '📊', title: 'Year 10', body: 'Account value:<br>Favorable: <span class="amount">' + v(av10h) + '</span><br>Conservative: ' + v(av10l) },
        { icon: '🎁', title: 'Loyalty bonuses', body: 'Manulife rewards persistence:<br>• Year 10: loyalty bonus<br>• Year 15: loyalty bonus<br>• Year 20: loyalty bonus<br>All bonuses added to the account.' },
        { icon: '🚀', title: 'Year 20', body: 'Account value (favorable):<br><span class="amount">' + v(av20h) + '</span><br><br>' + Name + '\'s age: ' + (s.age + 19) + '. Compounding has multiplied the value significantly.' },
        { icon: '💚', title: 'Summary', body: 'Total premiums paid: <span class="amount">' + v(totalPaid) + '</span><br>Account value after 20 years: <span class="amount">' + v(av20h) + '</span><br><br>Time and compounding turn small premiums into significant assets.' }
      ]
    },
    'critical-illness': {
      icon: '🏥', title: 'Critical Illness', desc: 'Rider benefits when illness strikes',
      slides: [
        { icon: '💪', title: '10 healthy years', body: Name + ' pays premiums for ' + s.paymentYears + ' years and maintains the policy.<br>Year 10 account value: <span class="amount">' + v(av10h) + '</span>' },
        { icon: '🏥', title: 'Critical illness diagnosed', body: 'In year 10, at age ' + (s.age + 9) + ', ' + name + ' is diagnosed with late-stage critical illness.' },
        { icon: '🛡️', title: 'Green Shield activates', body: 'Late-stage critical illness benefit:<br><span class="amount">200,000,000 VND</span><br><br>This helps cover treatment costs immediately.' },
        { icon: '🏨', title: 'Hospitalization', body: 'Green Reserve provides:<br><span class="highlight">200,000 VND/day</span> hospitalization<br>ICU: <span class="highlight">600,000 VND/day</span><br><br>30 days = <span class="amount">6 million VND</span> support.' },
        { icon: '📊', title: 'Main policy continues', body: 'Account value continues to grow.<br>Death benefit remains protected.<br><br>The main policy is not affected by rider claims.' },
        { icon: '💚', title: 'Total benefits received', body: 'Critical illness: <span class="highlight">200 million VND</span><br>Hospital support: 6 million VND<br><br>And the main policy still protects ' + name + '\'s family.' }
      ]
    },
    'family-grows': {
      icon: '👶', title: 'Growing Family', desc: 'SA increases with your family',
      slides: [
        { icon: '👨‍👩‍👧', title: 'Current family', body: Name + ' currently has ' + s.children + ' child(ren).<br>Initial SA: <span class="amount">' + v(baseSA) + '</span>' },
        { icon: '👶', title: 'New members', body: 'Each new family member automatically increases SA by <span class="highlight">+5%</span> per member.' },
        { icon: '📈', title: 'Double SA increase', body: 'Combining auto 10%/year AND family increase:<br><br>Year 3 + 2 new children = SA increases by ' + v(sa3 * 0.10) + '<br>Max +25% SA from new members.' },
        { icon: '🛡️', title: 'Maximum protection', body: 'With ' + s.children + ' child(ren), SA increased by <span class="amount">+' + familyBonus + '%</span>.<br><br>Effective SA year 1: <span class="amount">' + v(baseSA * (1 + familyBonus / 100)) + '</span>' },
        { icon: '💚', title: 'What it means', body: 'Xanh Tương Lai understands that as your family grows, protection needs grow too.<br><br>No health re-assessment. No complicated procedures.' }
      ]
    },
    'what-if-lapse': {
      icon: '⚠️', title: 'What if it lapses?', desc: 'Understand risks to prevent them',
      slides: [
        { icon: '⚠️', title: 'When does a policy lapse?', body: 'A policy lapses when the account value is insufficient to cover risk fees and management fees.' },
        { icon: '📉', title: 'Contributing factors', body: '• <span class="warn">Older age</span> → risk fees increase sharply<br>• <span class="warn">Low premiums</span> → less accumulation<br>• <span class="warn">Short payment term</span> → fewer contributions<br>• <span class="warn">Low returns</span> → slow growth' },
        { icon: '📊', title: Name + '\'s parameters', body: 'Premium: ' + v(s.budget) + '/year × ' + s.paymentYears + ' years<br>Starting age: ' + s.age + '<br><br>Conservative (' + (lowRate * 100).toFixed(1) + '%): Account year 30 = ' + v(av30l) + '<br>Favorable (' + (rate * 100).toFixed(0) + '%): ' + v(av30h) },
        { icon: '💡', title: 'How to prevent lapse', body: '• Pay higher premiums for more accumulation<br>• Choose funds with higher expected returns<br>• Pay for 5 years instead of 3<br>• Start early when risk fees are low' },
        { icon: '💚', title: 'Advice for ' + name, body: 'At age ' + s.age + ' with ' + v(s.budget) + '/year, ' + (s.paymentYears === 5 ? 'you\'ve chosen a good payment term.' : 'consider paying for 5 years for more accumulation.') + '<br><br>Try changing the parameters to see the impact.' }
      ]
    }
  };
}

if (typeof window !== 'undefined') {
  window.buildScenariosEN = buildScenariosEN;
}
