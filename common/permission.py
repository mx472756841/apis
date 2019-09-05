import json

from app import db


def get_roles():
    """
    获取所有角色路由，包含权限信息
    :return:
    """
    roles_info = []
    sql = """
        select id, `key`, `name`, description from base_role_info
    """
    cur = db.session.execute(sql)
    all_roles = cur.fetchall()

    for role_id, key, name, desc in all_roles:
        routes = get_role_routes(role_id)
        roles_info.append({
            "key": key,
            "name": name,
            "description": desc,
            "routes": routes
        })
    print(roles_info)
    return roles_info


def get_role_routes(role_id):
    """
    获取指定角色的路由，并按照上下级关系排列好
    :param role_id:
    :return:
    """
    sql = """
        select 
            a.id, a.path, a.name, a.component, a.alwaysShow,
            a.redirect, a.meta, a.hidden
        from base_route_info a, base_role_route_info b
        where a.id = b.route_id 
        and b.role_id = :role_id
        and a.parent_route_id is null
    """

    cur = db.session.execute(sql, {"role_id": role_id})
    routes = cur.fetchall()
    return_routes = []
    for route in routes:
        childs = get_child_routes(role_id, route[0])
        data = {
            "path": route[1],
            "name": route[2],
            "component": route[3],
            "alwaysShow": True if route[4] else False,
            "redirect": route[5],
            "hidden": True if route[7] else False
        }
        if route[6]:
            data['meta'] = json.loads(route[6])

        if childs:
            data['children'] = childs

        return_routes.append(data)

    return return_routes


def get_child_routes(role_id, route_id):
    """
    获取指定父级route和角色的routes
    :return:
    """
    sql = """
        select 
            a.id, a.path, a.name, a.component, a.alwaysShow,
            a.redirect, a.meta, a.hidden
        from base_route_info a, base_role_route_info b
        where a.id = b.route_id 
        and b.role_id = :role_id
        and a.parent_route_id = :route_id
    """
    cur = db.session.execute(sql, {"role_id": role_id, "route_id": route_id})
    routes = cur.fetchall()
    return_routes = []
    for route in routes:
        # 继续递归获取当前的子集
        childs = get_child_routes(role_id, route[0])
        data = {
            "path": route[1],
            "name": route[2],
            "component": route[3],
            "alwaysShow": True if route[4] else False,
            "redirect": route[5],
            "hidden": True if route[7] else False
        }
        if route[6]:
            data['meta'] = json.loads(route[6])

        if childs:
            data['children'] = childs

        return_routes.append(data)
    return return_routes
