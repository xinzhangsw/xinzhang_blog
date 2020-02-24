## 这是什么
一次Django的web实践，参考了[追梦人物的博客](https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial)和[刘江的博客](https://www.liujiangblog.com/course/django/)并在此基础上实现了新的内容
## 在本地运行项目
1. 克隆至本地
   ```
   git clone https://github.com/xinzhangsw/xinzhang_blog.git
   ```
2. 安装依赖
   ```
   pipenv install
   ```

3. 迁移数据库
   ```
   pipenv run python manage.py migrate
   ```
4. 运行本地环境
   ```
   pipenv run python manage.py createsuperuser
   pipenv run python manage.py runserver
   ```
5. 访问<u>127.0.0.1:8000</u>
