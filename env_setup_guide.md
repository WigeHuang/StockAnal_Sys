# OpenAI API 配置指南

## 🎯 快速开始

### 1. 获取OpenAI API密钥
API秘钥：
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

1. **注册账户**: 访问 [OpenAI Platform](https://platform.openai.com/)
2. **验证邮箱**: 完成邮箱验证
3. **添加支付方式**: 绑定信用卡或借记卡
4. **创建API密钥**: 
   - 进入 "API Keys" 页面
   - 点击 "Create new secret key"
   - 复制生成的密钥

### 2. 创建环境配置文件

在项目根目录创建 `.env` 文件：

```bash
# API 提供商 (OpenAI SDK)
API_PROVIDER=openai

# OpenAI API 配置
OPENAI_API_URL=https://api.openai.com/v1
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_API_MODEL=gpt-4o
NEWS_MODEL=gpt-4o

# 功能调用模型
FUNCTION_CALL_MODEL=gpt-4o

# QA上下文数量
MAX_QA=10

# 其他配置
REDIS_URL=redis://localhost:6379
USE_REDIS_CACHE=False
DATABASE_URL=sqlite:///data/stock_analyzer.db
USE_DATABASE=False
LOG_LEVEL=INFO
LOG_FILE=logs/stock_analyzer.log
```

### 3. 模型选择建议

#### 推荐配置 (平衡性能和成本)
```bash
OPENAI_API_MODEL=gpt-4o
NEWS_MODEL=gpt-4o
FUNCTION_CALL_MODEL=gpt-4o
```

#### 经济配置 (降低成本)
```bash
OPENAI_API_MODEL=gpt-4o-mini
NEWS_MODEL=gpt-4o-mini
FUNCTION_CALL_MODEL=gpt-4o-mini
```

#### 高性能配置 (最佳效果)
```bash
OPENAI_API_MODEL=gpt-4o
NEWS_MODEL=gpt-4o
FUNCTION_CALL_MODEL=gpt-4o
```

## 💡 使用技巧

### 1. 成本控制
- 使用 `gpt-4o-mini` 进行日常对话
- 使用 `gpt-4o` 进行复杂分析
- 设置使用量限制

### 2. 功能测试
```bash
# 启动系统
./start_venv.sh

# 访问智能问答页面
http://localhost:8888/qa
```

### 3. 监控使用量
- 在 OpenAI Dashboard 查看使用情况
- 设置使用量警报
- 定期检查账单

## 🔧 故障排除

### 常见问题

1. **API密钥无效**
   - 检查密钥是否正确复制
   - 确认账户有足够余额

2. **请求超时**
   - 检查网络连接
   - 尝试使用更快的模型

3. **配额限制**
   - 检查账户配额
   - 升级到付费计划

## 📊 成本估算

### 典型使用场景

| 功能 | 每次调用 | 月使用100次 | 月费用 |
|------|----------|-------------|--------|
| 股票分析 | ~2000 tokens | 200,000 tokens | ~$0.50 |
| 智能问答 | ~500 tokens | 50,000 tokens | ~$0.13 |
| 情景预测 | ~1000 tokens | 100,000 tokens | ~$0.25 |

**总计**: 约 $0.88/月 (使用 gpt-4o-mini)

## 🎉 开始使用

配置完成后，您就可以享受以下AI功能：

- 🤖 **智能股票分析**
- 💬 **多轮对话问答**
- 📈 **市场情景预测**
- 📰 **实时新闻分析**
- 🎯 **投资建议生成**

享受AI增强的股票分析体验！ 


### DeepSeek
https://platform.deepseek.com/
使用网易邮箱（2020）绑定，使用微信扫码登录
api key: sk-bd2a7e8394c745338a15f926c0e611a0