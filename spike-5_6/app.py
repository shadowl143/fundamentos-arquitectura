from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

SECRET_KEY = "mi_clave_super_secreta"

# Usuarios de ejemplo
USERS = {
    "julian.lara": {"password": "123456", "role": "admin"},
    "jose.torres": {"password": "123456", "role": "user"},
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"message": "Token requerido"}), 401

        try:
            token = auth_header.split(" ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = USERS.get(data["sub"])

            if not current_user:
                return jsonify({"message": "Usuario no válido"}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401
        except Exception:
            return jsonify({"message": "Formato de token inválido"}), 401

        return f(current_user, *args, **kwargs)
    return decorated


def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated(current_user, *args, **kwargs):
            if current_user["role"] != required_role:
                return jsonify({"message": "No tienes permiso"}), 403
            return f(current_user, *args, **kwargs)
        return decorated
    return decorator


@app.route("/login", methods=["POST"])
def login():
    auth = request.get_json()
    username = auth.get("username")
    password = auth.get("password")

    user = USERS.get(username)

    if not user or user["password"] != password:
        return jsonify({"message": "Credenciales inválidas"}), 401

    token = jwt.encode({
        "sub": username,
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({"token": token})


@app.route("/admin-zone", methods=["GET"])
@token_required
@role_required("admin")
def admin_zone(current_user):
    return jsonify({
        "message": "Acceso concedido al área admin",
        "user": current_user
    })


@app.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return jsonify({
        "message": "Acceso concedido",
        "user": current_user
    })


if __name__ == "__main__":
    app.run(debug=True)