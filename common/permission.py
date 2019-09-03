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

    return roles_info


def get_role_routes(role_id):
    sql = """
        select a.*, b.*
        from base_route_info a, base_role_route_info b
        where a.id = b.route_id and b.role_id = :role_id
    """

    cur = db.session.execute(sql, {"role_id": role_id})
    print(cur.fetchall())
    return []


def get_routes():
    """
    获取指定用户的routes
    :return:
    """
    pass
