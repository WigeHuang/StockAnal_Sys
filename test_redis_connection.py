#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Redis连接测试脚本
用于测试Redis连接是否正常
"""

import os
import sys
import redis
from dotenv import load_dotenv

def test_redis_connection():
    """测试Redis连接"""
    # 加载环境变量
    load_dotenv()
    
    # 获取Redis配置
    redis_url = os.getenv('REDIS_URL')
    use_redis = os.getenv('USE_REDIS_CACHE', 'False').lower() == 'true'
    
    print("=== Redis连接测试 ===")
    print(f"USE_REDIS_CACHE: {use_redis}")
    print(f"REDIS_URL: {redis_url}")
    print()
    
    if not use_redis:
        print("❌ Redis缓存未启用，请设置 USE_REDIS_CACHE=True")
        return False
    
    if not redis_url:
        print("❌ 未配置REDIS_URL")
        return False
    
    try:
        # 创建Redis连接
        print("正在连接Redis...")
        r = redis.from_url(redis_url)
        
        # 测试连接
        r.ping()
        print("✅ Redis连接成功!")
        
        # 测试基本操作
        print("正在测试基本操作...")
        
        # 设置测试键
        test_key = "test_connection"
        test_value = "Hello Redis!"
        r.set(test_key, test_value, ex=60)  # 60秒过期
        print(f"✅ 设置键值: {test_key} = {test_value}")
        
        # 获取测试键
        retrieved_value = r.get(test_key)
        if retrieved_value:
            retrieved_value = retrieved_value.decode('utf-8')
            print(f"✅ 获取键值: {test_key} = {retrieved_value}")
        else:
            print("❌ 获取键值失败")
            return False
        
        # 删除测试键
        r.delete(test_key)
        print(f"✅ 删除测试键: {test_key}")
        
        # 获取Redis信息
        info = r.info()
        print(f"✅ Redis版本: {info.get('redis_version', 'Unknown')}")
        print(f"✅ 连接数: {info.get('connected_clients', 'Unknown')}")
        print(f"✅ 内存使用: {info.get('used_memory_human', 'Unknown')}")
        
        print("\n🎉 Redis连接测试完成，所有功能正常!")
        return True
        
    except redis.ConnectionError as e:
        print(f"❌ Redis连接失败: {e}")
        print("\n可能的原因:")
        print("1. Redis服务器未启动")
        print("2. 网络连接问题")
        print("3. 端口被防火墙阻止")
        print("4. Redis URL格式错误")
        return False
        
    except redis.AuthenticationError as e:
        print(f"❌ Redis认证失败: {e}")
        print("\n可能的原因:")
        print("1. 密码错误")
        print("2. 用户名错误")
        print("3. Redis配置了认证但URL中没有提供密码")
        return False
        
    except Exception as e:
        print(f"❌ Redis测试失败: {e}")
        return False

def show_redis_url_examples():
    """显示Redis URL示例"""
    print("\n=== Redis URL格式示例 ===")
    print("1. 本地Redis (无密码):")
    print("   REDIS_URL=redis://localhost:6379")
    print()
    print("2. 远程Redis (无密码):")
    print("   REDIS_URL=redis://192.168.1.100:6379")
    print()
    print("3. 带密码的Redis:")
    print("   REDIS_URL=redis://:your_password@host:port")
    print()
    print("4. 带用户名和密码的Redis:")
    print("   REDIS_URL=redis://username:password@host:port")
    print()
    print("5. 带数据库编号的Redis:")
    print("   REDIS_URL=redis://:password@host:port/1")
    print()
    print("6. SSL连接的Redis:")
    print("   REDIS_URL=rediss://:password@host:port")
    print()

if __name__ == "__main__":
    print("Redis连接测试工具")
    print("=" * 50)
    
    # 显示Redis URL示例
    show_redis_url_examples()
    
    # 测试连接
    success = test_redis_connection()
    
    if success:
        print("\n✅ 可以启用Redis缓存了!")
        print("请在.env文件中设置:")
        print("USE_REDIS_CACHE=True")
    else:
        print("\n❌ 请检查Redis配置后重试")
        sys.exit(1) 