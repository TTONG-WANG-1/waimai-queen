# 👑 外卖女王 - 深圳外卖推荐助手

基于小红书等平台的深圳外卖推荐系统，解决"今天吃什么"的难题。

## 🌟 功能特点

- 📍 **区域切换**：支持南山/福田/罗湖/宝安等深圳主要区域
- 🍱 **智能推荐**：综合评分、价格、销量等多维度推荐
- 📊 **数据来源**：小红书、大众点评真实食客评价
- ⏰ **定时推送**：每天 11:00/17:00 飞书推送
- 🌐 **可交互网页**：GitHub Pages 部署，可分享

## 🚀 快速开始

### 1. 查看网页

```bash
# 在浏览器打开
open web/index.html
```

### 2. 更新数据

```bash
# 运行数据采集脚本
python3 crawler/xiaohongshu.py
```

### 3. 部署到 GitHub Pages

```bash
# 推送到 GitHub
cd /home/wangtong/openclaw/workspace/waimai-queen
git init
git add .
git commit -m "Initial commit: 外卖女王 v1.0"
git remote add origin https://github.com/TTONG-WANG-1/waimai-queen.git
git push -u origin main
```

然后在 GitHub 仓库设置中启用 GitHub Pages。

## 📁 项目结构

```
waimai-queen/
├── web/                    # 前端网页
│   └── index.html          # 主页面
├── crawler/                # 数据采集
│   └── xiaohongshu.py      # 小红书采集
├── push/                   # 推送服务
│   └── feishu_push.py      # 飞书推送
├── data/                   # 数据存储
│   ├── areas.json          # 区域配置
│   └── shops.json          # 店铺数据
├── config.py               # 配置文件
└── README.md               # 说明文档
```

## 📋 待办事项

- [ ] 实现小红书自动采集（目前手动添加）
- [ ] 添加大众点评数据采集
- [ ] 实现自动定位功能
- [ ] 添加个人口味偏好
- [ ] 定时推送自动化

## 📝 使用说明

### 添加新店铺

编辑 `data/shops.json`，添加新店铺数据：

```json
{
  "id": "4",
  "name": "店铺名称",
  "area": "南山区",
  "subArea": "科技园",
  "rating": "4.5",
  "price": "人均 50 元",
  "recommendations": ["推荐菜 1", "推荐菜 2"],
  "source": "小红书",
  "link": "小红书笔记链接",
  "collectedAt": "2026-03-30T18:00:00"
}
```

### 测试推送

```bash
python3 push/feishu_push.py
```

## 🙏 致谢

数据来源：
- 小红书：https://www.xiaohongshu.com/
- 大众点评：https://www.dianping.com/

---

© 2026 外卖女王 👑
