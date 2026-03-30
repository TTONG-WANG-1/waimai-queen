#!/usr/bin/env python3
"""
外卖女王 - 飞书定时推送脚本
每天 11:00 和 17:00 推送外卖推荐
"""
import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / 'data'
SHOPS_FILE = DATA_DIR / 'shops.json'

def get_today_shops(area='南山区', sub_area='科技园', limit=5):
    """获取今日推荐店铺"""
    if not SHOPS_FILE.exists():
        return []
    
    with open(SHOPS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    shops = data.get('shops', [])
    filtered = [s for s in shops if s.get('area') == area and s.get('subArea') == sub_area]
    return filtered[:limit]

def format_push_message(shops, meal_type='午餐'):
    """格式化推送消息"""
    if not shops:
        return f"😢 暂无{meal_type}推荐，换个区域试试吧～"
    
    lines = [f"👑 外卖女王 · {meal_type}推荐", ""]
    
    for i, shop in enumerate(shops, 1):
        lines.append(f"{i}. 🍜 {shop['name']}")
        lines.append(f"   ⭐ 评分：{shop.get('rating', '暂无')}")
        lines.append(f"   💰 人均：{shop.get('price', '未知')}")
        lines.append(f"   🌟 推荐：{', '.join(shop.get('recommendations', []))}")
        lines.append("")
    
    lines.append(f"📍 区域：{shops[0].get('area', '')}·{shops[0].get('subArea', '')}")
    lines.append(f"🕐 更新时间：{datetime.now().strftime('%m-%d %H:%M')}")
    lines.append("")
    lines.append("🌐 查看更多：https://ttong-wang-1.github.io/waimai-queen/")
    
    return '\n'.join(lines)

if __name__ == '__main__':
    # 测试推送消息
    shops = get_today_shops()
    message = format_push_message(shops, '午餐')
    print(message)
