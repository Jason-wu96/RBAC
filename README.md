# rabc权限组件

## 开发环境
   * python3.6
   * django2.2
   * sqlite3(也可以使用mysql等数据库）
  
## 设计流程

#### 1.关系表的创建
  
          users    <--------->    roles  <--------->    permission    <--------    group
                      多对多                多对多                        多对一
                  
                  
####  2.创建登录页面

         （1）在app01.views中将用户id注册到session中
         （2）在rbac.server.permission_session中将登录用户所有权限注册和菜单栏权限到session中
         
####  3.建立中间件 verifier.py

          登录前做验证，看用户是否拥有权限
          
          
####   4.左侧菜单栏

           为了使用户表和角色表同时集成一个模板，又能实母版和数据统一继承，用自定义inclusion_tag标签
           
           
####    5.前端知识

            左侧菜单栏主要运用了fixed，右侧表单为了实现滑动运用了overflow滚动条，还有一些bootstrap的应用
            
            
## 结果

#### rbac插件很好地实现了用户权限的登录验证，在以后的项目中可以直接引用，只是前端页面做得好不够好，以后有时间修改一下



### 未完待续.....

          
         

    
