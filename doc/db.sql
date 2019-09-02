-- 基础角色表
CREATE TABLE `base_role_info`  (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `key` varchar(150) NOT NULL COMMENT '角色key',
  `name` varchar(150) NOT NULL COMMENT '角色名字',
  `description` varchar(150) COMMENT '角色描述',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- 基础路由表
CREATE TABLE `base_route_info`  (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  -- 路由的path
  `path` varchar(150) COMMENT '路由路径',
  -- 路由的名字
  `name` varchar(150) COMMENT '名字',
  -- 使用的组件
  `component` varchar(150) COMMENT '组件',
  -- 当你一个路由下面的 children 声明的路由大于1个时，自动会变成嵌套的模式--如组件页面
  -- 只有一个时，会将那个子路由当做根路由显示在侧边栏--如引导页面
  -- 若你想不管路由下面的 children 声明的个数都显示你的根路由
  -- 你可以设置 alwaysShow: true，这样它就会忽略之前定义的规则，一直显示根路由
  `alwaysShow` tinyint(1) default 0 COMMENT '是否自动嵌套',
  `redirect` varchar(150) COMMENT '当设置 noRedirect 的时候该路由在面包屑导航中不可被点击',
  `meta` text COMMENT 'meta info',
  `hidden` tinyint(1) default 0 COMMENT '当设置 true 的时候该路由不会再侧边栏出现 如401，login等页面，或者如一些编辑页面/edit/1',
  `parent_route_id` int(10) COMMENT '上级路由ID',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;


-- 角色路由表
CREATE TABLE `base_role_route_info`  (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `role_id` varchar(150) NOT NULL COMMENT '角色ID',
  `route_id` varchar(150) NOT NULL COMMENT '路由ID',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- 用户角色表
