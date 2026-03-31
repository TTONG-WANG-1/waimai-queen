# 👑 外卖女王 - 深圳外卖推荐助手

基于真实评价的深圳外卖推荐工具，帮你快速找到附近的好吃的！

## 🌐 在线访问

**GitHub Pages**: https://ttong-wang-1.github.io/waimai-queen/web/index.html

## ✨ 核心功能

### 📍 精准定位
- **地铁线路选择**: 支持 1 号线、2 号线、5 号线、13 号线
- **地铁站选择**: 每条线路的所有站点
- **搜索范围**: 2 公里、3 公里、5 公里可选

### 🍱 智能推荐
- **距离计算**: 基于 Haversine 公式计算实际距离
- **换一批功能**: 每次显示 10 家不重复店铺
- **数据来源**: 小红书博主推荐 + 大众点评高分店铺

### 📊 店铺信息
- 店铺名称、评分、人均价格
- 菜系类型、所在区域
- 推荐菜品
- 距离当前位置的公里数
- 直达链接（Google 智能直达）

## 🛠️ 技术栈

- **前端**: 原生 HTML/CSS/JavaScript
- **数据**: JSON 格式存储
- **部署**: GitHub Pages
- **距离计算**: Haversine 公式

## 📁 项目结构

```
waimai-queen/
├── web/
│   └── index.html      # 主页面
├── data/
│   ├── metro.json      # 深圳地铁线路数据
│   └── shops.json      # 外卖店铺数据
├── build.py            # 数据生成脚本
└── README.md           # 说明文档
```

## 🚀 本地开发

```bash
# 克隆项目
git clone https://github.com/TTONG-WANG-1/waimai-queen.git
cd waimai-queen

# 使用任意 HTTP 服务器启动
python3 -m http.server 8000

# 访问 http://localhost:8000/web/index.html
```

## 📝 数据更新

### 添加新店铺
编辑 `data/shops.json`，添加新店铺数据：
```json
{
  "id": "31",
  "name": "店铺名称",
  "lat": 22.55,
  "lng": 113.98,
  "area": "南山",
  "subArea": "科技园",
  "rating": "4.5",
  "price": "60 元",
  "cuisine": "菜系",
  "recs": ["推荐菜 1", "推荐菜 2"],
  "source": "小红书/大众点评"
}
```

### 更新地铁数据
编辑 `data/metro.json`，添加新线路或站点。

## 📈 未来计划

- [ ] 添加更多地铁线路（7 号线、9 号线、11 号线等）
- [ ] 增加店铺收藏功能
- [ ] 增加用户评价功能
- [ ] 添加更多数据源（美团、饿了么）
- [ ] 支持按菜系筛选
- [ ] 支持按价格筛选

## 📄 许可证

MIT License

---

## 🗺️ 高德地图 API 集成（可选）

使用高德地图 API 自动获取店铺精准位置：

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置 API Key
cp .env.example .env
# 编辑 .env 填入你的 AMAP_KEY

# 3. 批量更新店铺位置
python3 gaode_api.py
```

**申请 API Key**: https://lbs.amap.com/
**详细文档**: [GAODE_API_GUIDE.md](GAODE_API_GUIDE.md)

## 📈 未来计划

- [x] 高德地图 API 集成
- [ ] 添加更多地铁线路（7 号线、9 号线、11 号线等）
- [ ] 增加店铺收藏功能
- [ ] 增加用户评价功能
- [ ] 添加更多数据源（美团、饿了么）
- [ ] 支持按菜系筛选
- [ ] 支持按价格筛选
- [ ] 实时定位功能

## 📄 许可证

MIT License

---

**最后更新**: 2026-03-31
**店铺数量**: 44 家
**覆盖线路**: 4 条地铁线路
**API 集成**: 高德地图（待配置）
