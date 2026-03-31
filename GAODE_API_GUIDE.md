# 🗺️ 高德地图 API 集成指南

## 📋 第一步：申请 API Key

### 1. 注册账号
访问 https://lbs.amap.com/ 并注册/登录高德开放平台账号

### 2. 创建应用
1. 进入 **控制台** → **应用管理** → **我的应用**
2. 点击 **创建新应用**
3. 填写应用信息：
   - **应用名称**: 外卖女王
   - **应用类型**: Web 服务
   - **备注**: 外卖推荐助手

### 3. 添加 Key
1. 在应用下点击 **添加 Key**
2. 选择 **Web 服务** 类型
3. 白名单设置：
   - 开发环境：`0.0.0.0/0`（仅测试用）
   - 生产环境：填写你的服务器 IP
4. 复制生成的 **Key**

### 4. 配置 Key
将 Key 填入 `gaode_api.py`：
```python
AMAP_CONFIG = {
    "key": "你的 API Key",  # 替换这里
    "secret": "",
}
```

## 💰 配额说明

### 免费额度
- **个人开发者**: 5 万次/天
- **企业开发者**: 100 万次/天
- **QPS 限制**: 50 次/秒

### 我们的使用量估算
- 单次搜索：约 1 次调用
- 更新 44 家店铺：约 44 次调用
- 每日更新：约 50-100 次调用
- **月度使用**: 约 1500-3000 次（远低于免费额度）

## 🚀 使用方法

### 1. 安装依赖
```bash
pip install requests
```

### 2. 测试 API
```bash
cd /home/wangtong/openclaw/workspace/waimai-queen
python3 gaode_api.py
```

### 3. 批量更新店铺位置
```bash
python3 gaode_api.py
# 或手动调用
python3 -c "from gaode_api import batch_update_shops; batch_update_shops('web/data/shops.json')"
```

## 📊 API 功能

### 1. POI 搜索
搜索店铺位置信息：
```python
from gaode_api import search_poi

result = search_poi("木屋烧烤 南山科技园")
if result and result.get("pois"):
    poi = result["pois"][0]
    print(f"名称：{poi['name']}")
    print(f"地址：{poi['address']}")
    print(f"位置：{poi['location']}")  # 经度，纬度
```

### 2. 地理编码
将地址转换为经纬度：
```python
from gaode_api import geocode_address

location = geocode_address("深圳市南山区科技园")
if location:
    lng, lat = location
    print(f"经度：{lng}, 纬度：{lat}")
```

### 3. 获取店铺位置
```python
from gaode_api import get_shop_location

info = get_shop_location("木屋烧烤", "南山区")
if info:
    print(f"经纬度：{info['lat']}, {info['lng']}")
    print(f"地址：{info['address']}")
```

## 🔧 集成到现有流程

### 自动更新脚本
创建 `scripts/update_locations.py`：
```bash
#!/bin/bash
cd /home/wangtong/openclaw/workspace/waimai-queen
python3 gaode_api.py
git add web/data/shops.json
git commit -m "chore: 更新店铺位置信息"
git push
```

### 定期更新
使用 cron 每周更新一次：
```bash
# 每周一上午 9 点执行
0 9 * * 1 cd /home/wangtong/openclaw/workspace/waimai-queen && python3 gaode_api.py
```

## 📝 注意事项

### 1. API Key 安全
- ⚠️ **不要** 将 Key 提交到 GitHub
- ✅ 使用 `.env` 文件或环境变量
- ✅ 生产环境设置 IP 白名单

### 2. 错误处理
- 网络超时：设置 timeout=10
- 配额超限：检查每日使用量
- 搜索无结果：使用备选地址

### 3. 数据质量
- 优先使用"店铺名 + 区域"搜索
- 验证返回的经纬度是否合理
- 人工复核重要店铺位置

## 🎯 下一步优化

### 短期
1. ✅ 配置 API Key
2. ✅ 批量更新现有 44 家店铺
3. ✅ 验证位置准确性

### 中期
1. 添加店铺地址显示
2. 集成到网站前端
3. 添加"导航到此"功能

### 长期
1. 实时位置更新
2. 店铺营业状态
3. 用户位置定位

## 🔗 相关文档

- 高德开放平台：https://lbs.amap.com/
- Web 服务 API 文档：https://lbs.amap.com/api/webservice/guide
- POI 搜索 API：https://lbs.amap.com/api/webservice/guide/api/search
- 地理编码 API：https://lbs.amap.com/api/webservice/guide/api/geocoding

---

**最后更新**: 2026-03-31
**店铺数量**: 44 家
**预计 API 调用**: 50 次/天
