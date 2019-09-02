-- 添加角色
insert into base_role_info(id, `key`, `name`, description) values(1, 'admin', '超级管理员', '超级管理员');
insert into base_role_info(id, `key`, `name`, description) values(2, 'editor', '编辑人员', '编辑人员');
insert into base_role_info(id, `key`, `name`, description) values(3, 'visitor', '访问人员', '访问人员');

-- 添加route
insert into base_route_info(id, path, `name`, component, alwaysShow, redirect, hidden,  meta) values(1, '/permission', '权限管理', 'layout/Layout', 1, '/permission/index', 0, '{"title": "permission", "icon": "lock", "roles": ["admin", "editor"]}');
insert into base_route_info(id, path, `name`, component, alwaysShow, redirect, hidden,  meta, parent_route_id) values(2, 'page', '页面权限', 'views/permission/page', 0, '', 0, '{"title": "页面权限", "roles": ["admin"]}', 1);
insert into base_route_info(id, path, `name`, component, alwaysShow, redirect, hidden,  meta, parent_route_id) values(3, 'directive', '直接权限', 'views/permission/directive', 0, '', 0, '{"title": "directivePermission"}', 1);
insert into base_route_info(id, path, `name`, component, alwaysShow, redirect, hidden,  meta, parent_route_id) values(4, 'role', '角色权限管理', 'views/permission/role', 0, '', 0, '{"title": "rolePermission",  "roles": ["admin"]}', 1);

-- 添加角色路由
insert into base_role_route_info(role_id, route_id) values(1, 1), (1, 2), (1, 3), (1, 4);
insert into base_role_route_info(role_id, route_id) values(2, 1), (2, 3);
insert into base_role_route_info(role_id, route_id) values(3, 1), (3, 3);