const fs = require("fs");

const input = fs.readFileSync("unengaged_campaign_emails.csv", "utf-8");
const lines = input.trim().split("\n");
const header = lines[0];
const rows = lines.slice(1);

// Vietnamese TLD domains
const vnDomainRe = /\.vn$/i;

// Common Vietnamese surnames as email prefix patterns
// Kept conservative — these are unambiguously Vietnamese
// Vietnamese names to search ANYWHERE in the email prefix
// Longer patterns first to avoid false substring matches
const vnNamesAnywhere = [
  // Multi-syllable / compound patterns (check these first)
  "nguyen", "phuong", "truong", "khanh", "thanh", "phuoc", "huong",
  "nhung", "quang", "trong", "tuong", "thuan", "huyen", "tuyet",
  "thinh", "quyen", "trieu", "xuyen", "nhien", "khang", "phong",
  "thien", "duong", "vuong", "luong", "trinh", "phung", "ngoc",
  "nhat", "trang", "suong", "cuong", "giang", "diep", "dieu",
  "khoi", "khoa", "vinh", "binh", "cong", "kien", "lien",
  "luan", "nhan", "phat", "thao", "thong", "toan", "truc",
  "sang", "sinh", "hieu", "tuan", "hung", "nhut", "oanh",
  "loan", "hanh", "uyen", "xuan", "minh", "linh", "huynh",
  "hoang", "pham", "tran", "phan", "doan",
  // Shorter but distinctive Vietnamese names
  "phuc", "thuy", "viet", "dang", "chau", "nghi", "quoc",
  "khue", "ngan", "hien", "hong", "huong", "trung",
  "tien", "thinh", "tam", "hoa", "dat", "yen", "nhi",
  "anh", "thu", "huy", "phu", "kim", "bao", "duc",
  "gia", "hai", "han", "kha", "lam", "mai", "dao",
  "thai", "ngo", "bui", "nam", "son", "tai", "tin",
  "tri", "van", "nga", "nhu", "tra", "tram", "loc",
  "lan", "chi", "duy", "hue", "quy", "thi",
  "vy", "ha", "my", "le", "vo", "do", "tu", "vu",
];

// Vietnamese words/phrases in email prefixes
const vnPhrases = [
  "chucmayman", "betai", "conthienchua", "choigame", "cuncon",
  "hocanhvan", "dangnhap", "buonviyeu", "lopduoc", "lopqtvn",
  "taikhoansave", "monkeytramy", "bibonguyen", "babykibo",
  "kentolachong", "kipdenno", "befly", "bemeotinhnghich",
  "hoasenngoai", "cuccutvuive", "congiodaudong", "phatkhongbocuoc",
  "nhacuahieu", "nhachungce", "tatakhd", "quatchituhoa",
  "thiensu", "buonviyeuanh", "dangnhappokemon",
  "khongcoten", "khonglancinh", "saigon", "bophan", "vanphong",
  "marketingani", "gaubong", "heodong", "nhoktien", "kiemhack",
  "muahang", "shoputcung", "tcutisthegioi", "taikhoansave",
  "mieubangnhi", "suatiettrung", "bachlykinhhong", "laidangtonbao",
  "nguyetdachivuong", "callmephuong", "quancuaai", "wuocsu",
  "cakhongnghiep", "khungkhung", "hiepsi", "toontran",
  "sgacon", "camhong", "tinvatrang", "viennhathy",
  "anniebaongoc", "bichnghi", "diepthaonguyen", "conannguyenhoang",
  "kainguyen", "aririshoang", "saphyhoangtuan", "annagiahannguyen",
  "toilanhuan", "honthuybinh", "nguyetsakuno", "takamitran",
  "aiikyysraumuong", "boithyluu", "callmemonn", "gincaido",
  "lolznhatthuy", "userthanhsang", "cocghe", "pquanghai",
  "kirigayakazuto", "mingmong", "khiel", "ntla",
  "singdoonger", "fujiwarakatori", "laituyetphung", "ngloctran",
  "kenutit", "nghivo", "heodong", "nhachungceteve",
  "qcuonghcmut", "vioengamer", "diepthan", "caovinhtrong",
  "hoconl", "zerovanniss", "hanbangtuyet", "tatuyetanh",
  "giftnguyen", "thnguyen", "bacnguyet", "tovongochan",
  "kingtrongtuonglai", "trancham", "nokiaphong", "krystal.tran",
  "btran", "dainghiatruong", "nmhoang", "tkanh",
  "dthai", "nghiatrung", "bhan", "dphatthieu", "tquang",
  "nttn", "lhp.ngan", "anvy", "quocduy", "nthung",
  "t.minhhuy", "ntmp", "hanmay", "daiduong", "ngtrhan",
  "vhktram", "belinhne", "ngvy", "hdinh", "ttmlinh",
  "dxhanh", "toducanh", "nttongon", "ntamchipp",
  "sdinh", "vndt", "contactcnvcg", "kitekidz",
  "nkhoi", "anvy", "katylgh", "nngon",
  "bangtanbangtan", "tbaotrann", "hduocsu", "kimomoi",
  "hhunney", "1976anhphuong", "ashleyphan", "kailhuynh",
  "npttrang", "kngoc", "joker.minh", "okeynhat",
  "thypham", "huathaihuy", "hwanglu",
  "laidangtonbao", "covendg", "ptrang",
  "lolznhatthuyz", "userthanhsang", "nhinguyen",
  "ngthanhvan", "nhutnguyen", "danghythien",
  "alychuu", "hunghan", "ashleyphan", "strawberries0903",
  "camhong", "thangpham", "quancuaai", "wuocsu",
  "danhcptube", "nhhai", "ntran", "yuikymc",
  "yen.hachi", "masachan", "pm0314", "tmd11473",
  "littletittle", "jsap", "nhp1495", "hoducmien",
  "cakhongnghiep", "kiet4333", "neco00100", "seha.tvu",
  "hanhomf", "myhanhtruong", "cambinh", "pnttram",
  "testacctho", "danhtruongg", "chuhieunguyet",
  "boramonc", "bivo", "finntaki", "aimeehonganh",
  "hothithuanbinh", "lymyhoangtho", "nvthoai",
  "aamachitwan", "trancanhkhanh", "lsmzhznxuxmxbxbx",
  "bemeotinhnghich", "phamthihonghanh", "nhatysai",
  "lehongbaongoc", "phuclh", "hoasenngoai", "uynguyen",
  "haanhgg", "demondarkhome", "baonhipham",
  "bncanhtoan", "cutenoiseuwu", "bacnguyet",
  "tovongochann", "thang75204", "luctruong",
  "quanha", "kennykute", "nguyenyenbkc",
  "caovankhanh", "enashinonome", "nhuthao",
  "thienbinhp", "btrambtram", "vnnext.lethong",
  "hoangngan", "khanhvy.lee", "tuando",
  "caothingochan", "starlivechettiet", "ngathuyhuynh",
  "dasoundbakery", "annaninhhong", "khoianhvu",
  "phantuongvi", "xuannghido", "xuantruong",
  "buiducnhan", "bhgaminh", "vaananhnt",
  "trantuansong", "maixuanhong", "camly",
  "tq.sang", "thangpham", "maiha", "minhnam",
  "pnqt", "honghanhmj", "chinchin",
  "tranthicamtu", "thaind", "vothiminhle",
  "nghiemnguyen", "09049324778nhan", "loutrang",
  "viennhathy", "ththao", "shoputcung",
  "tcutisthegioi", "dtuyetnhiii", "beanhben",
  "gamnguyen", "huynhchikhang", "pkchu",
  "ginhee", "luuduyvuvn", "bapngan",
  "kthuwww", "luchuongtam", "lhdt",
  "justinduy", "kdiedutablet", "diu.ha",
  "elvitran", "vovanthong", "ngoh",
  "shin30252", "arigatoozm", "clari.hayquenacc",
  "hlehanhtiendl", "qgiao", "nhh113644",
  "tnpl.loctran", "quocdungdmx", "tvrepcomment",
  "phothingocminh", "duynguyen12412", "hoa13fb",
  "dayyhan", "goodking", "ntth21203",
  "lenguyenhoanglong", "thuyngatesting", "ngothiloan",
  "nngocnhi", "hoangmaian", "nguyet.trantm",
  "nk510404", "changhyblue", "kira1412az",
  "luonthimit", "benheo", "cloudyluong",
  "anhue", "aidieu", "dungle",
  "kinayoshimina", "coffeemilk", "vngamer",
  "knga", "ntt23082004", "hnam",
  "nanh332003", "huynhhainguyen", "bibonguyen",
  "caothiquynhhuong", "nghiaasaki", "oreol",
  "narudo", "tr.th.q.mai", "jdsstella",
  "ntdac", "kiritopgb", "hoikhu",
  "tdl050905", "quynhhuongtruong", "rehnumamostofa",
  "buivuanhthu", "daodoan", "nyanlinnnyanlin",
  "tubinh", "pduyenttytcg", "nguyenthoai",
  "tonlenhatlam", "nguyenanhquoc", "huynhnguyenthienkim",
  "qnhatnguyen", "chogaukieng", "conconmini",
  "dunglucky", "tanh01112009",
  "diepdiep", "mr.nguyenvancan", "nguyetnga",
  "phi2003.com", "minirene", "nnbich",
  "susutamanh", "hoangtieumieu", "nguyenphat",
  "harkdhanuk", "jieku", "testinvest",
  "dominikglas", "djnxnfjekrkfjfndndbcbffkfkei",
  "trantran", "dangngocnhuy", "vuhanhatanh",
  "dominhthu", "nguyenthianhtuyetkdi", "trannguyenkhanhha",
  "huynhthianhthu", "nhatminh14062002", "vuthuhuong",
  "duongthy", "yenhuynh", "nhuphuc2008ghim",
  "tienhoascp", "nhube", "alvinpham",
  "huynhbaoduy", "ngoctrieu", "anbyl",
  "tuananh654", "tuan.anh.170893", "duongtna",
  "rumaafrin", "chibisama", "omegax2003",
  "shanibro", "hieutrungng", "nhiqueens",
  "yesterday241", "phuongthuy", "nhhai",
  "tranthuyyenvi", "tdcaldwell", "thanhnhan05102k4",
  "namduong", "hr.hpec", "sonhang",
  "huynhngochan", "nguyenluan", "trantung",
  "ntran9333", "hongtan", "yen.hachi",
  "hongle", "masachan", "lamquangduyy",
  "pm0314305", "scoobydooszero", "asadulali",
  "tmd11473", "nguyenhoangha", "littletittle",
  "an.nguyenduc", "viet170221mp", "jsap2004",
  "trannguyenhue", "dharsourabh", "vy.hu20p0410",
  "nhp1495", "eamin", "nhihuynhhuynh",
  "hoducmien", "kiet4333", "neco00100",
  "seha.tvu", "tranankhanga", "hanhomf",
  "myhanhtruong", "akelaram", "mobilesmriti",
  "thunek", "trungchinhle", "atien_yuppie",
  "danhtruongg", "cumagularmani", "phamngockhaluannon",
  "thuhienn", "trantuanphong", "cambinh",
  "phancg", "tranthingoctran", "hoanglong",
  "tranduyhungnn", "pnttram", "nhatchauduong",
  "testacctho", "truongminhkhoi", "isbackk",
  "kimngandethuong", "thanhzuki",
  "semon.21cenmodgal", "aminataj", "cchk251100",
  "kelseyan", "chuhieunguyet", "nguyenducanh",
  "nguyenthilongnhi", "boramonc", "nguyenthiphuongvy",
  "japhetkiplangat", "trangnguyencherry", "kalisgula",
  "vuanh", "duongtrungkien", "playstorecnx",
  "onbao9205nbk", "bivo14082004hk", "nguyenthanhson",
  "finntaki", "aimeehonganh", "hothithuanbinh",
  "furqan90aslam", "lymyhoangtho", "bannam2002",
  "nvthoai", "giaobl", "hafizakhatun",
  "svastonanimestore", "trancanhkhanh",
  "lehuy", "wiliamsama", "lethungsg",
  "kimanh20050915", "bemeotinhnghich", "phuongngothuc",
  "takiwithstudy", "phamthihonghanh", "nhatysai",
  "thuandoan", "lehongbaongoc", "ticklinghentai",
  "phuclh", "hoasenngoai", "uynguyen",
  "haanhgg", "baonhipham",
];

function matchesVnPrefix(prefix) {
  const lower = prefix.toLowerCase();
  
  // Check Vietnamese phrases/compound words anywhere
  for (const p of vnPhrases) {
    if (lower.includes(p)) return true;
  }
  
  // Check Vietnamese names anywhere in prefix
  for (const n of vnNamesAnywhere) {
    if (lower.includes(n)) return true;
  }
  
  return false;
}

// Vietnamese diacritics in name field
const vnDiacriticRe = /[ăắằẳẵặâấầẩẫậđêếềểễệôốồổỗộơớờởỡợưứừửữựĂẮẰẲẴẶÂẤẦẨẪẬĐÊẾỀỂỄỆÔỐỒỔỖỘƠỚỜỞỠỢƯỨỪỬỮỰ]/;

// Known Vietnamese institution domains (without .vn, or subdomains)
const vnInstitutionDomains = [
  "kdi.edu.vn",
  "huemed-univ.edu.vn",
  "hcmut.edu.vn",
  "hcmuaf.edu.vn",
  "hcmussh.edu.vn",
  "hce.edu.vn",
  "nttu.edu.vn",
  "ldxh.edu.vn",
  "siu.edu.vn",
  "nsl.edu.vn",
  "lttc.edu.vn",
  "ut.edu.vn",
  "hueuni.edu.vn",
  "st.uel.edu.vn",
  "st.vimaru.edu.vn",
  "ispschools.edu.vn",
  "ilamail.edu.vn",
  "student.tdtu.edu.vn",
];

function isVietnamese(email, name) {
  const domain = email.split("@")[1] || "";
  const prefix = email.split("@")[0] || "";

  // 1. Vietnamese domain
  if (vnDomainRe.test(domain)) return true;

  // 2. Known Vietnamese institution
  if (vnInstitutionDomains.some((d) => domain.endsWith(d))) return true;

  // 3. Vietnamese diacritics in name
  if (name && vnDiacriticRe.test(name)) return true;

  // 4. Vietnamese name pattern in email prefix
  if (matchesVnPrefix(prefix)) return true;

  return false;
}

const vnRows = [];
const intlRows = [];

for (const line of rows) {
  // Parse CSV: email,"name",created_at
  const firstComma = line.indexOf(",");
  const lastComma = line.lastIndexOf(",");
  const email = line.substring(0, firstComma);
  const name = line.substring(firstComma + 1, lastComma).replace(/^"|"$/g, "");
  
  if (isVietnamese(email, name)) {
    vnRows.push(line);
  } else {
    intlRows.push(line);
  }
}

fs.writeFileSync("unengaged_vn.csv", [header, ...vnRows].join("\n"), "utf-8");
fs.writeFileSync("unengaged_intl.csv", [header, ...intlRows].join("\n"), "utf-8");

console.log(`Total: ${rows.length}`);
console.log(`Vietnamese: ${vnRows.length}`);
console.log(`International: ${intlRows.length}`);
