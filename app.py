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
    r.raise_for_status()
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
        return jsonify({
            "mensaje": "Medición guardada correctamente",
            "data": guardar_medicion(data)
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/mediciones")
def consultar_mediciones():
    device_id = request.args.get("device_id")
    variable = request.args.get("tipo_variable")
    limit = request.args.get("limit", "50")

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
    r = requests.get(url, headers=headers, params=params, timeout=15)
    r.raise_for_status()
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)