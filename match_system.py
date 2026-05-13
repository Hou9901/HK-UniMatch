# ==========================================================
# Hong Kong Master Match System
# All Majors Optimized: Business / STEM / Media / Arts / Social
# Real HK University Admission Standards + Priority Recommendation
# ==========================================================

from typing import Optional
import os

# ======================= CHINA MAINLAND UNIVERSITY TIERS =======================
# Definition of university tiers for mainland China universities
# Classified by comprehensive strength and admission difficulty
UNIVERSITY_TIERS = {
    # C9 + top sino-foreign cooperative universities
    "T0": [
        "北京大学", "清华大学", "复旦大学", "上海交通大学",
        "浙江大学", "中国科学技术大学", "南京大学", "中国人民大学",
        "香港中文大学（深圳）", "香港科技大学（广州）",
        "上海纽约大学", "昆山杜克大学"
    ],
    # top 985 + leading 211 universities / schools with strong specialties
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
    # mainstream 211 + strong non-985 or non-211 universities / high-quality sino-foreign cooperative universities
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
        "贵州大学", "云南大学", "广西大学", "海南大学",
        "深圳大学", "浙江工业大学", "江苏大学", "南京工业大学",
        "福建师范大学", "广东工业大学", "杭州电子科技大学",
        "南京信息工程大学", "南京邮电大学", "南京林业大学",
        "宁波大学", "浙江师范大学", "首都师范大学", "扬州大学",
        "北师香港浸会大学", "西交利物浦大学", "宁波诺丁汉大学",
    ],
    # policy 211 + top 200 universities ranked by SoftRanking
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

# ======================= SPECIAL SCHOOLS =======================
# Specialised institutions with strong disciplinary advantages (classified by major type)
# These schools are not in the standard tier list but have equivalent strength to T2 universities
BUSINESS_SPECIAL = ["东北财经大学", "江西财经大学", "浙江工商大学", "南京财经大学", "南京审计大学", "山东财经大学",
                    "天津财经大学", "首都经济贸易大学", "上海对外经贸大学"]
STEM_SPECIAL = ["杭州电子科技大学", "南京邮电大学", "重庆邮电大学", "浙江工业大学", "广东工业大学", "江苏大学",
                "深圳大学", "天津工业大学", "成都理工大学", "上海理工大学", "南京工业大学", "西安邮电大学"]
MEDIA_SPECIAL = ["浙江传媒学院", "四川传媒学院", "南京传媒学院", "武汉传媒学院", "北京电影学院", "上海视觉艺术学院"]
ARTS_SPECIAL = ["四川外国语大学", "西安外国语大学", "广东外语外贸大学", "天津外国语大学", "外交学院", "北京语言大学",
                "首都师范大学", "山东师范大学", "福建师范大学"]
SOCIAL_SPECIAL = ["西北政法大学", "西南政法大学", "华东政法大学", "上海政法学院", "山东政法学院", "中国青年政治学院",
                  "中国社会科学院大学"]

# Classification of Popular/Unpopular Majors + Admission Criteria (GPA/IELTS Thresholds)
# Rule Explanation: [Basic GPA, Competitive GPA, Basic IELTS, Competitive IELTS]
# ======================= 1. Business =======================
BUSINESS_MAJORS = {
    "hot": ["金融硕士", "会计硕士", "商业分析", "金融科技", "市场营销", "国际商务"],
    "cold": ["供应链管理", "人力资源管理", "运营管理", "旅游与酒店管理", "公共财务", "创业管理"]
}
BUSINESS_RULES = {
    "T0": {"hot": {"Top3": [3.2, 3.5, 6.5, 7.0], "Top5": [3.0, 3.3, 6.5, 6.5], "All8": [2.8, 3.1, 6.0, 6.5]},
           "cold": {"Top3": [3.0, 3.3, 6.5, 6.5], "Top5": [2.8, 3.1, 6.0, 6.5], "All8": [2.6, 2.9, 6.0, 6.0]}},
    "T1": {"hot": {"Top3": [3.3, 3.6, 6.5, 7.0], "Top5": [3.1, 3.4, 6.5, 7.0], "All8": [2.9, 3.2, 6.0, 6.5]},
           "cold": {"Top3": [3.1, 3.4, 6.5, 6.5], "Top5": [2.9, 3.2, 6.0, 6.5], "All8": [2.7, 3.0, 6.0, 6.0]}},
    "T2": {"hot": {"Top3": [3.4, 3.7, 6.5, 7.0], "Top5": [3.2, 3.5, 6.5, 7.0], "All8": [3.0, 3.3, 6.0, 6.5]},
           "cold": {"Top3": [3.2, 3.5, 6.5, 6.5], "Top5": [3.0, 3.3, 6.0, 6.5], "All8": [2.8, 3.1, 6.0, 6.0]}},
    "T3": {"hot": {"Top3": [3.5, 3.8, 6.5, 7.0], "Top5": [3.3, 3.6, 6.5, 7.0], "All8": [3.1, 3.4, 6.0, 6.5]},
           "cold": {"Top3": [3.3, 3.6, 6.5, 6.5], "Top5": [3.1, 3.4, 6.0, 6.5], "All8": [2.9, 3.2, 6.0, 6.0]}}
}

# ======================= 2. STEM =======================
STEM_MAJORS = {
    "hot": ["计算机科学", "数据科学", "人工智能", "电子信息工程", "信息技术", "软件工程"],
    "cold": ["土木工程", "环境科学", "材料工程", "机械工程", "海事工程", "工业工程"]
}
STEM_RULES = {
    "T0": {"hot": {"Top3": [2.9, 3.2, 6.0, 6.5], "Top5": [2.7, 3.0, 6.0, 6.0], "All8": [2.5, 2.8, 6.0, 6.0]},
           "cold": {"Top3": [2.8, 3.1, 6.0, 6.0], "Top5": [2.6, 2.9, 6.0, 6.0], "All8": [2.4, 2.7, 6.0, 6.0]}},
    "T1": {"hot": {"Top3": [3.0, 3.3, 6.0, 6.5], "Top5": [2.8, 3.1, 6.0, 6.0], "All8": [2.6, 2.9, 6.0, 6.0]},
           "cold": {"Top3": [2.9, 3.2, 6.0, 6.0], "Top5": [2.7, 3.0, 6.0, 6.0], "All8": [2.5, 2.8, 6.0, 6.0]}},
    "T2": {"hot": {"Top3": [3.2, 3.5, 6.0, 6.5], "Top5": [3.0, 3.3, 6.0, 6.0], "All8": [2.8, 3.1, 6.0, 6.0]},
           "cold": {"Top3": [3.0, 3.3, 6.0, 6.0], "Top5": [2.8, 3.1, 6.0, 6.0], "All8": [2.6, 2.9, 6.0, 6.0]}},
    "T3": {"hot": {"Top3": [3.3, 3.6, 6.0, 6.5], "Top5": [3.1, 3.4, 6.0, 6.0], "All8": [2.9, 3.2, 6.0, 6.0]},
           "cold": {"Top3": [3.1, 3.4, 6.0, 6.0], "Top5": [2.9, 3.2, 6.0, 6.0], "All8": [2.7, 3.0, 6.0, 6.0]}}
}

# ======================= 3. Media =======================
MEDIA_MAJORS = {
    "hot": ["新闻学", "传播学", "新媒体", "国际新闻", "媒体管理", "数字媒体"],
    "cold": ["影视制作", "创意媒体", "广告设计", "文化创意产业", "媒体教育", "视觉传播"]
}
MEDIA_RULES = {
    "T0": {"hot": {"Top3": [3.1, 3.4, 6.5, 7.0], "Top5": [2.9, 3.2, 6.5, 6.5], "All8": [2.7, 3.0, 6.5, 6.5]},
           "cold": {"Top3": [3.0, 3.3, 6.5, 6.5], "Top5": [2.8, 3.1, 6.5, 6.5], "All8": [2.6, 2.9, 6.0, 6.0]}},
    "T1": {"hot": {"Top3": [3.2, 3.5, 6.5, 7.0], "Top5": [3.0, 3.3, 6.5, 7.0], "All8": [2.8, 3.1, 6.5, 6.5]},
           "cold": {"Top3": [3.1, 3.4, 6.5, 6.5], "Top5": [2.9, 3.2, 6.5, 6.5], "All8": [2.7, 3.0, 6.0, 6.0]}},
    "T2": {"hot": {"Top3": [3.3, 3.6, 6.5, 7.0], "Top5": [3.1, 3.4, 6.5, 7.0], "All8": [2.9, 3.2, 6.5, 6.5]},
           "cold": {"Top3": [3.2, 3.5, 6.5, 6.5], "Top5": [3.0, 3.3, 6.5, 6.5], "All8": [2.8, 3.1, 6.0, 6.0]}},
    "T3": {"hot": {"Top3": [3.4, 3.7, 6.5, 7.0], "Top5": [3.2, 3.5, 6.5, 7.0], "All8": [3.0, 3.3, 6.5, 6.5]},
           "cold": {"Top3": [3.3, 3.6, 6.5, 6.5], "Top5": [3.1, 3.4, 6.5, 6.5], "All8": [2.9, 3.2, 6.0, 6.0]}}
}

# ======================= 4. Arts =======================
ARTS_MAJORS = {
    "hot": ["翻译硕士", "英语教育", "对外英语教学", "国际英语教育", "语言研究", "跨文化交流"],
    "cold": ["中国语言文学", "文化研究", "历史研究", "哲学研究", "艺术史", "比较文学"]
}
ARTS_RULES = {
    "T0": {"hot": {"Top3": [3.1, 3.4, 6.5, 7.0], "Top5": [2.9, 3.2, 6.5, 7.0], "All8": [2.7, 3.0, 6.5, 6.5]},
           "cold": {"Top3": [3.0, 3.3, 6.5, 6.5], "Top5": [2.8, 3.1, 6.5, 6.5], "All8": [2.6, 2.9, 6.0, 6.0]}},
    "T1": {"hot": {"Top3": [3.2, 3.5, 6.5, 7.0], "Top5": [3.0, 3.3, 6.5, 7.0], "All8": [2.8, 3.1, 6.5, 6.5]},
           "cold": {"Top3": [3.1, 3.4, 6.5, 6.5], "Top5": [2.9, 3.2, 6.5, 6.5], "All8": [2.7, 3.0, 6.0, 6.0]}},
    "T2": {"hot": {"Top3": [3.3, 3.6, 6.5, 7.0], "Top5": [3.1, 3.4, 6.5, 7.0], "All8": [2.9, 3.2, 6.5, 6.5]},
           "cold": {"Top3": [3.2, 3.5, 6.5, 6.5], "Top5": [3.0, 3.3, 6.5, 6.5], "All8": [2.8, 3.1, 6.0, 6.0]}},
    "T3": {"hot": {"Top3": [3.4, 3.7, 6.5, 7.0], "Top5": [3.2, 3.5, 6.5, 7.0], "All8": [3.0, 3.3, 6.5, 6.5]},
           "cold": {"Top3": [3.3, 3.6, 6.5, 6.5], "Top5": [3.1, 3.4, 6.5, 6.5], "All8": [2.9, 3.2, 6.0, 6.0]}}
}

# ======================= 5. Social Science =======================
SOCIAL_MAJORS = {
    "hot": ["公共政策", "社会管理", "国际关系", "城市管理", "公共行政", "发展研究"],
    "cold": ["社会工作", "社会学", "人类学", "社会政策", "老年学", "社区服务"]
}
SOCIAL_RULES = {
    "T0": {"hot": {"Top3": [3.1, 3.4, 6.5, 7.0], "Top5": [2.9, 3.2, 6.5, 6.5], "All8": [2.7, 3.0, 6.5, 6.5]},
           "cold": {"Top3": [3.0, 3.3, 6.5, 6.5], "Top5": [2.8, 3.1, 6.5, 6.5], "All8": [2.6, 2.9, 6.0, 6.0]}},
    "T1": {"hot": {"Top3": [3.2, 3.5, 6.5, 7.0], "Top5": [3.0, 3.3, 6.5, 7.0], "All8": [2.8, 3.1, 6.5, 6.5]},
           "cold": {"Top3": [3.1, 3.4, 6.5, 6.5], "Top5": [2.9, 3.2, 6.5, 6.5], "All8": [2.7, 3.0, 6.0, 6.0]}},
    "T2": {"hot": {"Top3": [3.3, 3.6, 6.5, 7.0], "Top5": [3.1, 3.4, 6.5, 7.0], "All8": [2.9, 3.2, 6.5, 6.5]},
           "cold": {"Top3": [3.2, 3.5, 6.5, 6.5], "Top5": [3.0, 3.3, 6.5, 6.5], "All8": [2.8, 3.1, 6.0, 6.0]}},
    "T3": {"hot": {"Top3": [3.4, 3.7, 6.5, 7.0], "Top5": [3.2, 3.5, 6.5, 7.0], "All8": [3.0, 3.3, 6.5, 6.5]},
           "cold": {"Top3": [3.3, 3.6, 6.5, 6.5], "Top5": [3.1, 3.4, 6.5, 6.5], "All8": [2.9, 3.2, 6.0, 6.0]}}
}

# ======================= Core Configuration =======================
# - Top3: HKU / CUHK / HKUST (Top 3 universities in Hong Kong)
# - Top5: Top3 + CityU / PolyU (Top 5 + CityU and PolyU)
# - All8: All 8 major universities in Hong Kong
# Aggregates specialised institutions, major lists, and admission rules by major type
HK_GROUPS = {"Top3": "港大/港中文/港科大", "Top5": "Top5+城大理工", "All8": "全港八大"}
MAJOR_CONFIG = {
    "business": {"special": BUSINESS_SPECIAL, "majors": BUSINESS_MAJORS, "rules": BUSINESS_RULES},
    "stem": {"special": STEM_SPECIAL, "majors": STEM_MAJORS, "rules": STEM_RULES},
    "media": {"special": MEDIA_SPECIAL, "majors": MEDIA_MAJORS, "rules": MEDIA_RULES},
    "arts": {"special": ARTS_SPECIAL, "majors": ARTS_MAJORS, "rules": ARTS_RULES},
    "social": {"special": SOCIAL_SPECIAL, "majors": SOCIAL_MAJORS, "rules": SOCIAL_RULES}
}

# ======================= Valid University Set =======================
# Combined set of all valid universities (standard tiers + specialised institutions)
# Used for input validation and tier determination
ALL_UNIVERSITIES = set()
for _schools in UNIVERSITY_TIERS.values():
    ALL_UNIVERSITIES.update(_schools)
for _cfg in MAJOR_CONFIG.values():
    ALL_UNIVERSITIES.update(_cfg["special"])


# ======================= Core Functions - Automatic Tier Determination =======================
def get_tier(uni_name, major_type):
    """
    Determine the tier of a mainland China university for admission evaluation.
    1. Check standard tiers (T0-T3) first
    2. If university is in major-specific special list → assign T2
    3. Default to T3 if not found

    Args:
        uni_name (str): Name of the mainland university
        major_type (str): Major category (business/stem/media/arts/social)

    Returns:
        str: Tier (T0/T1/T2/T3)
    """
    for t, schools in UNIVERSITY_TIERS.items():
        if uni_name in schools:
            return t
    if uni_name in MAJOR_CONFIG[major_type]["special"]:
        return "T2"
    return "T3"


# ======================= Granular Evaluation =======================
def evaluate(gpa, ielts, req):
    """
    Evaluate applicant's GPA/IELTS against admission requirements.
    Requirement format: [base GPA, competitive GPA, base IELTS, competitive IELTS]

    Evaluation Outcomes:
    1. ❌ Not Eligible: GPA < base GPA OR IELTS < base IELTS
    2. ✅ Strong Competitiveness: GPA ≥ competitive GPA AND IELTS ≥ competitive IELTS
    3. ⚠️ At Risk: Meets base requirements but not competitive thresholds

    Args:
        gpa (float): Applicant's GPA
        ielts (float): Applicant's IELTS score
        req (list): Admission thresholds [base_gpa, comp_gpa, base_ielts, comp_ielts]

    Returns:
        tuple: (status_str, description_str)
    """
    base_gpa, comp_gpa, base_ielts, comp_ielts = req

    # Not meeting minimum requirements
    if gpa < base_gpa or ielts < base_ielts:
        return "❌ 未达标", f"最低要求：GPA≥{base_gpa} 雅思≥{base_ielts}"

    # Strong competitiveness (meets competitive thresholds)
    if gpa >= comp_gpa and ielts >= comp_ielts:
        return "✅ 强竞争力", f"达标：GPA≥{comp_gpa} 雅思≥{comp_ielts}"

    # At risk (meets base but not competitive)
    return "⚠️ 有风险", f"建议提升：GPA≥{comp_gpa} 雅思≥{comp_ielts}"


# ======================= Core Optimisation: Priority Recommendation for Hot Majors =======================
def recommend(uni_name, gpa, ielts, major_type):
    """
    Generate HK master's program recommendations based on applicant profile.
    Prioritizes hot majors and filters eligible HK university groups (only include if both hot/cold meet base requirements).

    Args:
        uni_name (str): Mainland university name
        gpa (float): Applicant's GPA
        ielts (float): Applicant's IELTS score
        major_type (str): Major category (business/stem/media/arts/social)

    Returns:
        dict: Recommendation results with applicant info and eligible HK university groups
    """

    # Auto-determine university tier
    tier = get_tier(uni_name, major_type)
    cfg = MAJOR_CONFIG[major_type]
    hot_majors = cfg["majors"]["hot"]
    cold_majors = cfg["majors"]["cold"]
    rules = cfg["rules"][tier]

    output = {
        "本科院校": uni_name,
        "自动判定等级": tier,
        "专业方向": major_type,
        "GPA": gpa,
        "雅思": ielts,
        "推荐列表": []
    }

    for gk, group_name in HK_GROUPS.items():
        hot_status, hot_desc = evaluate(gpa, ielts, rules["hot"][gk])
        cold_status, cold_desc = evaluate(gpa, ielts, rules["cold"][gk])
        # Require both tracks to meet at least the minimum GPA/IELTS bar for this tier.
        # If we only required cold ("保底"), a tier could appear while hot majors were still
        # "❌ 未达标", which reads like the whole tier (including 热门) is reachable.
        hot_ok = "❌" not in hot_status
        cold_ok = "❌" not in cold_status
        if hot_ok and cold_ok:
            output["推荐列表"].append({
                "港校梯队": group_name,
                "热门专业": {
                    "专业": hot_majors,
                    "状态": hot_status,
                    "说明": hot_desc
                },
                "冷门保底": {
                    "专业": cold_majors,
                    "状态": cold_status,
                    "说明": cold_desc
                }
            })

    return output


# ======================= Conversion (IELTS TO TOEFL) =======================
def toefl_to_ielts_equivalent(toefl_total: float) -> float:
    """
    Convert TOEFL iBT total score (0–120) to approximate IELTS band score.
    Used for unified English proficiency evaluation.

    Args:
        toefl_total (float): TOEFL iBT total score

    Returns:
        float: Equivalent IELTS band (4.0–9.0)
    """
    t = float(toefl_total)
    if t >= 118:
        return 9.0
    if t >= 115:
        return 8.5
    if t >= 110:
        return 8.0
    if t >= 102:
        return 7.5
    if t >= 94:
        return 7.0
    if t >= 79:
        return 6.5
    if t >= 60:
        return 6.0
    if t >= 46:
        return 5.5
    if t >= 35:
        return 5.0
    if t >= 32:
        return 4.5
    return 4.0


def score_to_ielts_for_filter(exam_type: str, score: float) -> float:
    """
    Convert English exam score to IELTS equivalent for filtering.
    Supports TOEFL (convert to IELTS) or raw IELTS score.

    Args:
        exam_type (str): "TOEFL" or "IELTS"
        score (float): Exam score (TOEFL total or IELTS band)

    Returns:
        float: IELTS equivalent score

    Raises:
        ValueError: If exam_type is not "TOEFL" or "IELTS"
    """
    et = exam_type.strip().upper()
    if et == "TOEFL":
        return toefl_to_ielts_equivalent(score)
    if et == "IELTS":
        return float(score)
    raise ValueError(f"Unsupported exam_type: {exam_type!r}")


def row_english_requirement_as_ielts_band(row: dict) -> Optional[float]:
    """
    Extract English requirement from CSV row and convert to IELTS equivalent.
    Priority: 1. Raw IELTS score → 2. TOEFL score (converted) → 3. None (if neither is valid)

    Args:
        row (dict): CSV row with "IELTS" and/or "TOEFL" columns

    Returns:
        Optional[float]: IELTS equivalent band, or None if no valid score
    """
    raw_ielts = row.get("IELTS", "")
    cell_i = "" if raw_ielts is None else str(raw_ielts).strip()
    if cell_i:
        try:
            return float(cell_i)
        except (ValueError, TypeError):
            pass

    raw_toefl = row.get("TOEFL", "")
    cell_t = "" if raw_toefl is None else str(raw_toefl).strip()
    if cell_t:
        try:
            return toefl_to_ielts_equivalent(float(cell_t))
        except (ValueError, TypeError):
            pass

    return None


# HK University Short Name → Full English Name Mapping
UNI_SHORT_TO_FULL = {
    "HKU": "The University of Hong Kong",
    "CUHK": "The Chinese University of Hong Kong",
    "HKUST": "The Hong Kong University of Science and Technology",
    "PolyU": "The Hong Kong Polytechnic University",
    "CityU": "City University of Hong Kong",
    "HKBU": "Hong Kong Baptist University",
    "LingnanU": "Lingnan University",
    "EdUHK": "The Education University of Hong Kong"
}

ALL_SHORTS = list(UNI_SHORT_TO_FULL.keys())

# Map HK University Group Display Name to Short Codes
TIER_DISPLAY_TO_SHORTS = {
    "港大/港中文/港科大": ["HKU", "CUHK", "HKUST"],
    "Top5+城大理工": ["CityU", "PolyU"],
    "全港八大": ["HKBU", "LingnanU", "EdUHK"]
}

# Map Major Type to CSV Category Name
MAJOR_TYPE_TO_CATEGORY = {
    "business": "Business",
    "stem": "Engineering&Technology",
    "social": "Social Sciences",
    "arts": "Humanities",
    "media": "Humanities"
}

# Valid major types (restrict input to these values)
ALLOWED_MAJOR_TYPES = frozenset(MAJOR_CONFIG.keys())

# Programme category display order (matches UI labels); unknown / missing sort last ("Other").
PROGRAMME_CATEGORY_ORDER = (
    "Business",
    "Engineering&Technology",
    "Social Sciences",
    "Humanities",
    "Art",
    "Medicine&Health",
    "Education",
)


def _category_sort_rank(category: Optional[str]) -> int:
    """
    Assign sort rank to programme category (for display ordering).
    Unknown/missing categories get the highest rank (sorted last).

    Args:
        category (Optional[str]): Programme category from CSV

    Returns:
        int: Sort rank (lower = earlier in display)
    """
    if category is None or not str(category).strip():
        return len(PROGRAMME_CATEGORY_ORDER)
    key = str(category).strip()
    try:
        return PROGRAMME_CATEGORY_ORDER.index(key)
    except ValueError:
        return len(PROGRAMME_CATEGORY_ORDER)


def sort_programmes_for_display(programmes: list[dict]) -> list[dict]:
    """
    Sort programmes for user-friendly display:
    1. Keep university order as first seen (no reordering of universities)
    2. Within each university:
       a. Category (per PROGRAMME_CATEGORY_ORDER)
       b. University name (case-insensitive)
       c. Programme name (case-insensitive)

    Args:
        programmes (list[dict]): List of programme dicts from CSV

    Returns:
        list[dict]: Sorted programme list
    """
    if not programmes:
        return programmes
    uni_seq: list[str] = []
    seen: set[str] = set()
    for p in programmes:
        u = p.get("University") or ""
        if u not in seen:
            seen.add(u)
            uni_seq.append(u)
    rank_of = {u: i for i, u in enumerate(uni_seq)}
    fallback = len(uni_seq)

    def sort_key(p: dict) -> tuple[int, int, str, str]:
        u = p.get("University") or ""
        prog = p.get("Programme") or ""
        return (
            rank_of.get(u, fallback),
            _category_sort_rank(p.get("Category")),
            str(u).casefold(),
            str(prog).casefold(),
        )

    return sorted(programmes, key=sort_key)


def enrich_recommendations_with_programmes(result: dict, ielts: float, major_type: str, csv_path: str, logger) -> dict:
    """
    Enrich recommendation results with detailed programme info from CSV.
    Filters programmes by:
    1. Major category (matches major_type)
    2. HK university group (matches recommendation list)
    3. English requirement (IELTS ≤ applicant's score)

    Args:
        result (dict): Base recommendation result from `recommend()`
        ielts (float): Applicant's IELTS score (or TOEFL-converted)
        major_type (str): Major category (business/stem/media/arts/social)
        csv_path (str): Path to CSV file with HK programme details
        logger: Logger instance for warning messages

    Returns:
        dict: Enriched result with "programmes" key in each recommendation item
    """
    category = MAJOR_TYPE_TO_CATEGORY.get(major_type, "Business")
    csv_rows = []
    try:
        with open(csv_path, encoding="latin1") as f:
            import csv
            reader = csv.DictReader(f)
            for row in reader:
                if row["Category"] == category:
                    csv_rows.append(row)
    except FileNotFoundError:
        pass

    for item in result["推荐列表"]:
        shorts = TIER_DISPLAY_TO_SHORTS.get(item["港校梯队"])
        if shorts:
            full_names = {UNI_SHORT_TO_FULL[s] for s in shorts if s in UNI_SHORT_TO_FULL}
            hot_status = item["热门专业"]["状态"]
            if "✅" in hot_status:
                match_level = "✅ 有竞争力"
            elif "⚠️" in hot_status:
                match_level = "⚠️ 有风险"
            else:
                match_level = hot_status
            programmes = []
            for r in csv_rows:
                if r["University"] not in full_names:
                    continue
                req_band = row_english_requirement_as_ielts_band(r)
                if req_band is None:
                    logger.warning(
                        "Skipping programme row: empty or non-numeric IELTS and TOEFL "
                        "(programme=%r, university=%r, raw_ielts=%r, raw_toefl=%r)",
                        r.get("Programme"),
                        r.get("University"),
                        r.get("IELTS"),
                        r.get("TOEFL"),
                    )
                    continue
                if req_band <= ielts:
                    programmes.append({
                        "Programme": r["Programme"],
                        "University": r["University"],
                        "Category": r["Category"],
                        "IELTS": r["IELTS"],
                        "Duration": r["Duration"],
                        "Apply date": r["Apply date"],
                        "match_level": match_level
                    })
            item["programmes"] = sort_programmes_for_display(programmes)
        else:
            item["programmes"] = []

    return result


def get_programmes_from_csv(csv_path: str, uni_short: Optional[str] = None) -> list[dict]:
    """
    Retrieve HK programme details from CSV, optionally filtered by university short name.

    Args:
        csv_path (str): Path to CSV file with HK programme details
        uni_short (Optional[str]): HK university short code (HKU/CUHK/etc.) → filter results

    Returns:
        list[dict]: Sorted list of programme dicts (or empty list if file not found)
    """
    full_name = UNI_SHORT_TO_FULL.get(uni_short) if uni_short else None
    results = []
    try:
        with open(csv_path, encoding="latin1") as f:
            import csv
            reader = csv.DictReader(f)
            for row in reader:
                if full_name is None or row["University"] == full_name:
                    results.append({
                        "University": row["University"],
                        "Programme": row["Programme"],
                        "Category": row["Category"],
                        "IELTS": row["IELTS"],
                        "TOEFL": row.get("TOEFL", ""),
                        "Duration": row["Duration"],
                        "Apply date": row["Apply date"]
                    })
    except FileNotFoundError:
        pass
    return sort_programmes_for_display(results)


# ======================= Testing =======================
if __name__ == "__main__":
    # 测试：深圳大学 + GPA3.3 + IELTS 6.5 + Business
    result = recommend("深圳大学", 3.3, 6.5, "business")

    print("===== 香港硕士匹配结果 =====")
    for k, v in result.items():
        if k != "推荐列表":
            print(f"{k}: {v}")

    print("\n===== 智能推荐（热门优先）=====")
    for i, item in enumerate(result["推荐列表"], 1):
        hot = item['热门专业']
        cold = item['冷门保底']
        print(f"\n{i}. {item['港校梯队']}")
        print(f"   🔥 热门专业: {hot['状态']} | {', '.join(hot['专业'])}")
        print(f"      {hot['说明']}")
        print(f"   ❄️ 冷门保底: {cold['状态']} | {', '.join(cold['专业'])}")
        print(f"      {cold['说明']}")