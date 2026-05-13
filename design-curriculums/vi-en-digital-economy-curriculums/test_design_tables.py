"""Design-time table validation tests for the vi-en Digital Economy curriculums.

These tests validate the hand-authored design tables in design.md (vocabulary
selections, description tones, farewell registers, titles) before any
curriculum content is built. The tables live only in design.md, so they are
encoded here as Python constants — do NOT import them from another module.

If a test fails, the design itself is out of compliance with the spec. Do not
modify the constants to make tests pass; report the violation to the user and
update design.md instead.

Feature: vi-en-digital-economy-curriculums
"""

from itertools import combinations
from collections import Counter


# --------------------------------------------------------------------------
# Design tables encoded from design.md Sections 4 and 5
# --------------------------------------------------------------------------

CURRICULUMS = [
    {
        "index": 1,
        "title": "Hành Trình Của Shopee",
        "series": 1,
        "order": 1,
        "fmt": "story_reading",
        "level": "preintermediate",
        "subtopic_nouns": ["shopee"],
        "vocab_groups": [
            ["platform", "shopper", "browse", "listing", "cart"],
            ["checkout", "seller", "customer", "inventory", "growth"],
            ["marketplace", "store", "supplier", "online", "shipping"],
            ["profit", "expansion", "packaging", "transform", "journey"],
        ],
        "description_tone": "provocative_question",
        "farewell_register": "introspective_guide",
    },
    {
        "index": 2,
        "title": "Câu Chuyện Khởi Nghiệp Việt",
        "series": 1,
        "order": 2,
        "fmt": "story_reading",
        "level": "intermediate",
        "subtopic_nouns": ["khởi nghiệp"],
        "vocab_groups": [
            ["founder", "venture", "capital", "funding", "pivot"],
            ["scale", "valuation", "milestone", "ambition", "perseverance"],
            ["mentor", "ecosystem", "innovation", "breakthrough", "prototype"],
            ["investor", "equity", "traction", "unicorn", "vision"],
        ],
        "description_tone": "vivid_scenario",
        "farewell_register": "warm_accountability",
    },
    {
        "index": 3,
        "title": "Từ Tiền Mặt Đến Ví Số",
        "series": 1,
        "order": 3,
        "fmt": "story_reading",
        "level": "intermediate",
        "subtopic_nouns": ["tiền mặt", "ví số"],
        "vocab_groups": [
            ["cashless", "wallet", "transfer", "scan", "balance"],
            ["transaction", "fintech", "adoption", "convenience", "trust"],
            ["regulation", "banking", "deposit", "withdrawal", "generation"],
            ["instant", "secure", "ledger", "settlement", "peer"],
        ],
        "description_tone": "metaphor_led",
        "farewell_register": "practical_momentum",
    },
    {
        "index": 4,
        "title": "Mua Sắm Trực Tuyến",
        "series": 2,
        "order": 1,
        "fmt": "speaking",
        "level": "preintermediate",
        "subtopic_nouns": ["mua sắm"],
        "vocab_groups": [
            ["order", "item", "deliver", "package", "address"],
            ["review", "rating", "discount", "voucher", "coupon"],
            ["shipping", "payment", "confirm", "cancel", "track"],
            ["arrive", "damaged", "satisfied", "refund", "return"],
        ],
        "description_tone": "bold_declaration",
        "farewell_register": "team_building_energy",
    },
    {
        "index": 5,
        "title": "Thanh Toán Không Tiền Mặt",
        "series": 2,
        "order": 2,
        "fmt": "speaking",
        "level": "preintermediate",
        "subtopic_nouns": ["thanh toán", "tiền mặt"],
        "vocab_groups": [
            ["account", "fee", "charge", "code", "link"],
            ["send", "receive", "receipt", "history", "statement"],
            ["amount", "recharge", "confirm", "success", "error"],
            ["qr", "password", "pin", "mobile", "verify"],
        ],
        "description_tone": "empathetic_observation",
        "farewell_register": "practical_momentum",
    },
    {
        "index": 6,
        "title": "Làm Việc Từ Xa",
        "series": 2,
        "order": 3,
        "fmt": "speaking",
        "level": "preintermediate",
        "subtopic_nouns": ["làm việc"],
        "vocab_groups": [
            ["remote", "meeting", "video", "microphone", "mute"],
            ["share", "screen", "schedule", "deadline", "project"],
            ["task", "team", "manager", "colleague", "message"],
            ["reply", "available", "focus", "break", "hybrid"],
        ],
        "description_tone": "surprising_fact",
        "farewell_register": "warm_accountability",
    },
    {
        "index": 7,
        "title": "Mạng Xã Hội Và Tiếp Thị Số",
        "series": 3,
        "order": 1,
        "fmt": "balanced",
        "level": "preintermediate",
        "subtopic_nouns": ["mạng xã hội", "tiếp thị"],
        "vocab_groups": [
            ["post", "like", "follow", "comment", "content"],
            ["viral", "audience", "brand", "campaign", "influencer"],
            ["engagement", "reach", "target", "click", "banner"],
            ["promote", "channel", "trend", "hashtag", "analytics"],
        ],
        "description_tone": "provocative_question",
        "farewell_register": "quiet_awe",
    },
    {
        "index": 8,
        "title": "Tiền Mã Hoá Và Blockchain",
        "series": 3,
        "order": 2,
        "fmt": "balanced",
        "level": "intermediate",
        "subtopic_nouns": ["tiền mã hoá", "blockchain"],
        "vocab_groups": [
            ["cryptocurrency", "blockchain", "decentralized", "token", "mining"],
            ["exchange", "address", "contract", "smart", "protocol"],
            ["volatile", "speculative", "custody", "validate", "consensus"],
            ["network", "hash", "encryption", "immutable", "distributed"],
        ],
        "description_tone": "bold_declaration",
        "farewell_register": "practical_momentum",
    },
    {
        "index": 9,
        "title": "Trí Tuệ Nhân Tạo Trong Kinh Doanh",
        "series": 3,
        "order": 3,
        "fmt": "balanced",
        "level": "intermediate",
        "subtopic_nouns": ["trí tuệ nhân tạo", "kinh doanh"],
        "vocab_groups": [
            ["artificial", "intelligence", "automate", "algorithm", "model"],
            ["predict", "dataset", "training", "chatbot", "recommendation"],
            ["efficiency", "productivity", "machine", "learning", "generate"],
            ["analyze", "insight", "decision", "augment", "deploy"],
        ],
        "description_tone": "metaphor_led",
        "farewell_register": "introspective_guide",
    },
    {
        "index": 10,
        "title": "An Ninh Mạng Và Quyền Riêng Tư",
        "series": 3,
        "order": 4,
        "fmt": "balanced",
        "level": "intermediate",
        "subtopic_nouns": ["an ninh mạng", "quyền riêng tư"],
        "vocab_groups": [
            ["cyber", "security", "password", "encryption", "privacy"],
            ["breach", "hacker", "phishing", "malware", "firewall"],
            ["authentication", "vulnerable", "protect", "identity", "leak"],
            ["scam", "fraud", "sensitive", "consent", "threat"],
        ],
        "description_tone": "vivid_scenario",
        "farewell_register": "team_building_energy",
    },
]

SERIES_TONES = {
    1: "vivid_scenario",
    2: "empathetic_observation",
    3: "bold_declaration",
}

FORBIDDEN_LEVEL_SUBSTRINGS = [
    "beginner", "preintermediate", "intermediate", "upper-intermediate", "advanced",
    "sơ cấp", "sơ trung cấp", "trung cấp", "cao trung cấp", "nâng cao",
    "a1", "a2", "b1", "b2", "c1", "c2",
]


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def _full_vocab(curriculum):
    """Return the full 20-word lowercased vocabList for a curriculum."""
    words = []
    for group in curriculum["vocab_groups"]:
        words.extend(w.lower() for w in group)
    return words


def _curriculums_in_series(series_number):
    """Return curriculums in a series ordered by display order."""
    return sorted(
        [c for c in CURRICULUMS if c["series"] == series_number],
        key=lambda c: c["order"],
    )


# --------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------

def test_vocab_pairwise_overlap_at_most_2():
    """Validates: Requirement 2.3a — pairwise vocab overlap ≤ 2."""
    vocab_sets = {c["index"]: set(_full_vocab(c)) for c in CURRICULUMS}
    for a, b in combinations(CURRICULUMS, 2):
        shared = vocab_sets[a["index"]] & vocab_sets[b["index"]]
        assert len(shared) <= 2, (
            f"Curriculums {a['index']} ({a['title']}) and "
            f"{b['index']} ({b['title']}) share {len(shared)} words "
            f"(> 2): {sorted(shared)}"
        )


def test_vocab_word_frequency_at_most_2():
    """Validates: Requirement 2.3b — no single word appears in >2 curriculums."""
    word_curricula = Counter()
    for c in CURRICULUMS:
        # Count each unique word once per curriculum.
        for word in set(_full_vocab(c)):
            word_curricula[word] += 1
    over = {w: n for w, n in word_curricula.items() if n > 2}
    assert not over, (
        f"Words appearing in more than 2 curriculums: {over}"
    )


def test_description_tone_distribution_max_3():
    """Validates: Requirement 6.6 — no description tone is used more than 3 times."""
    counts = Counter(c["description_tone"] for c in CURRICULUMS)
    over = {t: n for t, n in counts.items() if n > 3}
    assert not over, (
        f"Description tones used more than 3 times: {over}"
    )


def test_description_tone_no_adjacent_within_series():
    """Validates: Requirement 6.5 — adjacent curriculums in a series use different description tones."""
    for series_num in (1, 2, 3):
        ordered = _curriculums_in_series(series_num)
        for prev, curr in zip(ordered, ordered[1:]):
            assert prev["description_tone"] != curr["description_tone"], (
                f"Series {series_num}: adjacent curriculums "
                f"{prev['index']} ({prev['title']}) and "
                f"{curr['index']} ({curr['title']}) share description tone "
                f"'{prev['description_tone']}'"
            )


def test_farewell_register_per_series_no_adjacent():
    """Validates: Requirement 8.8 — adjacent curriculums in a series use different farewell registers."""
    for series_num in (1, 2, 3):
        ordered = _curriculums_in_series(series_num)
        for prev, curr in zip(ordered, ordered[1:]):
            assert prev["farewell_register"] != curr["farewell_register"], (
                f"Series {series_num}: adjacent curriculums "
                f"{prev['index']} ({prev['title']}) and "
                f"{curr['index']} ({curr['title']}) share farewell register "
                f"'{prev['farewell_register']}'"
            )


def test_farewell_register_count_in_range_1_to_3():
    """Validates: Requirement 8.9 — each farewell register used appears 1-3 times."""
    counts = Counter(c["farewell_register"] for c in CURRICULUMS)
    out_of_range = {r: n for r, n in counts.items() if not (1 <= n <= 3)}
    assert not out_of_range, (
        f"Farewell registers outside [1, 3]: {out_of_range}"
    )


def test_series_description_tones_all_distinct():
    """Validates: Requirement 13.7 — the 3 series description tones are all distinct."""
    tones = list(SERIES_TONES.values())
    assert len(set(tones)) == len(tones), (
        f"Series description tones must all be distinct, got: {SERIES_TONES}"
    )


def test_curriculum_titles_word_and_char_bounds():
    """Validates: Requirement 7.1 — titles are 2-8 words and ≤ 50 chars."""
    for c in CURRICULUMS:
        title = c["title"]
        word_count = len(title.split())
        assert 2 <= word_count <= 8, (
            f"Curriculum {c['index']} title '{title}' has {word_count} words "
            f"(must be 2-8)"
        )
        assert len(title) <= 50, (
            f"Curriculum {c['index']} title '{title}' is {len(title)} chars "
            f"(must be ≤ 50)"
        )


def test_curriculum_titles_no_forbidden_level_substrings():
    """Validates: Requirement 7.3 — titles contain no level indicators (case-insensitive)."""
    for c in CURRICULUMS:
        title_lower = c["title"].lower()
        for forbidden in FORBIDDEN_LEVEL_SUBSTRINGS:
            assert forbidden not in title_lower, (
                f"Curriculum {c['index']} title '{c['title']}' contains "
                f"forbidden level substring '{forbidden}'"
            )


def test_curriculum_titles_unique():
    """Validates: Requirement 7.5 — all 10 titles are unique."""
    titles = [c["title"] for c in CURRICULUMS]
    duplicates = [t for t, n in Counter(titles).items() if n > 1]
    assert not duplicates, f"Duplicate titles: {duplicates}"


def test_subtopic_noun_coverage():
    """Validates: Requirement 7.4 — each title contains a subtopic noun or vocab word."""
    for c in CURRICULUMS:
        title_lower = c["title"].lower()
        vocab = _full_vocab(c)
        has_subtopic_noun = any(noun.lower() in title_lower for noun in c["subtopic_nouns"])
        has_vocab_word = any(word in title_lower for word in vocab)
        assert has_subtopic_noun or has_vocab_word, (
            f"Curriculum {c['index']} title '{c['title']}' contains neither "
            f"a subtopic noun {c['subtopic_nouns']} nor any vocab word"
        )
