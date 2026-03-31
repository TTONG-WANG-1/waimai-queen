#!/usr/bin/env python3
"""
高德地图 API 集成 - 获取店铺精准位置信息
文档：https://lbs.amap.com/api/webservice/guide/api/search
"""
import json
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 高德地图 API 配置
AMAP_CONFIG = {
    "key": os.getenv("AMAP_KEY", ""),
    "secret": os.getenv("AMAP_SECRET", ""),
    "city": os.getenv("DEFAULT_CITY", "深圳"),
    "poi_type": os.getenv("POI_TYPE", "050000"),
}

def search_poi(keywords, city="深圳", types="050000", offset=25):
    """
    搜索 POI（兴趣点）
    
    Args:
        keywords: 搜索关键词（店铺名称）
        city: 城市名称
        types: POI 类型代码（050000=餐饮）
        offset: 返回数量
    
    Returns:
        dict: POI 搜索结果
    """
    url = "https://restapi.amap.com/v3/place/text"
    params = {
        "key": AMAP_CONFIG["key"],
        "keywords": keywords,
        "city": city,
        "types": types,
        "offset": offset,
        "output": "json"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"搜索失败 {keywords}: {e}")
        return None

def geocode_address(address, city="深圳"):
    """
    地理编码 - 将地址转换为经纬度
    
    Args:
        address: 地址字符串
        city: 城市名称
    
    Returns:
        tuple: (经度，纬度) 或 None
    """
    url = "https://restapi.amap.com/v3/geocode/geo"
    params = {
        "key": AMAP_CONFIG["key"],
        "address": f"{city}{address}",
        "output": "json"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "1" and data.get("geocodes"):
            location = data["geocodes"][0]["location"]
            lng, lat = location.split(",")
            return float(lng), float(lat)
        return None
    except Exception as e:
        print(f"地理编码失败 {address}: {e}")
        return None

def get_shop_location(shop_name, area=""):
    """
    获取店铺位置信息
    
    Args:
        shop_name: 店铺名称
        area: 所在区域
    
    Returns:
        dict: 包含经纬度等信息
    """
    keywords = f"{shop_name}"
    if area:
        keywords = f"{area}{shop_name}"
    
    result = search_poi(keywords)
    
    if result and result.get("status") == "1" and result.get("pois"):
        poi = result["pois"][0]
        location = poi.get("location", "").split(",")
        return {
            "name": poi.get("name", shop_name),
            "lat": float(location[1]) if len(location) > 1 else None,
            "lng": float(location[0]) if len(location) > 0 else None,
            "address": poi.get("address", ""),
            "type": poi.get("type", ""),
            "tel": poi.get("tel", ""),
            "rating": poi.get("biz_ext", {}).get("rating", "")
        }
    return None

def batch_update_shops(shops_file, output_file=None):
    """
    批量更新店铺位置信息
    
    Args:
        shops_file: 输入店铺 JSON 文件
        output_file: 输出文件路径
    """
    if output_file is None:
        output_file = shops_file
    
    # 读取现有数据
    with open(shops_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    shops = data.get("shops", [])
    updated_count = 0
    
    print(f"开始更新 {len(shops)} 家店铺位置...")
    
    for i, shop in enumerate(shops):
        if shop.get("lat") and shop.get("lng"):
            print(f"[{i+1}/{len(shops)}] {shop['name']} - 已有坐标，跳过")
            continue
        
        print(f"[{i+1}/{len(shops)}] {shop['name']} - 正在搜索...")
        location = get_shop_location(shop["name"], shop.get("area", ""))
        
        if location and location["lat"] and location["lng"]:
            shop["lat"] = location["lat"]
            shop["lng"] = location["lng"]
            shop["address"] = location.get("address", "")
            updated_count += 1
            print(f"  ✅ 更新：{location['lat']}, {location['lng']}")
        else:
            print(f"  ⚠️ 未找到")
    
    # 保存更新后的数据
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n完成！更新了 {updated_count}/{len(shops)} 家店铺")
    return updated_count

if __name__ == "__main__":
    # 测试示例
    print("高德地图 API 集成测试")
    print("=" * 50)
    
    # 检查 API Key
    if AMAP_CONFIG["key"] == "YOUR_AMAP_KEY_HERE":
        print("⚠️ 请先配置 API Key！")
        print("\n申请步骤：")
        print("1. 访问 https://lbs.amap.com/")
        print("2. 注册/登录账号")
        print("3. 进入控制台 -> 应用管理 -> 我的应用")
        print("4. 创建新应用，选择'Web 服务'类型")
        print("5. 复制 Key 并替换 gaode_api.py 中的 YOUR_AMAP_KEY_HERE")
    else:
        # 测试搜索
        test_shops = ["木屋烧烤 南山", "海底捞 深圳"]
        for shop in test_shops:
            result = search_poi(shop)
            if result and result.get("pois"):
                poi = result["pois"][0]
                print(f"\n✅ {poi['name']}")
                print(f"   地址：{poi.get('address', '')}")
                print(f"   位置：{poi.get('location', '')}")
