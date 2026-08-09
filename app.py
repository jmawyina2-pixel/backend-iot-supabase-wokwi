from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def guardar_medicion(data):
    url = f"{SUPABASE_URL}/rest/v1/mediciones"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    r = requests.post(url, headers=headers, json=data, timeout=15)
    return r.json()

@app.get("/")
def inicio():
    return jsonify({"proyecto": "Backend IoT Histórico", "estado": "funcionando"})

@app.post("/mediciones")
def crear_medicion():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    campos = ["device_id", "tipo_variable", "valor", "unidad"]
    faltantes = [c for c in campos if c not in data]
    if faltantes:
        return jsonify({"error": "Faltan campos", "campos": faltantes}), 400

    try:
        data["valor"] = float(data["valor"])
        res = guardar_medicion(data)
        return jsonify({
            "mensaje": "Medición guardada correctamente",
            "data": res
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/mediciones")
def consultar_mediciones():
    device_id = request.args.get("device_id")
    variable = request.args.get("tipo_variable")
    limit = request.args.get("limit", "50")

    if not SUPABASE_URL or not SUPABASE_KEY:
        return jsonify({"error": "Variables de entorno SUPABASE_URL o SUPABASE_KEY no configuradas en Render"}), 500

    url = f"{SUPABASE_URL}/rest/v1/mediciones"
    params = {"select": "*", "order": "timestamp.desc", "limit": limit}

    if device_id:
        params["device_id"] = f"eq.{device_id}"
    if variable:
        params["tipo_variable"] = f"eq.{variable}"

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }

    try:
        r = requests.get(url, headers=headers, params=params, timeout=15)
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": "Error al conectar con Supabase", "detalle": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
