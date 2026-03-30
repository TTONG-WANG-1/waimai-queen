#!/usr/bin/env python3
"""
外卖女王 - 小红书数据采集脚本
采集深圳地区外卖推荐笔记
"""
import json
import re
from datetime import datetime
from pathlib import Path

# 配置
DATA_DIR = Path(__file__).parent.parent / 'data'
SHOPS_FILE = DATA_DIR / 'shops.json'

# 深圳区域关键词
SHENZHEN_AREAS = {
    '南山区': ['南山', '科技园', '海岸城', '深圳湾', '前海', '西丽', '蛇口'],
    '福田区': ['福田', 'CBD', '车公庙', '华强北', '香蜜湖'],
    '罗湖区': ['罗湖', '国贸', '东门', '万象城'],
    '宝安区': ['宝安', '西乡', '福永', '沙井'],
    '龙华区': ['龙华', '深圳北', '民治'],
    '龙岗区': ['龙岗', '大运', '布吉', '坂田']
}

def detect_area(text):
    """从文本中检测区域"""
    text = text.lower()
    for area, keywords in SHENZHEN_AREAS.items():
        for keyword in keywords:
            if keyword in text:
                return area, keyword
    return '深圳市', '深圳'

def parse_xiaohongshu_note(note_data):
    """解析小红书笔记数据"""
    title = note_data.get('title', '')
    desc = note_data.get('desc', '')
    area, sub_area = detect_area(title + ' ' + desc)
    
    # 提取店铺名（简单规则，后续优化）
    shop_name = note_data.get('shop_name', '未知店铺')
    
    # 提取推荐菜
    recommendations = []
    if 'recommendations' in note_data:
        recommendations = note_data['recommendations']
    
    shop = {
        'id': note_data.get('id', datetime.now().timestamp()),
        'name': shop_name,
        'area': area,
        'subArea': sub_area,
        'rating': note_data.get('rating', ''),
        'price': note_data.get('price', ''),
        'recommendations': recommendations,
        'source': '小红书',
        'link': note_data.get('link', ''),
        'image': note_data.get('image', ''),
        'collectedAt': datetime.now().isoformat()
    }
    
    return shop

def load_existing_shops():
    """加载已有店铺数据"""
    if SHOPS_FILE.exists():
        with open(SHOPS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'lastUpdate': datetime.now().isoformat(), 'shops': []}

def save_shops(data):
    """保存店铺数据"""
    DATA_DIR.mkdir(exist_ok=True)
    with open(SHOPS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_sample_shops():
    """添加示例店铺数据（用于测试）"""
    sample_shops = [
        {
            'id': '1',
            'name': '木屋烧烤',
            'area': '南山区',
            'subArea': '科技园',
            'rating': '4.8',
            'price': '人均 60 元',
            'recommendations': ['烤羊肉串', '烤茄子', '蒜蓉生蚝'],
            'source': '小红书',
            'link': 'https://www.xiaohongshu.com/...',
            'image': '',
            'collectedAt': datetime.now().isoformat()
        },
        {
            'id': '2',
            'name': '点都德',
            'area': '福田区',
            'subArea': 'CBD',
            'rating': '4.6',
            'price': '人均 80 元',
            'recommendations': ['虾饺', '红米肠', '流沙包'],
            'source': '小红书',
            'link': 'https://www.xiaohongshu.com/...',
            'image': '',
            'collectedAt': datetime.now().isoformat()
        },
        {
            'id': '3',
            'name': '探鱼',
            'area': '南山区',
            'subArea': '海岸城',
            'rating': '4.5',
            'price': '人均 70 元',
            'recommendations': ['清江鱼', '烤牛蛙', '红糖糍粑'],
            'source': '小红书',
            'link': 'https://www.xiaohongshu.com/...',
            'image': '',
            'collectedAt': datetime.now().isoformat()
        }
    ]
    
    data = load_existing_shops()
    data['shops'] = sample_shops
    data['lastUpdate'] = datetime.now().isoformat()
    save_shops(data)
    print(f"✅ 已添加 {len(sample_shops)} 个示例店铺")

if __name__ == '__main__':
    print("👑 外卖女王 - 数据采集")
    print("=" * 40)
    
    # 添加示例数据
    add_sample_shops()
    
    print(f"\n📊 数据已保存到：{SHOPS_FILE}")
    print("🌐 访问 web/index.html 查看结果")
