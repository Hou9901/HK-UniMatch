# ==========================================================
# Hong Kong Master Match System (Optimized for Real Admissions)
# All Majors Optimized: Business / STEM / Media / Arts / Social
# Real HK University Admission Standards + Priority Recommendation
# Optimized Version: Auto-tiering + Granular GPA/IELTS + Priority for Hot Majors
# ==========================================================

# ======================= GLOBAL UNIVERSITY TIERS =======================
UNIVERSITY_TIERS = {
    "T0": [
        "北京大学", "清华大学", "复旦大学", "上海交通大学",
        "浙江大学", "中国科学技术大学", "南京大学", "中国人民大学",
        "香港中文大学（深圳）", "香港科技大学（广州）",
        "上海纽约大学", "昆山杜克大学"
    ],
    "T1": [
        "北京航空航天大学", "北京理工大学", "北京师范大学", "中国农业大学",
        "同济大学", "南开大学", "天津大学", "哈尔滨工业大学", "吉林大学",
        "大连理工大学", "西安交通大学", "西北工业大学", "兰州大学", "山东大学",
        "武汉大学", "华中科技大学", "中南大学", "湖南大学", "四川大学",
        "电子科技大学", "重庆大学", "中山大学", "华南理工大学", "厦门大学",
        "东南大学", "中央民族大学", "西北农林科技大学", "中国海洋大学", "东北大学",
        "上海财经大学", "中央财经大学", "对外经济贸易大学", "中国政法大学",
        "北京外国语大学", "上海外国语大学", "中国传媒大学", "北京邮电大学",
        "西安电子科技大学", "南京航空航天大学", "南京理工大学",
        "香港城市大学（东莞）", "南方科技大学", "上海科技大学"
    ],
    "T2": [
        "华东理工大学", "东华大学", "上海大学", "北京科技大学", "北京化工大学",
        "北京林业大学", "北京中医药大学", "华北电力大学", "中国矿业大学",
        "中国石油大学", "中国地质大学", "北京工业大学", "北京交通大学",
        "天津医科大学", "河北工业大学", "太原理工大学", "辽宁大学", "大连海事大学",
        "东北师范大学", "哈尔滨工程大学", "苏州大学", "河海大学", "江南大学",
        "南京农业大学", "中国药科大学", "南京师范大学", "安徽大学", "合肥工业大学",
        "福州大学", "南昌大学", "郑州大学", "武汉理工大学", "华中农业大学",
        "华中师范大学", "中南财经政法大学", "湖南师范大学", "暨南大学",
        "华南师范大学", "西南大学", "西南交通大学", "西南财经大学",
        "西北大学", "长安大学", "陕西师范大学",
        "贵州大学", "云南大学", "广西大学",         "海南大学",
        "深圳大学", "浙江工业大学", "江苏大学", "南京工业大学",
        "福建师范大学", "广东工业大学", "杭州电子科技大学",
        "南京信息工程大学", "南京邮电大学", "南京林业大学",
        "宁波大学", "浙江师范大学", "首都师范大学",         "扬州大学",
        "北师香港浸会大学", "西交利物浦大学", "宁波诺丁汉大学",
    ],
    "T3": [
         "四川农业大学", "东北农业大学", "东北林业大学",
        "西藏大学", "青海大学", "宁夏大学", "新疆大学",
        "石河子大学", "延边大学", "内蒙古大学",
        "深圳北理莫斯科大学", "广东以色列理工学院", "温州肯恩大学",
        "山西大学", "华南农业大学", "山东师范大学",
        "广州大学", "上海理工大学", "青岛大学",
        "燕山大学", "昆明理工大学", "西安理工大学",
        "浙江理工大学", "杭州师范大学", "湘潭大学",
        "西安建筑科技大学", "西南石油大学", "湖北大学",
        "福建农林大学", "上海师范大学", "武汉科技大学",
        "江西师范大学", "成都理工大学", "山东农业大学",
        "温州大学", "河北大学", "陕西科技大学",
        "天津工业大学", "长沙理工大学", "长春理工大学",
        "华侨大学", "山东科技大学", "江苏科技大学",
        "上海海洋大学", "安徽农业大学", "中北大学",
        "安徽师范大学", "河南农业大学", "重庆邮电大学",
        "南通大学", "广西师范大学", "浙江农林大学",
        "齐鲁工业大学", "中国计量大学", "沈阳农业大学",
        "西北师范大学", "黑龙江大学", "集美大学",
        "天津科技大学", "武汉纺织大学", "天津师范大学",
        "吉林农业大学", "湖北工业大学", "辽宁师范大学",
        "曲阜师范大学", "常州大学", "湖南农业大学",
        "青岛科技大学", "河南师范大学", "武汉工程大学",
        "天津理工大学", "上海海事大学", "江苏师范大学",
        "汕头大学", "三峡大学", "济南大学",
        "河南科技大学", "河北师范大学", "北京建筑大学",
        "沈阳航空航天大学", "安徽理工大学", "南昌航空大学",
        "北京信息科技大学", "桂林电子科技大学", "长江大学",
        "国际关系学院", "西安科技大学", "青岛理工大学",
        "上海电力大学", "河北农业大学", "湖南科技大学",
        "重庆交通大学", "兰州交通大学", "安徽工业大学",
        "河南理工大学", "华东交通大学", "西安邮电大学",
        "山东理工大学", "南华大学", "沈阳工业大学",
        "云南师范大学"
    ]
}

# ======================= SPECIAL SCHOOLS (Field-Specific Excellence) =======================
BUSINESS_SPECIAL = ["东北财经大学", "江西财经大学", "浙江工商大学", "南京财经大学", "南京审计大学", "山东财经大学", "天津财经大学", "首都经济贸易大学", "上海对外经贸大学"]
STEM_SPECIAL = ["杭州电子科技大学", "南京邮电大学", "重庆邮电大学", "浙江工业大学", "广东工业大学", "江苏大学", "深圳大学", "天津工业大学", "成都理工大学", "上海理工大学", "南京工业大学", "西安邮电大学"]
MEDIA_SPECIAL = ["浙江传媒学院", "四川传媒学院", "南京传媒学院", "武汉传媒学院", "北京电影学院", "上海视觉艺术学院"]
ARTS_SPECIAL = ["四川外国语大学", "西安外国语大学", "广东外语外贸大学", "天津外国语大学", "外交学院", "北京语言大学", "首都师范大学", "山东师范大学", "福建师范大学"]
SOCIAL_SPECIAL = ["西北政法大学", "西南政法大学", "华东政法大学", "上海政法学院", "山东政法学院", "中国青年政治学院", "中国社会科学院大学"]
# ======================= 1. Business  =======================
# - GPA scaled to 4.0 (real HK unis prioritize 3.0+/4.0 as baseline for top programs)
# - IELTS: Hot majors require 7.0+ (real cutoff for HKU/CUHK Business), cold majors 6.0+ (minimum for admission)
# - Tier-based competitiveness (T3 unis need higher GPA/IELTS to compensate for school ranking)
BUSINESS_MAJORS = {
    "hot": ["Master of Finance", "Master of Accounting", "Business Analytics", "FinTech", "Marketing", "International Business"],
    "cold": ["Supply Chain Management", "Human Resource Management", "Operations Management", "Tourism and Hospitality Management", "Public Finance", "Entrepreneurship Management"]
}
BUSINESS_RULES = {
    "T0": {"hot": {"Top3": [3.5, 3.8, 7.0, 7.5], "Top5": [3.2, 3.5, 6.5, 7.0], "All8": [3.0, 3.3, 6.0, 6.5]},
          "cold": {"Top3": [3.3, 3.6, 6.5, 7.0], "Top5": [3.0, 3.3, 6.0, 6.5], "All8": [2.8, 3.1, 6.0, 6.0]}},
    "T1": {"hot": {"Top3": [3.6, 3.9, 7.0, 7.5], "Top5": [3.3, 3.6, 6.5, 7.0], "All8": [3.1, 3.4, 6.0, 6.5]},
          "cold": {"Top3": [3.4, 3.7, 6.5, 7.0], "Top5": [3.1, 3.4, 6.0, 6.5], "All8": [2.9, 3.2, 6.0, 6.0]}},
    "T2": {"hot": {"Top3": [3.7, 4.0, 7.0, 7.5], "Top5": [3.4, 3.7, 6.5, 7.0], "All8": [3.2, 3.5, 6.5, 7.0]},
          "cold": {"Top3": [3.5, 3.8, 6.5, 7.0], "Top5": [3.2, 3.5, 6.0, 6.5], "All8": [3.0, 3.3, 6.0, 6.5]}},
    "T3": {"hot": {"Top3": [3.8, 4.0, 7.0, 7.5], "Top5": [3.6, 3.9, 7.0, 7.5], "All8": [3.4, 3.7, 6.5, 7.0]},
          "cold": {"Top3": [3.6, 3.9, 7.0, 7.0], "Top5": [3.4, 3.6, 6.5, 7.0], "All8": [3.2, 3.5, 6.0, 6.5]}}
}

# ======================= 2. STEM  =======================
# - Lower baseline GPA (STEM values technical skills over pure GPA), but higher IELTS for research-focused hot majors
# - AI/CS require 6.5+ IELTS (real HKUST/CityU cutoff), engineering majors 6.0+
STEM_MAJORS = {
    "hot": ["Computer Science", "Data Science", "Artificial Intelligence", "Electronic and Information Engineering", "Information Technology", "Software Engineering"],
    "cold": ["Civil Engineering", "Environmental Science", "Materials Engineering", "Mechanical Engineering", "Maritime Engineering", "Industrial Engineering"]
}
STEM_RULES = {
    "T0": {"hot": {"Top3": [3.1, 3.5, 6.5, 7.0], "Top5": [2.8, 3.2, 6.0, 6.5], "All8": [2.6, 3.0, 6.0, 6.0]}, "cold": {"Top3": [3.0, 3.3, 6.0, 6.5], "Top5": [2.7, 3.0, 6.0, 6.0], "All8": [2.5, 2.8, 6.0, 6.0]}},
    "T1": {"hot": {"Top3": [3.3, 3.7, 6.5, 7.0], "Top5": [3.0, 3.4, 6.0, 6.5], "All8": [2.8, 3.1, 6.0, 6.0]}, "cold": {"Top3": [3.1, 3.4, 6.0, 6.5], "Top5": [2.8, 3.1, 6.0, 6.0], "All8": [2.6, 2.9, 6.0, 6.0]}},
    "T2": {"hot": {"Top3": [3.5, 3.9, 6.5, 7.0], "Top5": [3.2, 3.6, 6.0, 6.5], "All8": [3.0, 3.3, 6.0, 6.5]}, "cold": {"Top3": [3.3, 3.6, 6.0, 6.5], "Top5": [3.0, 3.3, 6.0, 6.0], "All8": [2.8, 3.1, 6.0, 6.0]}},
    "T3": {"hot": {"Top3": [3.7, 4.0, 7.0, 7.5], "Top5": [3.5, 3.8, 6.5, 7.0], "All8": [3.3, 3.6, 6.0, 6.5]}, "cold": {"Top3": [3.5, 3.8, 6.0, 6.5], "Top5": [3.3, 3.5, 6.0, 6.5], "All8": [3.1, 3.4, 6.0, 6.0]}}
}

# ======================= 3. Media =======================
# - Higher IELTS (media requires strong English: 7.0+ for hot majors like International Journalism)
# - GPA: Slightly higher for T3 unis (compensate for school ranking)
MEDIA_MAJORS = {
    "hot": ["Journalism", "Communications", "New Media", "International Journalism", "Media Management", "Digital Media"],
    "cold": ["Film Production", "Creative Media", "Advertising Design", "Cultural and Creative Industries", "Media Education", "Visual Communication"]
}
MEDIA_RULES = {
    "T0": {"hot": {"Top3": [3.3, 3.7, 7.0, 7.5], "Top5": [3.0, 3.4, 6.5, 7.0], "All8": [2.8, 3.1, 6.5, 6.5]}, "cold": {"Top3": [3.1, 3.5, 6.5, 7.0], "Top5": [2.8, 3.2, 6.5, 6.5], "All8": [2.6, 2.9, 6.0, 6.5]}},
    "T1": {"hot": {"Top3": [3.5, 3.8, 7.0, 7.5], "Top5": [3.2, 3.5, 6.5, 7.0], "All8": [3.0, 3.3, 6.5, 6.5]}, "cold": {"Top3": [3.3, 3.6, 6.5, 7.0], "Top5": [3.0, 3.3, 6.5, 6.5], "All8": [2.8, 3.1, 6.0, 6.5]}},
    "T2": {"hot": {"Top3": [3.7, 4.0, 7.0, 7.5], "Top5": [3.4, 3.8, 7.0, 7.5], "All8": [3.2, 3.5, 6.5, 7.0]}, "cold": {"Top3": [3.5, 3.8, 6.5, 7.0], "Top5": [3.2, 3.5, 6.5, 6.5], "All8": [3.0, 3.3, 6.0, 6.5]}},
    "T3": {"hot": {"Top3": [3.8, 4.0, 7.5, 8.0], "Top5": [3.6, 3.9, 7.0, 7.5], "All8": [3.4, 3.7, 6.5, 7.0]}, "cold": {"Top3": [3.6, 3.9, 7.0, 7.5], "Top5": [3.3, 3.6, 6.5, 7.0], "All8": [3.1, 3.4, 6.0, 6.5]}}
}

# ======================= 4. Arts =======================
# - IELTS critical (translation/TEFL require 7.0+ for top programs, 6.5+ minimum)
# - GPA: More lenient for T0/T1 (language proficiency outweighs GPA)
ARTS_MAJORS = {
    "hot": ["Master of Translation and Interpreting", "English Language Education", "Teaching English to Speakers of Other Languages (TESOL)", "International English Education", "Linguistics", "Cross-Cultural Communication"],
    "cold": ["Chinese Language and Literature", "Cultural Studies", "Historical Studies", "Philosophical Studies", "Art History", "Comparative Literature"]
}
ARTS_RULES = {
    "T0": {"hot": {"Top3": [3.2, 3.6, 7.0, 7.5], "Top5": [2.9, 3.3, 6.5, 7.0], "All8": [2.7, 3.0, 6.5, 6.5]}, "cold": {"Top3": [3.0, 3.4, 6.5, 7.0], "Top5": [2.7, 3.1, 6.5, 6.5], "All8": [2.5, 2.8, 6.0, 6.5]}},
    "T1": {"hot": {"Top3": [3.4, 3.7, 7.0, 7.5], "Top5": [3.1, 3.4, 6.5, 7.0], "All8": [2.9, 3.2, 6.5, 6.5]}, "cold": {"Top3": [3.2, 3.5, 6.5, 7.0], "Top5": [2.9, 3.2, 6.5, 6.5], "All8": [2.7, 3.0, 6.0, 6.5]}},
    "T2": {"hot": {"Top3": [3.6, 3.9, 7.0, 7.5], "Top5": [3.3, 3.7, 7.0, 7.5], "All8": [3.1, 3.4, 6.5, 7.0]}, "cold": {"Top3": [3.4, 3.7, 6.5, 7.0], "Top5": [3.1, 3.4, 6.5, 6.5], "All8": [2.9, 3.2, 6.0, 6.5]}},
    "T3": {"hot": {"Top3": [3.7, 4.0, 7.5, 8.0], "Top5": [3.5, 3.8, 7.0, 7.5], "All8": [3.3, 3.6, 6.5, 7.0]}, "cold": {"Top3": [3.5, 3.8, 6.5, 7.0], "Top5": [3.2, 3.5, 6.5, 6.5], "All8": [3.0, 3.3, 6.0, 6.5]}}
}

# ======================= 5. Social Science =======================
# - IELTS: 7.0+ for hot majors (IR/Public Policy at HKU/CUHK requires 7.0), 6.0+ for cold
# - GPA: T3 unis need 3.4+ for All8 (compensate for school ranking)
SOCIAL_MAJORS = {
    "hot": ["Public Policy", "Social Management", "International Relations", "Urban Management", "Public Administration", "Development Studies"],
    "cold": ["Social Work", "Sociology", "Anthropology", "Social Policy", "Gerontology", "Community Services"]
}
SOCIAL_RULES = {
    "T0": {"hot": {"Top3": [3.3, 3.7, 7.0, 7.5], "Top5": [3.0, 3.4, 6.5, 7.0], "All8": [2.8, 3.1, 6.5, 6.5]}, "cold": {"Top3": [3.1, 3.5, 6.5, 7.0], "Top5": [2.8, 3.2, 6.5, 6.5], "All8": [2.6, 2.9, 6.0, 6.5]}},
    "T1": {"hot": {"Top3": [3.5, 3.8, 7.0, 7.5], "Top5": [3.2, 3.5, 6.5, 7.0], "All8": [3.0, 3.3, 6.5, 6.5]}, "cold": {"Top3": [3.3, 3.6, 6.5, 7.0], "Top5": [3.0, 3.3, 6.5, 6.5], "All8": [2.8, 3.1, 6.0, 6.5]}},
    "T2": {"hot": {"Top3": [3.7, 4.0, 7.0, 7.5], "Top5": [3.4, 3.8, 7.0, 7.5], "All8": [3.2, 3.5, 6.5, 7.0]}, "cold": {"Top3": [3.5, 3.8, 6.5, 7.0], "Top5": [3.2, 3.5, 6.5, 6.5], "All8": [3.0, 3.3, 6.0, 6.5]}},
    "T3": {"hot": {"Top3": [3.8, 4.0, 7.5, 8.0], "Top5": [3.6, 3.9, 7.0, 7.5], "All8": [3.4, 3.7, 6.5, 7.0]}, "cold": {"Top3": [3.6, 3.9, 7.0, 7.5], "Top5": [3.3, 3.6, 6.5, 7.0], "All8": [3.1, 3.4, 6.0, 6.5]}}
}

# ======================= Core Configuration =======================
HK_GROUPS = {"Top3": "HKU / CUHK / HKUST", "Top5": "Top3 + CityU / PolyU", "All8": "All 8 HKU Grants Committee Universities"}
MAJOR_CONFIG = {
    "business": {"special": BUSINESS_SPECIAL, "majors": BUSINESS_MAJORS, "rules": BUSINESS_RULES},
    "stem": {"special": STEM_SPECIAL, "majors": STEM_MAJORS, "rules": STEM_RULES},
    "media": {"special": MEDIA_SPECIAL, "majors": MEDIA_MAJORS, "rules": MEDIA_RULES},
    "arts": {"special": ARTS_SPECIAL, "majors": ARTS_MAJORS, "rules": ARTS_RULES},
    "social": {"special": SOCIAL_SPECIAL, "majors": SOCIAL_MAJORS, "rules": SOCIAL_RULES}
}

# ======================= Valid University Set =======================
ALL_UNIVERSITIES = set()
for _schools in UNIVERSITY_TIERS.values():
    ALL_UNIVERSITIES.update(_schools)
for _cfg in MAJOR_CONFIG.values():
    ALL_UNIVERSITIES.update(_cfg["special"])

# ======================= Core Function: Auto Tiering =======================
def get_tier(uni_name, major_type):
    for t, schools in UNIVERSITY_TIERS.items():
        if uni_name in schools:
            return t
    if uni_name in MAJOR_CONFIG[major_type]["special"]:
        return "T2"
    return "T3"

# ======================= Core Function: Granular Evaluation =======================
def evaluate(gpa, ielts, req):
    base_gpa, comp_gpa, base_ielts, comp_ielts = req

    # Fully below minimum requirements
    if gpa < base_gpa or ielts < base_ielts:
        return "❌ Not Eligible", f"Minimum Requirements: GPA≥{base_gpa}, IELTS≥{base_ielts}"

    # Strong competitiveness (meet top-tier standards)
    if gpa >= comp_gpa and ielts >= comp_ielts:
        return "✅ Strong Competitiveness", f"Competitive: GPA≥{comp_gpa}, IELTS≥{comp_ielts}"

    # Marginal risk (meet minimum but not competitive)
    return "⚠️ At Risk", f"Recommended Improvement: GPA≥{comp_gpa}, IELTS≥{comp_ielts}"

# ======================= Core Function: Priority Recommendation for Hot Majors =======================
def recommend(uni_name, gpa, ielts, major_type):
    # Auto-determine university tier
    tier = get_tier(uni_name, major_type)
    cfg = MAJOR_CONFIG[major_type]
    hot_majors = cfg["majors"]["hot"]
    cold_majors = cfg["majors"]["cold"]
    rules = cfg["rules"][tier]

    output = {
        "Undergraduate University": uni_name,
        "Auto-Assigned Tier": tier,
        "Major Category": major_type,
        "GPA (4.0 Scale)": gpa,
        "IELTS Score": ielts,
        "Recommendation List": []
    }

    for gk, group_name in HK_GROUPS.items():
        hot_status, hot_desc = evaluate(gpa, ielts, rules["hot"][gk])
        cold_status, cold_desc = evaluate(gpa, ielts, rules["cold"][gk])
        # Only include if both hot/cold majors meet minimum requirements (avoid misleading recommendations)
        hot_eligible = "❌" not in hot_status
        cold_eligible = "❌" not in cold_status
        if hot_eligible and cold_eligible:
            output["Recommendation List"].append({
                "HK University Group": group_name,
                "Hot Majors": {
                    "Majors": hot_majors,
                    "Status": hot_status,
                    "Details": hot_desc
                },
                "Safety Majors (Cold)": {
                    "Majors": cold_majors,
                    "Status": cold_status,
                    "Details": cold_desc
                }
            })

    return output
