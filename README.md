# FlaskWeb

学习Python-Flask记录

### 参考书：Flask Web Development: Developing Web Applications with Python-Flask Web 开发

### 结构：大型程序的结构：配置选项，程序包，启动脚本，需求文件，单元测试等

### 目前已完成：

- 模版Flask-Bootstrap
- Web表单：Flask-WTF
- 数据库：Flask-SQLALchemy
- 集成Python shell：Flask-Script
- 数据库前移：Flak-Migrate
- 用户认证：Flask-Login
- 新用户注册
- 更改密码
- 重设密码
- 修改电子邮件地址
- 角色在数据库中的表示

### 版本说明：

- v1.06 把角色写入数据库
- v1.05 实现重设修改电子邮件地址功能
- v1.04 实现更改密码功能
- v1.03 新用户注册，发送验证邮件，点击邮件中的链接，验证成功
- v1.02 增加了.gitignore文件，以忽略.pyc等文件

### 问题

重设密码功能无效，各步都实现了，但是在token验证处出问题，导致无法修改密码：

```python
data.get('resetkey') != self.id
```

暂时没找到原因，为什么上述不相等

