#!/usr/bin/env python3
"""Write curriculum 3 (urban planning) session 1 to the D2 generator file."""

content = '''
# ============================================================================
# 3. URBAN PLANNING — Quy Hoạch Đô Thị
# desc_tone: vivid_scenario | farewell_tone: practical_momentum
# ============================================================================
cur_urban_planning = {
    "title": "Quy Ho\u1EA1ch \u0110\u00F4 Th\u1ECB",
    "display_order": 3,
    "desc_tone": "vivid_scenario",
    "farewell_tone": "practical_momentum",
    "description": (
        "H\u00C3Y T\u01AF\u1EDENG T\u01AF\u1EE2NG B\u1EA0N \u0110\u1EEENG TR\u00CAN \u0110\u1ED2I MONTMARTRE, NH\u00CCN XU\u1ED0NG PARIS "
        "V\u1EDAI NH\u1EEENG \u0110\u1EA0I L\u1ED8 HAUSSMANN TH\u1EB2NG T\u1EAEP \u2014 V\u00C0 B\u1EA0N HI\u1EC2U T\u1EA0I SAO CH\u00DANG \u1EDE \u0110\u00D3.\\n\\n"
        "M\u1ED7i th\u00E0nh ph\u1ED1 l\u00E0 m\u1ED9t b\u1EA3n thi\u1EBFt k\u1EBF s\u1ED1ng \u2014 t\u1EEB quartier \u0111\u1EBFn boulevard, "
        "t\u1EEB zonage \u0111\u1EBFn densit\u00E9, m\u1ED7i quy\u1EBFt \u0111\u1ECBnh quy ho\u1EA1ch \u0111\u1ECBnh h\u00ECnh cu\u1ED9c s\u1ED1ng "
        "h\u00E0ng tri\u1EC7u ng\u01B0\u1EDDi. Hi\u1EC3u quy ho\u1EA1ch \u0111\u00F4 th\u1ECB l\u00E0 hi\u1EC3u t\u1EA1i sao th\u00E0nh ph\u1ED1 "
        "c\u1EE7a b\u1EA1n tr\u00F4ng nh\u01B0 v\u1EADy.\\n\\n"
        "V\u1EDBi 18 t\u1EEB v\u1EF1ng c\u1ED1t l\u00F5i \u2014 t\u1EEB urbanisme \u0111\u1EBFn durabilit\u00E9 \u2014 b\u1EA1n s\u1EBD t\u1EF1 tin "
        "\u0111\u1ECDc t\u00E0i li\u1EC7u quy ho\u1EA1ch, th\u1EA3o lu\u1EADn v\u1EC1 ph\u00E1t tri\u1EC3n \u0111\u00F4 th\u1ECB, "
        "v\u00E0 hi\u1EC3u c\u00E1ch c\u00E1c th\u00E0nh ph\u1ED1 Ph\u00E1p \u0111\u01B0\u1EE3c x\u00E2y d\u1EF1ng.\\n\\n"
        "\u0110\u00E2y kh\u00F4ng ch\u1EC9 l\u00E0 t\u1EEB v\u1EF1ng \u2014 \u0111\u00E2y l\u00E0 b\u1EA3n \u0111\u1ED3 ng\u00F4n ng\u1EEF c\u1EE7a th\u00E0nh ph\u1ED1."
    ),
    "preview": (
        "B\u1EA1n s\u1EBD b\u1EAFt \u0111\u1EA7u v\u1EDBi 6 t\u1EEB n\u1EC1n t\u1EA3ng: urbanisme (quy ho\u1EA1ch \u0111\u00F4 th\u1ECB), "
        "quartier (khu ph\u1ED1), boulevard (\u0111\u1EA1i l\u1ED9), pi\u00E9ton (ng\u01B0\u1EDDi \u0111i b\u1ED9), "
        "densit\u00E9 (m\u1EADt \u0111\u1ED9), zonage (ph\u00E2n v\u00F9ng). Ti\u1EBFp theo, infrastructure (h\u1EA1 t\u1EA7ng), "
        "m\u00E9tropole (\u0111\u00F4 th\u1ECB l\u1EDBn), banlieue (ngo\u1EA1i \u00F4), r\u00E9novation (c\u1EA3i t\u1EA1o), "
        "espace vert (kh\u00F4ng gian xanh), circulation (giao th\u00F4ng). Cu\u1ED1i c\u00F9ng, "
        "logement (nh\u00E0 \u1EDF), patrimoine urbain (di s\u1EA3n \u0111\u00F4 th\u1ECB), mixit\u00E9 (\u0111a d\u1EA1ng), "
        "accessibilit\u00E9 (kh\u1EA3 n\u0103ng ti\u1EBFp c\u1EADn), transport (v\u1EADn t\u1EA3i), durabilit\u00E9 (b\u1EC1n v\u1EEFng). "
        "Qua 3 b\u00E0i \u0111\u1ECDc ti\u1EBFng Ph\u00E1p v\u1EC1 l\u1ECBch s\u1EED quy ho\u1EA1ch Paris, "
        "th\u00E1ch th\u1EE9c \u0111\u00F4 th\u1ECB h\u00F3a v\u00E0 th\u00E0nh ph\u1ED1 t\u01B0\u01A1ng lai, 1 ph\u1EA7n \u00F4n t\u1EADp "
        "v\u00E0 1 b\u00E0i \u0111\u1ECDc t\u1ED5ng h\u1EE3p, b\u1EA1n s\u1EBD t\u1EF1 tin th\u1EA3o lu\u1EADn v\u1EC1 \u0111\u00F4 th\u1ECB b\u1EB1ng ti\u1EBFng Ph\u00E1p."
    ),
    "vocab": [
        ["urbanisme", "quartier", "boulevard", "pi\u00E9ton", "densit\u00E9", "zonage"],
        ["infrastructure", "m\u00E9tropole", "banlieue", "r\u00E9novation", "espace vert", "circulation"],
        ["logement", "patrimoine urbain", "mixit\u00E9", "accessibilit\u00E9", "transport", "durabilit\u00E9"],
    ],
'''

with open('vi-fr/_run_gen_d2_all.py', 'a', encoding='utf-8') as f:
    f.write(content)
print("Curriculum 3 header written")
