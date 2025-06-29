# 虚拟环境使用说明

## 问题解决

您之前遇到的依赖冲突问题已经通过创建虚拟环境解决。虚拟环境可以隔离项目依赖，避免与系统全局Python包产生冲突。

## 使用方法

### 方法1：使用启动脚本（推荐）
```bash
./start_venv.sh
```

### 方法2：手动激活虚拟环境
```bash
# 激活虚拟环境
source venv/bin/activate

# 启动服务器
python web_server.py
```

### 方法3：使用原有的start.sh脚本
```bash
# 确保在虚拟环境中
source venv/bin/activate

# 然后使用原有脚本
bash start.sh start
```

## 虚拟环境管理

### 激活虚拟环境
```bash
source venv/bin/activate
```

### 退出虚拟环境
```bash
deactivate
```

### 重新安装依赖（如果需要）
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 删除虚拟环境（如果需要重新创建）
```bash
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 注意事项

1. **每次使用前都需要激活虚拟环境**
2. **虚拟环境已经包含了所有必要的依赖**
3. **如果添加新的依赖，记得更新requirements.txt**
4. **虚拟环境文件夹(venv)不应该提交到版本控制系统**

## 访问系统

启动后，在浏览器中访问：http://localhost:8888

## 常见问题

### Q: 为什么需要虚拟环境？
A: 虚拟环境可以避免不同项目之间的Python包版本冲突，确保项目依赖的独立性。

### Q: 如何知道虚拟环境是否激活？
A: 命令行前面会显示 `(venv)` 前缀。

### Q: 可以删除venv文件夹吗？
A: 可以，但删除后需要重新创建虚拟环境并安装依赖。 